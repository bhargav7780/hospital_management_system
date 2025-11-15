from flask import Blueprint, render_template, request, redirect, url_for
from models.patient_model import add_patient, get_all_patients
from utils.auth_decorator import login_required

patient_bp = Blueprint("patient", __name__)

@patient_bp.route("/add", methods=["GET", "POST"])
@login_required
def add_patient_route():
    if request.method == "POST":
        data = {
            "name": request.form.get("name"),
            "age": int(request.form.get("age") or 0),
            "gender": request.form.get("gender"),
            "notes": request.form.get("notes")
        }
        add_patient(data)
        return redirect(url_for("patient.view_patients"))
    return render_template("add_patient.html")

@patient_bp.route("/view")
@login_required
def view_patients():
    patients = get_all_patients()
    return render_template("view_patients.html", patients=patients)
