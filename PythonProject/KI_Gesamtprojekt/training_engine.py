"""
Training Engine
Speichert und nutzt Trainingsdaten für KI-Evolution
"""


class TrainingEngine:
    """
    Speichert Benutzerwechselwirkungen für langfristiges Lernen
    """

    def __init__(self, db):
        self.db = db

    def store_interaction(self, user_id, input_text, response, module, tone):
        """Store user-AI interaction for training"""

        from ..models.training_data import TrainingData

        training_data = TrainingData(
            user_id=user_id,
            input_text=input_text,
            response_text=response,
            module=module,
            tone_applied=tone
        )

        self.db.session.add(training_data)
        self.db.session.commit()

        return {
            "stored": True,
            "training_id": training_data.id
        }

    def retrieve_similar(self, user_id, limit=5):
        """Retrieve similar past interactions"""

        from ..models.training_data import TrainingData

        data = TrainingData.query.filter_by(user_id=user_id) \
            .order_by(TrainingData.id.desc()) \
            .limit(limit) \
            .all()

        return [d.to_dict() for d in data]

    def get_user_patterns(self, user_id):
        """Analyze user interaction patterns"""

        from ..models.training_data import TrainingData

        data = TrainingData.query.filter_by(user_id=user_id).all()

        if not data:
            return {"patterns": "insufficient_data"}

        # Analyze modules used
        modules = {}
        for entry in data:
            mod = entry.module or "unknown"
            modules[mod] = modules.get(mod, 0) + 1

        # Analyze tones
        tones = {}
        for entry in data:
            tone = entry.tone_applied or "neutral"
            tones[tone] = tones.get(tone, 0) + 1

        return {
            "interaction_count": len(data),
            "most_used_modules": sorted(modules.items(), key=lambda x: x[1], reverse=True)[:3],
            "preferred_tones": sorted(tones.items(), key=lambda x: x[1], reverse=True)[:3],
            "data_richness": len(data) / 10  # Relative Metric
        }

    def generate_profile_insights(self, user_id):
        """Generate insights for profile evolution"""

        patterns = self.get_user_patterns(user_id)

        insights = {
            "recommendations": [],
            "patterns": patterns
        }

        # Generate recommendations
        if patterns.get("interaction_count", 0) > 50:
            insights["recommendations"].append("Erhöhtes Persönlichkeits-Level freigeschalten")

        if patterns.get("interaction_count", 0) > 200:
            insights["recommendations"].append("Co-Creator Modus verfügbar")

        return insights


def create_training_engine(db):
    """Factory function"""
    return TrainingEngine(db)
