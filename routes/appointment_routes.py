from flask import Blueprint, render_template, request, redirect, url_for
from models.appointment_model import book_appointment, get_appointments
from utils.auth_decorator import login_required

appointment_bp = Blueprint("appointment", __name__)

@appointment_bp.route("/book", methods=["GET", "POST"])
@login_required
def appointment_page():
    if request.method == "POST":
        data = {
            "patient_name": request.form.get("patient_name"),
            "doctor_name": request.form.get("doctor_name"),
            "date": request.form.get("date"),
            "reason": request.form.get("reason"),
        }
        book_appointment(data)
        return redirect(url_for("appointment.appointment_page"))
    appointments = get_appointments()
    return render_template("appointment.html", appointments=appointments)
