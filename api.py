from flask import Flask, jsonify, request
from inference import infer

app = Flask(__name__)

model = infer()

@app.route('/predict/', methods=['GET', 'POST'])
def predict():

    content = request.get_json()
    text = content["text"]
    candidate_labels = content["candidate_labels"]

    prediction = model.predict(
        text=text,
        candidate_lab=candidate_labels
    )

    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

