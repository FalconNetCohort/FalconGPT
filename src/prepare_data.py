import json

def prepare_data():
    with open('../data/usafa_documents.txt', 'r') as f:
        lines = f.readlines()

    messages = [{"role": "system", "content": "You are a chatbot trained on USAFA documents."}]

    for line in lines:
        messages.append({"role": "user", "content": line.strip()})
        # The assistant's content will be empty since this is for training
        messages.append({"role": "assistant", "content": ""})

    with open('../prepared_data/usafa_data.json', 'w') as f:
        json.dump({"messages": messages}, f)

if __name__ == "__main__":
    prepare_data()
