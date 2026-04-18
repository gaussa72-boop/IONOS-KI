import random

class GalacticBrain:
    def __init__(self):
        self.memory = []

    def think(self, prompt):
        self.memory.append(prompt)

        responses = [
            "Lichtstruktur erkannt in deiner Idee.",
            "Urspirit moduliert Realität als Symbolsystem.",
            "Quantum-Agenten aktivieren Musteranalyse.",
            "Wonderland Simulation erzeugt neue Weltlogik.",
        ]

        return random.choice(responses) + f" | Input: {prompt}"