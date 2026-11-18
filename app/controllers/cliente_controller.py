from flask import Blueprint, abort, render_template
from flask_login import current_user, login_required

from app.models import RolUsuario
from app.services import EquipoService, OrdenService


cliente_bp = Blueprint(
    "cliente",
    __name__,
    url_prefix="/portal"
)


def _validar_cliente():
    if current_user.rol != RolUsuario.CLIENTE:
        abort(403)


@cliente_bp.get("/reparaciones")
@login_required
def reparaciones():
    _validar_cliente()

    ordenes = OrdenService.listar_ordenes_cliente(
        current_user.id
    )

    return render_template(
        "cliente/reparaciones.html",
        ordenes=ordenes
    )


@cliente_bp.get("/equipos")
@login_required
def equipos():
    _validar_cliente()

    equipos_cliente = (
        EquipoService.listar_equipos_cliente(
            current_user.id
        )
    )

    return render_template(
        "cliente/equipos.html",
        equipos=equipos_cliente
    )