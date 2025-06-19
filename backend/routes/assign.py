from flask import Blueprint, jsonify
from utils.jwt import jwt_required
from utils.scheduler import run_stored_procedure

procedure_blueprint = Blueprint('procedure', __name__)

@procedure_blueprint.route('/assign', methods=['POST'])
@jwt_required
def assign_wafunnel_to_agents():
   
    result = run_stored_procedure()
    if not result:
        return jsonify({"status": "failure", "message": "Stored procedure execution failed."}), 500
    else:
        return jsonify({"status": "success", "message": "Stored procedure executed successfully."}), 200
   