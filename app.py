from flask import Flask, render_template
from config import SECRET_KEY
from routes.auth_routes import auth_bp
from routes.patient_routes import patient_bp
from routes.doctor_routes import doctor_bp
from routes.appointment_routes import appointment_bp

app = Flask(__name__, static_folder="static", template_folder="templates")
app.secret_key = SECRET_KEY or "dev-secret-key"

# register blueprints
app.register_blueprint(auth_bp, url_prefix="")
app.register_blueprint(patient_bp, url_prefix="/patient")
app.register_blueprint(doctor_bp, url_prefix="/doctor")
app.register_blueprint(appointment_bp, url_prefix="/appointment")

@app.route("/")
def root():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
