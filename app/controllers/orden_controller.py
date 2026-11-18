from flask import Blueprint, abort, render_template
from flask_login import current_user, login_required

from app.models import RolUsuario
from app.repositories import HistorialRepository
from app.services import (
    DiagnosticoService,
    OrdenService,
    TareaService,
)


orden_bp = Blueprint(
    "orden",
    __name__,
    url_prefix="/ordenes"
)


def _validar_acceso_orden(orden):
    if current_user.rol == RolUsuario.ADMINISTRADOR:
        return

    if current_user.rol == RolUsuario.TECNICO:
        if orden.tecnico_id != current_user.id:
            abort(403)

        return

    abort(403)


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


@orden_bp.get("/<int:orden_id>")
@login_required
def detalle(orden_id):
    try:
        orden = OrdenService.obtener_orden(orden_id)
    except ValueError:
        abort(404)

    _validar_acceso_orden(orden)

    diagnostico = (
        DiagnosticoService.obtener_diagnostico_orden(
            orden.id
        )
    )

    tareas = TareaService.listar_tareas_orden(
        orden.id
    )

    historial = HistorialRepository.listar_por_orden(
        orden.id
    )

    return render_template(
        "ordenes/detalle.html",
        orden=orden,
        diagnostico=diagnostico,
        tareas=tareas,
        historial=historial
    )