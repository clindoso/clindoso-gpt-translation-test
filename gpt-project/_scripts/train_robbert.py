from transformers import RobertaTokenizer, EncoderDecoderModel, Seq2SeqTrainingArguments, Seq2SeqTrainer
from datasets import load_dataset, Dataset, concatenate_datasets
import pandas as pd
import os
from term_scraper import extract_terms_from_directory
import config
from accelerate import Accelerator, DataLoaderConfiguration

accelerator = Accelerator(
    dataloader_config=DataLoaderConfiguration(
        dispatch_batches=None,
        split_batches=False,
        even_batches=True,
        use_seedable_sampler=True
    )
)

# Initialize tokenizer from BERT
# en_model_checkpoint = "bert-base-cased"
# en_tokenizer = AutoTokenizer.from_pretrained(en_model_checkpoint)

def initialize_language_model(lang="nl"):
    """
    Initializes language model.
    Returns tm_path.
    """
    language_models = config.LANGUAGE_MODELS
    if lang in language_models:
        tm_path = language_models[lang]["tm_path"]
    else:
        raise ValueError ("""
                You entered an invalid language code. Use one of the following:
                "de" for German
                "es" for Spanish
                "fr" for French
                "it" for Italian
                "nl" for Dutch
            """)
    
    return tm_path

# Define tokenizer functions
def tokenize_function(dataset, tokenizer):
    print("Batch size:", len(dataset['en']))  # Check batch size
    print("Sample data:", dataset['en'][:1], dataset['nl'][:1])  # Print first example of the batch
    return tokenizer(dataset['en'], dataset['nl'],
                     truncation=True,
                     padding="max_length",
                     max_length=512,
                     return_overflowing_tokens=False,
                     return_tensors="pt")

def prepare_data(dataset, tokenizer):
    def tokenize_labels(example, tokenizer):
        labels = tokenizer.encode(example['nl'], truncation=True, padding="max_length", max_length=512)
        example['labels'] = labels
        return example

    # Apply the tokenize_labels function to each example in the dataset
    dataset = dataset.map(tokenize_labels, fn_kwargs={'tokenizer': tokenizer})
    return dataset

def ensure_input_fields(batch):
    fields_to_include = ['input_ids', 'attention_mask']
    if 'labels' in batch:
        fields_to_include.append('labels')
    return {field: batch[field] for field in fields_to_include if field in batch}


def main():

    # Initialize tokenizer from RoBERT
    robbert_checkpoint = config.ROBBERT_CHECKPOINT
    tokenizer = RobertaTokenizer.from_pretrained(robbert_checkpoint)

    # Get term tuples from directory
    termbase_directory = config.TERMBASE_DIRECTORY
    term_tuples = extract_terms_from_directory(termbase_directory, lang='nl')
    # Remove file path column
    term_tuples = [(tup[1], tup[2]) for tup in term_tuples]

    # Create dataset from term tuples
    df_terms = pd.DataFrame(term_tuples, columns=['en', 'nl'])
    term_dataset = Dataset.from_pandas(df_terms)

    # Tokenize term dataset
    tokenized_term_dataset = term_dataset.map(lambda dataset: tokenize_function(dataset, tokenizer), batched=True)

    # Initialize language
    tm_path = initialize_language_model()

    # Load dataset (create csv train and validation files)
    dataset = load_dataset('csv', data_files=tm_path)

    # Split 
    train_valid_split = dataset['train'].train_test_split(test_size=0.2)

    # Tokenize dataset splits
    tokenized_train_dataset = train_valid_split['train'].map(lambda dataset: tokenize_function(dataset, tokenizer), batched=True)
    tokenized_valid_dataset = train_valid_split['test'].map(lambda dataset: tokenize_function(dataset, tokenizer), batched=True)
    tokenized_valid_dataset = prepare_data(tokenized_valid_dataset, tokenizer)
    tokenized_valid_dataset = tokenized_valid_dataset.map(ensure_input_fields, batched=True)
    # Add terms to training dataset
    tokenized_train_dataset = concatenate_datasets([tokenized_train_dataset, tokenized_term_dataset])    
    tokenized_train_dataset = prepare_data(tokenized_train_dataset, tokenizer)
    tokenized_train_dataset = tokenized_train_dataset.map(ensure_input_fields, batched=True)

    print("Tokenized data example:", tokenized_train_dataset[0])
    print("Tokenized data example:", tokenized_valid_dataset[0])
    
    # Initialize encoder-decoder model
    model = EncoderDecoderModel.from_encoder_decoder_pretrained(
        encoder_pretrained_model_name_or_path=robbert_checkpoint,
        decoder_pretrained_model_name_or_path=robbert_checkpoint
        )
    model.config.decoder_start_token_id = tokenizer.cls_token_id
    model.config.pad_token_id = tokenizer.pad_token_id

    # Define training arguments
    training_args = Seq2SeqTrainingArguments(
        output_dir="./results",
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        weight_decay=0.01,
        save_total_limit=3,
        num_train_epochs=3,
        predict_with_generate=True
    )

    # Initialize the trainer
    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_train_dataset,
        eval_dataset=tokenized_valid_dataset,
        tokenizer=tokenizer
    )
    print("Final check before training")
    print("Train dataset sample:", tokenized_train_dataset[0])
    print("Validation dataset sample:", tokenized_valid_dataset[0])
    # Train the model
    trainer.train()

    print("Inspecting first entry of tokenized training dataset:", next(iter(tokenized_train_dataset)))

    # Initialize model and tokenizer save paths
    robbert_model_save_path = config.ROBBERT_MODEL_SAVE_PATH
    tokenizer_save_path = config.TOKENIZER_SAVE_PATH

    # Create directories if they do not exist
    os.makedirs(robbert_model_save_path, exist_ok=True)
    os.makedirs(tokenizer_save_path, exist_ok=True)
    
    # Save model
    trainer.model.save_pretrained(robbert_model_save_path)
    tokenizer.save_pretrained(tokenizer_save_path)

if __name__ == "__main__":
    main()
