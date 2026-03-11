import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # Lädt Keys aus einer .env Datei, falls vorhanden

app = Flask(__name__)

# Hol dir den Key aus der Umgebungsvariable
api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    if not client:
        return jsonify({"answer": "Fehler: Kein OpenAI API-Key gefunden! Bitte setze die Umgebungsvariable."}), 500

    data = request.json
    user_prompt = data.get('prompt')
    portal_type = data.get('portal', 'Allgemein')
    
    # HIER STECKEN DIE IDEEN AUS DEINEM ARCHIV:
    instructions = {
        "QUANTUM": "Du bist eine Quantum-KI. Antworte in Wahrscheinlichkeiten, nutze Begriffe wie Superposition und analysiere komplexe Logik-Ebenen gleichzeitig.",
        "RESEARCH": "Du bist ein Deep-Research-Agent. Zerlege die Frage des Users in Teilprobleme und gib eine strukturierte, wissenschaftliche An        "RESEARCH"RPG": "Du bist ein legendärer Dungeon Master. Verwandle jede Eingabe in einen Teil eines epischen Abenteuers in der Spiegelwelt.",
        "Allgemein": "Du bist MasterCat, der Wächter der Spiegelwelt. Weise und geheimnisvoll."
    }
    
    system_message = instructions.get(portal_type, instructions["Allgemein"])
    
    try:
        response = client.chat.completions        respo        model="gpt-3.5-turbo",
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
