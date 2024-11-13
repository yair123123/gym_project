from flask import  request, jsonify, blueprints

from producers.membership_new_produce import produce_membership_details

membership_new_blueprint = blueprints.Blueprint("membership_new", __name__)

@membership_new_blueprint.route('/', methods=['POST'])
def create_new_member():
    details = request.json
    produce_membership_details(details)
    return jsonify({"message": "New member created successfully"}), 201
