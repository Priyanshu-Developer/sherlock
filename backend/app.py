#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Flask app to execute a stored procedure daily at 8:40 PM and provide lead data APIs.
"""

from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
from flask_cors import CORS
from datetime import datetime
import pymssql
import os

# === Load environment variables ===
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# === Database configuration ===
DB_CONFIG = {
    'server': os.getenv('DB_SERVER'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_DATABASE'),
    'port': int(os.getenv('DB_PORT', 1433)) 
}


def run_stored_procedure():
    """
    Executes the stored procedure to assign leads to agents.
    """
    try:
        print(f"[{datetime.now()}] Running stored procedure...")

        conn = pymssql.connect(
            server=DB_CONFIG['server'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database'],
            port=DB_CONFIG['port']
        )
        cursor = conn.cursor()
        cursor.callproc('sp_assign_wafunnel_to_agents')
        conn.commit()
        cursor.close()
        conn.close()

        print("✅ Stored procedure executed successfully.")
        return True

    except Exception as e:
        print("❌ Failed to execute stored procedure:", e)
        return False


def schedule_daily_task():
    """
    Schedules the stored procedure to run every day at 8:40 PM.
    """
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        func=run_stored_procedure,
        trigger='cron',
        hour=20,
        minute=40,
        id='daily_wafunnel_assignment'
    )
    scheduler.start()
    print("🕒 Scheduler started. Procedure will run every day at 8:40 PM.")


@app.route('/run-now', methods=['GET'])
def run_now():
    success = run_stored_procedure()
    if success:
        return jsonify({"status": "success", "message": "Stored procedure executed successfully."}), 200
    else:
        return jsonify({"status": "failure", "message": "Failed to execute stored procedure."}), 500


@app.route('/leads/summary', methods=['GET'])
def leads_summary():
    try:
        conn = pymssql.connect(
            server=DB_CONFIG['server'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database'],
            port=DB_CONFIG['port']
        )
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                COUNT(*) as total,
                SUM(CASE WHEN stage = 1 THEN 1 ELSE 0 END) as stage1,
                SUM(CASE WHEN stage = 2 THEN 1 ELSE 0 END) as stage2,
                SUM(CASE WHEN stage = 3 THEN 1 ELSE 0 END) as stage3,
                SUM(CASE WHEN stage = 4 THEN 1 ELSE 0 END) as stage4
            FROM Sherlocksauto.Wafunnel
        """)
        row = cursor.fetchone()
        cursor.close()
        conn.close()

        return jsonify({
            "totalLeads": row[0],
            "stage1": row[1],
            "stage2": row[2],
            "stage3": row[3],
            "stage4": row[4]
        }), 200

    except Exception as e:
        print("❌ Error fetching lead summary:", e)
        return jsonify({"status": "failure", "message": str(e)}), 500


@app.route('/leads/all', methods=['GET'])
def get_all_leads():
    try:
        conn = pymssql.connect(
            server=DB_CONFIG['server'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database'],
            port=DB_CONFIG['port']
        )
        cursor = conn.cursor(as_dict=True)
        cursor.execute("""
            SELECT id, Number AS phoneNo, Stage AS stage, Date AS date
            FROM Sherlocksauto.Wafunnel
        """)
        rows = cursor.fetchall()

        for row in rows:
            try:
                row['date'] = datetime.strptime(str(row['date']), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
            except Exception:
                row['date'] = str(row['date'])[:10]

        cursor.close()
        conn.close()
        return jsonify(rows), 200

    except Exception as e:
        print("❌ Error fetching leads:", e)
        return jsonify({"status": "failure", "message": str(e)}), 500


@app.route('/leads/agents', methods=['GET'])
def get_agent_leads():
    try:
        conn = pymssql.connect(
            server=DB_CONFIG['server'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database'],
            port=DB_CONFIG['port']
        )
        cursor = conn.cursor(as_dict=True)
        cursor.execute("SELECT id, agent, Number as phoneNo FROM agent_wafunnel_assignment ORDER BY id ASC")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify({'success': True, 'data': data}), 200
    except Exception as e:
        print("❌ Error fetching agent leads:", e)
        return jsonify({'success': False, 'error': str(e)}), 500


if __name__ == '__main__':
    schedule_daily_task()
    app.run(debug=False, use_reloader=False)
