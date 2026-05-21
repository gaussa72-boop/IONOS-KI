from core.mythos_engine import summon_agent

class GalacticBrain:
    def __init__(self):
        self.memory = []

    def think(self, prompt):
        self.memory.append(prompt)

        mythos = summon_agent(prompt)

        return {
            "raw_input": prompt,
            "mythos_response": mythos,
            "status": "URSPIRIT ACTIVE"
        }