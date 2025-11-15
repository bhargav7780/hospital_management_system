from flask import Blueprint, render_template, request, redirect, url_for
from models.doctor_model import add_doctor, get_all_doctors
from utils.auth_decorator import login_required

doctor_bp = Blueprint("doctor", __name__)

@doctor_bp.route("/add", methods=["GET", "POST"])
@login_required
def add_doctor_route():
    if request.method == "POST":
        data = {
            "name": request.form.get("name"),
            "specialty": request.form.get("specialty"),
            "phone": request.form.get("phone")
        }
        add_doctor(data)
        return redirect(url_for("doctor.view_doctors"))
    return render_template("add_doctor.html")

@doctor_bp.route("/view")
@login_required
def view_doctors():
    doctors = get_all_doctors()
    return render_template("view_doctors.html", doctors=doctors)
