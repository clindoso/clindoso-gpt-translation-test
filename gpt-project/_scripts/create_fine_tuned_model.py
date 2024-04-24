import openai
import argparse
import config
import os

def parse_arguments():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Create fine-tuned model via OpenAI API")
    parser.add_argument("--tr", required=True, help="Training data file path")
    parser.add_argument("--vd", required=True, help="Validation data file path")
    args = parser.parse_args()
    return args.tr, args.vd

def initialize_open_ai_client():
    """
    Initialize OpenAI client by setting the API key from the config file.
    Raises an error if the API key is not configured.
    """
    if not hasattr(config, 'OPENAI_API_KEY') or not config.OPENAI_API_KEY:
        raise EnvironmentError("API key for OpenAI is not configured properly.")
    openai.api_key = config.OPENAI_API_KEY

def upload_file(file_path, client):
  """
  Upload file to OpenAI platform.

  Parameters:
    - file_path (str): Path of the file to be uploaded
    - client (obj): OpenAI client object
  Returns:
    - str: ID of the file uploaded to OpenAI platform.
  """
  # Check if file exists
  if not os.path.isfile(file_path):
     raise FileNotFoundError(f"The file '{file_path}' does not exist.")
  
  with open(file_path, "rb") as file:
    file = client.files.create(
      file=open(file, "rb"),
      purpose='fine-tune'
    )
    return file.id

def train_model(training_data_file_id, validation_data_file_id, client, gpt_model="gpt-3.5-turbo-0125"):
  """
  Create a fine-tuning job on OpenAI platform.

  Parameters:
    - training_data_file_id (str): Training data file ID from OpenAI platform
    - validation_data_file_id (str): Validation data file ID from OpenAI platform
    - client (obj): OpenAI client object
    - gpt_model (str): Base model for fine-tuning, default is 'gpt-3.5-turbo-0125'
  """
  fine_tuning_job = client.fine_tuning.jobs.create(
    training_file=training_data_file_id,
    validation_file=validation_data_file_id,
    model=gpt_model
  )

def main():
   
   # Initialize OpenAI client
   client = initialize_open_ai_client()

   # Parse command-line arguments
   training_data_file_path, validation_data_file_path = parse_arguments()
   # Upload training data to OpenAI 
   training_data_file = upload_file(training_data_file_path, client)
   
   # Upload validation data to OpenAI
   validation_data_file = upload_file(validation_data_file_path, client)

   # Train model
   train_model(training_data_file, validation_data_file, client)

if __name__ == "__main__":
   main()
