import random

AGENTS = {
    "Ate Rea": "Urspiritueller Erzähler des Lichtreichs",
    "Quantum Sage": "analysiert Quantenlogik",
    "Wonder Architect": "baut Welten und Simulationen",
    "Code Monk": "schreibt und optimiert Code",
    "Shadow Mirror": "analysiert Fehler und Dunkelheit",
    "Light Healer": "transformiert Ideen in Heilmodelle",
    "AI Engineer": "Systemoptimierung",
    "Dream Voice": "träumerische Texte",
    "Reality Parser": "analytische Realitätsschicht",
    "Core Observer": "neutraler KI-Kern"
}

def get_agent_response(agent, prompt):
    styles = [
        "interpretiert",
        "transformiert",
        "analysiert",
        "übersetzt",
        "rekonstruiert"
    ]

    return f"{agent} {random.choice(styles)}: {prompt}"