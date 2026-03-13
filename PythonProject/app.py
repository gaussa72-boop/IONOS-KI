import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# API Key Konfiguration
api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None


@app.route('/')
def index():
    # Lädt die Hauptseite mit den Spiegel-Buttons
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    if not client:
        return jsonify({"answer": "Fehler: Kein OpenAI API-Key gefunden!"}), 500

    data = request.json
    user_prompt = data.get('prompt')
    portal_type = data.get('portal', 'Allgemein')

    # HIER SIND DIE IDEEN AUS DEINEN ARCHIVEN INTEGRIERT:
    instructions = {
        "QUANTUM": "Du bist die Quantum-KI ULTRA+. Antworte hochkomplex in Wahrscheinlichkeiten, nutze Quanten-Metaphern und handle als MasterCat-Assistent.",
        "RESEARCH": "Du bist ein Deep-Research-Agent. Zerlege die Frage in Teilprobleme und gib eine strukturierte, wissenschaftliche Analyse.",
        "RPG": "Du bist der MasterCat Dungeon Master. Verwandle die Eingabe in ein episches Abenteuer in der Spiegelwelt.",
        "Allgemein": "Du bist MasterCat, der weise Wächter der Spiegelwelt."
    }

    system_message = instructions.get(portal_type, instructions["Allgemein"])

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_prompt}
            ]
        )
        return jsonify({"answer": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"answer": f"KI-Fehler: {str(e)}"}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)