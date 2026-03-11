import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    user_prompt = data.get('prompt')
    portal_type = data.get('portal', 'Allgemein')
    
    instructions = {
        "RPG_QUEST": "Du bist ein Dungeon Master.",
        "SPACE_BATTLE": "Du bist ein Flottenkommandant.",
        "Allgemein": "Du bist MasterCat."
    }
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": instructions.get(portal_type, instructions["Allgemein"])},
                {"role": "user", "content": user_prompt}
            ]
        )
        return jsonify({"answer": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"answer": f"Fehler: {str(e)}"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
