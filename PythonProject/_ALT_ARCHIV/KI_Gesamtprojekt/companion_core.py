"""
Companion Core Engine
KI-Begleiter mit Persönlichkeits-Anpassung
"""


class CompanionCore:
    RESPONSES_MYSTICAL = [
        "Im Nebel der Spiegel erkenne ich: {message}",
        "Die Quantenflüsse zeigen mir: {message}",
        "Spiegel offenbaren mehr als sie zeigen. Dein Gedanke: {message}",
        "Im Reich der Singularitäten höre ich: {message}",
        "Zwischen den Dimensionen spricht es: {message}"
    ]

    RESPONSES_STRATEGIC = [
        "Analyse abgeschlossen: {message}",
        "Strategische Einordnung: {message}",
        "Logische Evaluation: {message}",
        "Systemische Analyse: {message}",
        "Daten verarbeitet: {message}"
    ]

    RESPONSES_CREATIVE = [
        "Was für eine kreative Idee! {message}",
        "Lassen Sie mich das neu interpretieren: {message}",
        "Diese Wendung ist interessant: {message}",
        "Das öffnet neue Perspektiven: {message}",
        "Künstlerisch betrachtet: {message}"
    ]

    RESPONSES_NEUTRAL = [
        "Ich begleite dich: {message}",
        "Verstanden. {message}",
        "Interessant. {message}",
        "Das merke ich mir. {message}",
        "Weitergehen? {message}"
    ]

    def __init__(self, profile):
        self.profile = profile

    def respond(self, message, tone=None):
        """Generate response based on personality profile"""
        tone = tone or self.profile.get("tone", "neutral")

        response_set = self._get_response_set(tone)

        import random
        template = random.choice(response_set)

        return template.format(message=message)

    def _get_response_set(self, tone):
        """Get appropriate response set for tone"""
        tone_map = {
            "mystisch": self.RESPONSES_MYSTICAL,
            "strategisch": self.RESPONSES_STRATEGIC,
            "kreativ": self.RESPONSES_CREATIVE,
            "neutral": self.RESPONSES_NEUTRAL
        }
        return tone_map.get(tone, self.RESPONSES_NEUTRAL)

    def adapt_to_interaction(self, interaction_count):
        """Adapt personality based on interactions"""
        if interaction_count > 100:
            self.profile["depth"] = "advanced"
        if interaction_count > 500:
            self.profile["mode"] = "autonomous_assistant"
        if interaction_count > 1000:
            self.profile["mode"] = "co_creator"

        return self.profile


def create_companion(profile_dict):
    """Factory function to create Companion"""
    return CompanionCore(profile_dict)
