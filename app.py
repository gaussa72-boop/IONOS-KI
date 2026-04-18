from flask import Flask, request, jsonify
from core.brain import GalacticBrain
from agents.agents import get_agent_response
from urspirit.poetry import generate_poem
from engine.game import World

app = Flask(__name__)

brain = GalacticBrain()
world = World()

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    prompt = data["prompt"]

    return jsonify({
        "brain": brain.think(prompt),
        "poem": generate_poem(prompt),
        "world": world.evolve(prompt),
        "agent": get_agent_response("Quantum Sage", prompt)
    })

if __name__ == "__main__":
    app.run(debug=True)