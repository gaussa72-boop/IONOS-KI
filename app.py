from flask import Flask, request, jsonify
from core.brain import GalacticBrain

app = Flask(__name__)
brain = GalacticBrain()

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    prompt = data["prompt"]

    result = brain.think(prompt)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)