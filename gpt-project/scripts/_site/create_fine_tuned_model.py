from openai import OpenAI
client = OpenAI()

client.fine_tuning.jobs.create(
  training_file="file-abc123",
  validation_file="", 
  model="gpt-3.5-turbo"
)