"""
Game Creator Routes
Game Generation und Management
"""

import os

from flask import Blueprint, request, jsonify, send_file
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..core.game_generator_engine import create_game_generator
from ..database import db
from ..models.generated_game import GeneratedGame
from ..models.user import User

game_bp = Blueprint("game", __name__, url_prefix="/api/game")

game_generator = create_game_generator()


@game_bp.route("/create", methods=["POST"])
@jwt_required()
def create_game():
    """Create new game from idea"""
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        if not user:
            return jsonify({"error": "User not found"}), 404

        data = request.get_json()
        idea = data.get("idea", "Unknown Game")
        genre = data.get("genre", "puzzle")

        # Generate game
        game_info = game_generator.generate_game(user_id, idea, genre)

        # Store in database
        game = GeneratedGame(
            user_id=user_id,
            game_id=game_info["game_id"],
            idea=idea,
            genre=genre,
            game_type="html",
            file_path=game_info["filepath"],
            description=f"Generated from idea: {idea}"
        )

        db.session.add(game)
        db.session.commit()

        return jsonify({
            "success": True,
            "game": game.to_dict(),
            "url": game_info["url"]
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@game_bp.route("/list", methods=["GET"])
@jwt_required()
def list_games():
    """List user's games"""
    try:
        user_id = get_jwt_identity()

        games = GeneratedGame.query.filter_by(user_id=user_id).all()

        return jsonify({
            "games": [g.to_dict() for g in games],
            "total": len(games)
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@game_bp.route("/<game_id>", methods=["GET"])
@jwt_required()
def get_game(game_id):
    """Get game details"""
    try:
        user_id = get_jwt_identity()

        game = GeneratedGame.query.filter_by(
            game_id=game_id,
            user_id=user_id
        ).first()

        if not game:
            return jsonify({"error": "Game not found"}), 404

        return jsonify({
            "game": game.to_dict()
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@game_bp.route("/<game_id>/play", methods=["POST"])
@jwt_required()
def play_game(game_id):
    """Record game play"""
    try:
        user_id = get_jwt_identity()

        game = GeneratedGame.query.filter_by(
            game_id=game_id,
            user_id=user_id
        ).first()

        if not game:
            return jsonify({"error": "Game not found"}), 404

        # Increment play count
        game.plays += 1

        # Record rating if provided
        data = request.get_json()
        if "rating" in data:
            game.rating = data["rating"]

        db.session.commit()

        return jsonify({
            "success": True,
            "game": game.to_dict()
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@game_bp.route("/file/<filename>", methods=["GET"])
def get_game_file(filename):
    """Download game file"""
    try:
        filepath = os.path.join(game_generator.GAMES_DIR, filename)

        if not os.path.exists(filepath):
            return jsonify({"error": "File not found"}), 404

        with open(filepath, 'r') as f:
            content = f.read()

        return content, 200, {'Content-Type': 'text/html'}

    except Exception as e:
        return jsonify({"error": str(e)}), 500
