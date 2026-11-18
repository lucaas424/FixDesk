from flask import Blueprint, abort, render_template
from flask_login import current_user, login_required

from app.models import RolUsuario
from app.services import AdministracionService


admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)


def _validar_administrador():
    if current_user.rol != RolUsuario.ADMINISTRADOR:
        abort(403)


@admin_bp.get("/ordenes")
@login_required
def ordenes():
    _validar_administrador()

    lista_ordenes = AdministracionService.listar_ordenes()

    return render_template(
        "admin/ordenes.html",
        ordenes=lista_ordenes
    )


@admin_bp.get("/equipos")
@login_required
def equipos():
    _validar_administrador()

    lista_equipos = AdministracionService.listar_equipos()

    return render_template(
        "admin/equipos.html",
        equipos=lista_equipos
    )


@admin_bp.get("/clientes")
@login_required
def clientes():
    _validar_administrador()

    lista_clientes = AdministracionService.listar_clientes()

    return render_template(
        "admin/clientes.html",
        clientes=lista_clientes
    )


@admin_bp.get("/tecnicos")
@login_required
def tecnicos():
    _validar_administrador()

    lista_tecnicos = AdministracionService.listar_tecnicos()

    return render_template(
        "admin/tecnicos.html",
        tecnicos=lista_tecnicos
    )