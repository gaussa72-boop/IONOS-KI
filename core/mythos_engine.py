import random
from agents.archetypes import ARCHETYPES

def summon_agent(prompt):
    name = random.choice(list(ARCHETYPES.keys()))
    agent = ARCHETYPES[name]

    return f"""
✨ MYTHOS CORE ACTIVATED ✨

Agent: {name}
Form: {agent['form']}

Interpretation:
{agent['ritual']}

Verarbeitung:
{prompt}

Resultat:
{agent['style']} Transformation aktiv.
"""