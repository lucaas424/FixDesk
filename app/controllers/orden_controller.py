from flask import Blueprint, abort, render_template
from flask_login import current_user, login_required

from app.models import RolUsuario
from app.services import OrdenService


orden_bp = Blueprint(
    "orden",
    __name__,
    url_prefix="/ordenes"
)


@orden_bp.get("/")
@login_required
def lista():
    if current_user.rol == RolUsuario.TECNICO:
        ordenes = OrdenService.listar_ordenes_tecnico(
            current_user.id
        )

    elif current_user.rol == RolUsuario.ADMINISTRADOR:
        ordenes = OrdenService.listar_ordenes()

    else:
        abort(403)

    return render_template(
        "ordenes/lista.html",
        ordenes=ordenes
    )