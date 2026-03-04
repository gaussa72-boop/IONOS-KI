
import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

memory_store = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    memory_store.append({"role": "user", "content": user_message})
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=memory_store
    )
    reply = response.choices[0].message.content
    memory_store.append({"role": "assistant", "content": reply})
    return jsonify({"reply": reply})

if __name__ == "__main__":
    if __name__ == "__main__":
        import os

        port = int(os.environ.get("PORT", 5000))
        app.run(host="0.0.0.0", port=port)
