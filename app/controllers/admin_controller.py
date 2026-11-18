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


@admin_bp.route(
    "/ordenes/nueva",
    methods=["GET", "POST"]
)
@login_required
def nueva_orden():
    _validar_administrador()

    equipos = AdministracionService.listar_equipos()
    tecnicos = AdministracionService.listar_tecnicos()

    if request.method == "POST":

        equipo_id = request.form.get(
            "equipo_id",
            type=int
        )

        tecnico_id = request.form.get(
            "tecnico_id",
            type=int
        )

        problema_reportado = request.form.get(
            "problema_reportado",
            ""
        )

        prioridad = request.form.get(
            "prioridad",
            "NORMAL"
        )

        observaciones = request.form.get(
            "observaciones",
            ""
        )

        try:
            orden = AdministracionService.crear_orden(
                equipo_id=equipo_id,
                tecnico_id=tecnico_id,
                problema_reportado=problema_reportado,
                prioridad=prioridad,
                observaciones=observaciones
            )

            flash(
                f"La orden #{orden.id} se creó correctamente.",
                "success"
            )

            return redirect(
                url_for("admin.ordenes")
            )

        except ValueError as error:
            flash(
                str(error),
                "danger"
            )

    return render_template(
        "admin/nueva_orden.html",
        equipos=equipos,
        tecnicos=tecnicos
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