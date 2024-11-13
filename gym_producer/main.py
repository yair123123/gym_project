from flask import Flask

from controllers.classes_registration_controller import classes_registration_blueprint
from controllers.equipment_audit_controller import equipment_audit_blueprint
from controllers.feedback_trainers_controller import feedback_trainers_blueprint
from controllers.membership_new_controller import membership_new_blueprint

app = Flask(__name__)

app.register_blueprint(equipment_audit_blueprint, url_prefix="/api/equipment_audit")

app.register_blueprint(classes_registration_blueprint, url_prefix="/api/classes")

app.register_blueprint(feedback_trainers_blueprint, url_prefix="/api/feedback_trainers")

app.register_blueprint(membership_new_blueprint, url_prefix="/api/membership_new")

if __name__ == '__main__':
    app.run(port=5001)
