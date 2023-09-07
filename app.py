from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

openai.api_key = config["OPENAI_API_KEY"]


@app.route('/train', methods=['POST'])
def train_model():
    with open(request.form['file_path'], 'rb') as f:
        response = openai.File.create(file=f, purpose="fine-tune")
        file_id = response.id
    
    model_response = openai.FineTuning.create(
      model="gpt-3.5-turbo",
      training_file=file_id
    )
    
    return jsonify({"model_id": model_response.id})

@app.route('/ask', methods=['POST'])
def ask_question():
    model_id = request.form['model_id']
    question = request.form['question']

    response = openai.Completion.create(
        model=model_id,
        prompt=question,
        max_tokens=150
    )
    return jsonify(response.choices[0].text.strip())

if __name__ == '__main__':
    app.run(debug=True)
