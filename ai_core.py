import random

def ai_response(msg):

    if "code" in msg.lower():
        return "Ich generiere neuen Code."

    if "roman" in msg.lower():
        return "Ich schreibe deine urspirituelle Geschichte weiter."

    if "social" in msg.lower():
        return "Social Media Analyse gestartet."

    responses = [
        "Quantenkern aktiv.",
        "Lebensblume berechnet Möglichkeiten.",
        "Multiversum Antwort generiert.",
        "KI lernt aus deiner Anfrage."
    ]

    return random.choice(responses)