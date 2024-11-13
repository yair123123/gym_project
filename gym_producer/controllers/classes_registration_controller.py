from flask import Blueprint, request, blueprints, jsonify

from producers.classes_registration_produce import produce_classes_registration

classes_registration_blueprint = blueprints.Blueprint("classes", __name__)


@classes_registration_blueprint.route('/registration', methods=['POST'])
def registration_classes_and_member():
    details = request.json
    produce_classes_registration(details)
    return jsonify({"message": "New registration created successfully"}), 201
