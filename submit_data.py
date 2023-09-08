import json
import openai
import requests

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

openai.api_key = config["OPENAI_API_KEY"]
  # Replace with your actual API key

def submit_for_finetuning(jsonl_file_path):
    # Step 2: Upload the file
    with open(jsonl_file_path, 'rb') as f:
        response = openai.File.create(file=f, purpose="fine-tune")
    file_id = response['id']

    # Step 3: Create a fine-tuning job
    fine_tuning_data = {
        "training_file": file_id,
        "model": "gpt-3.5-turbo-0613"
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}"
    }

    fine_tuning_response = requests.post("https://api.openai.com/v1/fine_tuning/jobs", headers=headers, data=json.dumps(fine_tuning_data))
    fine_tuning_job_id = fine_tuning_response.json()['id']

    return fine_tuning_job_id

model_id = submit_for_finetuning("CSD.jsonl")
print(f"Fine-tuning started. Model ID: {model_id}")
