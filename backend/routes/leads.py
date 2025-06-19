from flask import Blueprint, jsonify, request
from utils.jwt import jwt_required
from utils.db import SessionLocal
from utils.models import WAFunnel, AgentWAFunnelAssignment
from sqlalchemy import func

leads_blueprint = Blueprint('leads', __name__)


@leads_blueprint.route('/leads/all', methods=['GET'])
@jwt_required
def get_all_leads():
    db = SessionLocal()

    try:
        leads = db.query(WAFunnel).all()
        return jsonify([lead.as_dict() for lead in leads])
    finally:
        db.close()


@leads_blueprint.route('/leads/summary', methods=['GET'])
@jwt_required
def leads_summary():
    db = SessionLocal()
    try:
        total = db.query(func.count(WAFunnel.id)).scalar()
        stage1 = db.query(func.count()).filter(WAFunnel.stage == 1).scalar()
        stage2 = db.query(func.count()).filter(WAFunnel.stage == 2).scalar()
        stage3 = db.query(func.count()).filter(WAFunnel.stage == 3).scalar()
        stage4 = db.query(func.count()).filter(WAFunnel.stage == 4).scalar()
        return jsonify({
            "totalLeads": total,
            "stage1": stage1,
            "stage2": stage2,
            "stage3": stage3,
            "stage4": stage4
        })
    finally:
        db.close()


@leads_blueprint.route('/leads/agents', methods=['GET'])
@jwt_required
def get_agent_leads():
    db = SessionLocal()
    try:
        assignments = db.query(AgentWAFunnelAssignment).order_by(AgentWAFunnelAssignment.id).all()
        return jsonify({'success': True, 'data': [a.as_dict() for a in assignments]})
    finally:
        db.close()
