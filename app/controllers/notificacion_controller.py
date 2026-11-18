from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    url_for,
)
from flask_login import current_user, login_required

from app.models import RolUsuario
from app.services import NotificacionService


notificacion_bp = Blueprint(
    "notificacion",
    __name__,
    url_prefix="/notificaciones"
)


def _validar_cliente():
    if current_user.rol != RolUsuario.CLIENTE:
        abort(403)


@notificacion_bp.get("/")
@login_required
def lista():
    _validar_cliente()

    notificaciones = (
        NotificacionService.listar_notificaciones_cliente(
            current_user.id
        )
    )

    no_leidas = [
        notificacion
        for notificacion in notificaciones
        if not notificacion.leida
    ]

    return render_template(
        "notificaciones/lista.html",
        notificaciones=notificaciones,
        cantidad_no_leidas=len(no_leidas)
    )


@notificacion_bp.post("/<int:notificacion_id>/leer")
@login_required
def marcar_leida(notificacion_id):
    _validar_cliente()

    try:
        NotificacionService.marcar_como_leida(
            notificacion_id,
            current_user.id
        )

        flash(
            "La notificación se marcó como leída.",
            "success"
        )

    except ValueError as error:
        flash(
            str(error),
            "danger"
        )

    return redirect(
        url_for("notificacion.lista")
    )