from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'YOUR_OPENAI_API_KEY'
headers = {
    'Authorization': f'Bearer {API_KEY}'
}

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json['question']
    
    data = {
        "model": "ft:gpt-3.5-turbo:YOUR_ORG_ID",
        "messages": [
            {
                "role": "system",
                "content": "You are a chatbot trained on USAFA documents."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    answer = response.json()['choices'][0]['message']['content']

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
