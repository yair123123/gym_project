from flask import Blueprint, request, blueprints, jsonify

from producers.feedback_trainers_produce import produce_feedback_trainers

feedback_trainers_blueprint = blueprints.Blueprint("feedback_trainers", __name__)

@feedback_trainers_blueprint.route('/', methods=['POST'])
def post_feedback():
    details = request.json
    produce_feedback_trainers(details)
    return jsonify({'Message':"OK"})