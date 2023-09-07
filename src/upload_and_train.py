import requests

API_KEY = 'YOUR_OPENAI_API_KEY'

headers = {
    'Authorization': f'Bearer {API_KEY}'
}

def upload_and_train():
    files = {
        'file': ('usafa_data.json', open('../prepared_data/usafa_data.json', 'rb'))
    }

    response = requests.post('https://api.openai.com/v1/files', headers=headers, files=files)
    file_id = response.json()['id']

    data = {
        "training_file": file_id,
        "model": "gpt-3.5-turbo-0613"
    }

    response = requests.post('https://api.openai.com/v1/fine_tuning/jobs', headers=headers, json=data)
    print("Training job initiated. Check the job status on OpenAI dashboard.")

if __name__ == "__main__":
    upload_and_train()
