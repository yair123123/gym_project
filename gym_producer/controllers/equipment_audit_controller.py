from flask import request, blueprints, jsonify

from producers.equipment_audit_produce import produce_equipment_audit

equipment_audit_blueprint = blueprints.Blueprint("equipment_audit", __name__)

@equipment_audit_blueprint.route('/', methods=['POST'])
def details_equipment_audit():
    details = request.json
    produce_equipment_audit(details)
    return jsonify({'Message': "OK"})