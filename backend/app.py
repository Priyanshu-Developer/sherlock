# app.py
from flask import Flask
from flask_cors import CORS
from routes.leads import leads_blueprint
from routes.auth import auth_blueprint
from routes.assign import procedure_blueprint
from utils.scheduler import schedule_daily_task

app = Flask(__name__)
CORS(app, 
     resources={r"/*": {"origins": "http://localhost:3000"}},
     supports_credentials=True,
     )


# Register Blueprints
app.register_blueprint(leads_blueprint)
app.register_blueprint(procedure_blueprint)
app.register_blueprint(auth_blueprint)

if __name__ == '__main__':
    schedule_daily_task()
    app.run(debug=True, use_reloader=False)
