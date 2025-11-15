from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from models.user_model import create_user, find_by_username
import bcrypt

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password", "").encode()
        user = find_by_username(username)
        if user and bcrypt.checkpw(password, user["password"]):
            session["user"] = {"id": str(user["_id"]), "username": user["username"], "role": user.get("role","receptionist")}
            return redirect(url_for("auth.dashboard"))
        flash("Invalid credentials", "danger")
    return render_template("login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password", "").encode()
        role = request.form.get("role", "receptionist")
        if find_by_username(username):
            flash("User exists", "warning")
            return redirect(url_for("auth.register"))
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        create_user(username, hashed, role)
        flash("Account created. Please login.", "success")
        return redirect(url_for("auth.login"))
    return render_template("register.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))

# simple dashboard route (not a blueprint)
@auth_bp.route("/dashboard")
def dashboard():
    user = session.get("user")
    if not user:
        return redirect(url_for("auth.login"))
    return render_template("dashboard.html", user=user["username"], role=user["role"])
