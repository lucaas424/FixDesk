from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)

from app.services import AuthService


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.inicio"))

    if request.method == "POST":
        email = request.form.get("email", "")
        password = request.form.get("password", "")

        usuario = AuthService.autenticar(
            email,
            password
        )

        if usuario is None:
            flash(
                "El correo electrónico o la contraseña son incorrectos.",
                "danger"
            )

            return render_template(
                "auth/login.html",
                email=email
            )

        login_user(usuario)

        return redirect(url_for("main.inicio"))

    return render_template("auth/login.html")


@auth_bp.post("/logout")
@login_required
def logout():
    logout_user()

    flash(
        "La sesión se cerró correctamente.",
        "success"
    )

    return redirect(url_for("auth.login"))