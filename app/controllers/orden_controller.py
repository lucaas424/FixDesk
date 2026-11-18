from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
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

    if current_user.rol == RolUsuario.CLIENTE:
        if orden.equipo.cliente_id != current_user.id:
            abort(403)

        return

    abort(403)


def _obtener_orden_autorizada(orden_id):
    try:
        orden = OrdenService.obtener_orden(orden_id)
    except ValueError:
        abort(404)

    _validar_acceso_orden(orden)

    return orden


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
    orden = _obtener_orden_autorizada(orden_id)

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

    estados_permitidos = (
        OrdenService.TRANSICIONES_VALIDAS.get(
            orden.estado_actual,
            set()
        )
    )

    return render_template(
        "ordenes/detalle.html",
        orden=orden,
        diagnostico=diagnostico,
        tareas=tareas,
        historial=historial,
        estados_permitidos=estados_permitidos,
        RolUsuario=RolUsuario
    )


@orden_bp.post("/<int:orden_id>/estado")
@login_required
def cambiar_estado(orden_id):
    orden = _obtener_orden_autorizada(orden_id)

    if current_user.rol != RolUsuario.TECNICO:
        abort(403)

    nuevo_estado = request.form.get(
        "nuevo_estado",
        ""
    )

    try:
        OrdenService.cambiar_estado(
            orden.id,
            nuevo_estado,
            current_user.id
        )

        flash(
            "El estado de la orden se actualizó correctamente.",
            "success"
        )

    except ValueError as error:
        flash(
            str(error),
            "danger"
        )

    return redirect(
        url_for(
            "orden.detalle",
            orden_id=orden.id
        )
    )


@orden_bp.post("/<int:orden_id>/diagnostico")
@login_required
def registrar_diagnostico(orden_id):
    orden = _obtener_orden_autorizada(orden_id)

    if current_user.rol != RolUsuario.TECNICO:
        abort(403)

    descripcion = request.form.get(
        "descripcion",
        ""
    )

    try:
        DiagnosticoService.registrar_diagnostico(
            orden.id,
            descripcion,
            current_user.id
        )

        flash(
            "El diagnóstico se guardó correctamente.",
            "success"
        )

    except ValueError as error:
        flash(
            str(error),
            "danger"
        )

    return redirect(
        url_for(
            "orden.detalle",
            orden_id=orden.id
        )
    )


@orden_bp.post("/<int:orden_id>/tareas")
@login_required
def registrar_tarea(orden_id):
    orden = _obtener_orden_autorizada(orden_id)

    if current_user.rol != RolUsuario.TECNICO:
        abort(403)

    descripcion = request.form.get(
        "descripcion",
        ""
    )

    try:
        TareaService.registrar_tarea(
            orden.id,
            descripcion,
            current_user.id
        )

        flash(
            "La tarea de reparación se registró correctamente.",
            "success"
        )

    except ValueError as error:
        flash(
            str(error),
            "danger"
        )

    return redirect(
        url_for(
            "orden.detalle",
            orden_id=orden.id
        )
    )