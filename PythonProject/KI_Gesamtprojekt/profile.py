"""
Profile Routes
User Profile Management
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..models.user import User
from ..core.training_engine import create_training_engine
from ..core.personality_engine import create_personality_engine
from ..database import db

profile_bp = Blueprint("profile", __name__, url_prefix="/api/profile")

training_engine = create_training_engine(db)


@profile_bp.route("/", methods=["GET"])
@jwt_required()
def get_profile():
    """Get user profile"""
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        if not user or not user.profile:
            return jsonify({"error": "Profile not found"}), 404

        # Get training insights
        insights = training_engine.generate_profile_insights(user_id)

        return jsonify({
            "profile": user.profile.to_dict(),
            "insights": insights
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@profile_bp.route("/update", methods=["PUT"])
@jwt_required()
def update_profile():
    """Update user profile"""
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        if not user or not user.profile:
            return jsonify({"error": "Profile not found"}), 404

        data = request.get_json()

        # Update fields
        if "tone" in data:
            user.profile.tone = data["tone"]
        if "depth" in data:
            user.profile.depth = data["depth"]
        if "style" in data:
            user.profile.style = data["style"]
        if "mode" in data:
            user.profile.mode = data["mode"]

        db.session.commit()

        return jsonify({
            "success": True,
            "profile": user.profile.to_dict()
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@profile_bp.route("/evolution", methods=["GET"])
@jwt_required()
def get_evolution():
    """Get evolution status"""
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        if not user or not user.profile:
            return jsonify({"error": "Profile not found"}), 404

        # Create personality engine
        personality_engine = create_personality_engine(user.profile.to_dict())

        # Get evolution status
        evolution = personality_engine.get_evolution_status()

        return jsonify({
            "evolution": evolution,
            "interaction_count": user.profile.interaction_count,
            "next_level_at": (user.profile.level + 1) * 100  # Example formula
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@profile_bp.route("/training-history", methods=["GET"])
@jwt_required()
def get_training_history():
    """Get training history"""
    try:
        user_id = get_jwt_identity()
        limit = request.args.get("limit", 10, type=int)

        history = training_engine.retrieve_similar(user_id, limit)
        patterns = training_engine.get_user_patterns(user_id)

        return jsonify({
            "history": history,
            "patterns": patterns,
            "total": len(history)
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@profile_bp.route("/stats", methods=["GET"])
@jwt_required()
def get_stats():
    """Get profile statistics"""
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        if not user:
            return jsonify({"error": "User not found"}), 404

        # Get game count
        game_count = len(user.generated_games) if user.generated_games else 0
        training_count = len(user.training_data) if user.training_data else 0

        return jsonify({
            "user": user.username,
            "games_created": game_count,
            "interactions": training_count,
            "level": user.profile.level if user.profile else 1,
            "member_since": user.created_at.isoformat()
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
