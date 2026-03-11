"""
Personality Engine
Verwaltet Benutzer-Persönlichkeitsentwicklung und Evolution
"""


class PersonalityEngine:
    EVOLUTION_LEVELS = {
        1: {"name": "Initiate", "description": "Grundlegende KI-Interaktion"},
        2: {"name": "Explorer", "description": "Erkundung von Möglichkeiten"},
        3: {"name": "Creator", "description": "Eigene Inhalte erschaffen"},
        4: {"name": "Master", "description": "Erweiterte Kontrolle"},
        5: {"name": "Architect", "description": "Systeme designen"},
        6: {"name": "Philosopher", "description": "Tiefe verstehen"},
        7: {"name": "Visionary", "description": "Neue Welten schaffen"},
        8: {"name": "Sovereign", "description": "Volle Autonomie"},
        9: {"name": "Ascended", "description": "Meta-Bewusstsein"},
        10: {"name": "Quantum", "description": "Universelle Integration"}
    }

    def __init__(self, profile):
        self.profile = profile

    def update_interaction(self, interaction_count, success=True):
        """Update profile based on interaction"""

        profile_updated = False

        # Evolution based on interactions
        new_level = self._calculate_level(interaction_count)
        if new_level > self.profile.get("level", 1):
            self.profile["level"] = new_level
            profile_updated = True

        # Depth increases
        if interaction_count > 50:
            self.profile["depth"] = "erweitert"
        if interaction_count > 200:
            self.profile["depth"] = "profund"
        if interaction_count > 1000:
            self.profile["depth"] = "universal"

        # Mode adjustments
        if interaction_count > 100 and self.profile.get("mode") == "assistant":
            self.profile["mode"] = "co_creator"
            profile_updated = True

        if interaction_count > 500 and self.profile.get("mode") != "autonomous":
            self.profile["mode"] = "autonomous_partner"
            profile_updated = True

        return {
            "profile": self.profile,
            "updated": profile_updated,
            "level_info": self.EVOLUTION_LEVELS.get(self.profile["level"], {})
        }

    def _calculate_level(self, interaction_count):
        """Calculate evolution level based on interactions"""

        if interaction_count < 10:
            return 1
        elif interaction_count < 50:
            return 2
        elif interaction_count < 150:
            return 3
        elif interaction_count < 400:
            return 4
        elif interaction_count < 900:
            return 5
        elif interaction_count < 1800:
            return 6
        elif interaction_count < 3500:
            return 7
        elif interaction_count < 6500:
            return 8
        elif interaction_count < 12000:
            return 9
        else:
            return 10

    def adapt_personality(self, training_data):
        """Adapt personality based on accumulated training data"""

        if not training_data:
            return self.profile

        # Analyze preferred patterns
        tones = [d.get("tone") for d in training_data]
        genres = [d.get("genre") for d in training_data if d.get("genre")]

        # Update preferred tone (majority)
        if tones:
            most_common = max(set(tones), key=tones.count)
            self.profile["tone"] = most_common

        # Update preferred genre
        if genres:
            most_common = max(set(genres), key=genres.count)
            self.profile["preferred_genre"] = most_common

        return self.profile

    def get_evolution_status(self):
        """Get current evolution status"""
        level = self.profile.get("level", 1)
        return {
            "level": level,
            "name": self.EVOLUTION_LEVELS[level]["name"],
            "description": self.EVOLUTION_LEVELS[level]["description"],
            "profile": self.profile
        }


def create_personality_engine(profile):
    """Factory function"""
    return PersonalityEngine(profile)
