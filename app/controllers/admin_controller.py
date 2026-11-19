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


# =========================================================
# ÓRDENES
# =========================================================

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


@admin_bp.get("/ordenes/<int:orden_id>")
@login_required
def gestionar_orden(orden_id):
    _validar_administrador()

    try:
        orden = AdministracionService.obtener_orden(
            orden_id
        )
    except ValueError:
        abort(404)

    tecnicos = AdministracionService.listar_tecnicos()

    return render_template(
        "admin/gestionar_orden.html",
        orden=orden,
        tecnicos=tecnicos
    )


@admin_bp.post(
    "/ordenes/<int:orden_id>/tecnico"
)
@login_required
def cambiar_tecnico(orden_id):
    _validar_administrador()

    tecnico_id = request.form.get(
        "tecnico_id",
        type=int
    )

    if tecnico_id is None:
        flash(
            "Debés seleccionar un técnico.",
            "danger"
        )

        return redirect(
            url_for(
                "admin.gestionar_orden",
                orden_id=orden_id
            )
        )

    try:
        AdministracionService.asignar_tecnico(
            orden_id,
            tecnico_id
        )

        flash(
            "El técnico fue asignado correctamente.",
            "success"
        )

    except ValueError as error:
        flash(
            str(error),
            "danger"
        )

    return redirect(
        url_for(
            "admin.gestionar_orden",
            orden_id=orden_id
        )
    )


@admin_bp.post(
    "/ordenes/<int:orden_id>/prioridad"
)
@login_required
def cambiar_prioridad(orden_id):
    _validar_administrador()

    prioridad = request.form.get(
        "prioridad",
        ""
    )

    try:
        AdministracionService.cambiar_prioridad(
            orden_id,
            prioridad
        )

        flash(
            "La prioridad se actualizó correctamente.",
            "success"
        )

    except ValueError as error:
        flash(
            str(error),
            "danger"
        )

    return redirect(
        url_for(
            "admin.gestionar_orden",
            orden_id=orden_id
        )
    )


# =========================================================
# EQUIPOS
# =========================================================

@admin_bp.get("/equipos")
@login_required
def equipos():
    _validar_administrador()

    lista_equipos = AdministracionService.listar_equipos()

    return render_template(
        "admin/equipos.html",
        equipos=lista_equipos
    )

@admin_bp.route(
    "/equipos/nuevo",
    methods=["GET", "POST"]
)
@login_required
def nuevo_equipo():
    _validar_administrador()

    clientes = AdministracionService.listar_clientes()

    if request.method == "POST":

        cliente_id = request.form.get(
            "cliente_id",
            type=int
        )

        tipo = request.form.get(
            "tipo",
            ""
        )

        marca = request.form.get(
            "marca",
            ""
        )

        modelo = request.form.get(
            "modelo",
            ""
        )

        numero_serie = request.form.get(
            "numero_serie",
            ""
        )

        if cliente_id is None:
            flash(
                "Debés seleccionar un cliente.",
                "danger"
            )

            return render_template(
                "admin/nuevo_equipo.html",
                clientes=clientes
            )

        try:
            equipo = AdministracionService.registrar_equipo(
                cliente_id=cliente_id,
                tipo=tipo,
                marca=marca,
                modelo=modelo,
                numero_serie=numero_serie
            )

            flash(
                f"El equipo {equipo.marca} "
                f"{equipo.modelo} se registró correctamente.",
                "success"
            )

            return redirect(
                url_for("admin.equipos")
            )

        except ValueError as error:
            flash(
                str(error),
                "danger"
            )

    return render_template(
        "admin/nuevo_equipo.html",
        clientes=clientes
    )

# =========================================================
# CLIENTES
# =========================================================

@admin_bp.get("/clientes")
@login_required
def clientes():
    _validar_administrador()

    lista_clientes = AdministracionService.listar_clientes()

    return render_template(
        "admin/clientes.html",
        clientes=lista_clientes
    )


@admin_bp.route(
    "/clientes/nuevo",
    methods=["GET", "POST"]
)
@login_required
def nuevo_cliente():
    _validar_administrador()

    if request.method == "POST":

        nombre = request.form.get(
            "nombre",
            ""
        )

        apellido = request.form.get(
            "apellido",
            ""
        )

        email = request.form.get(
            "email",
            ""
        )

        password = request.form.get(
            "password",
            ""
        )

        try:
            cliente = AdministracionService.registrar_cliente(
                nombre=nombre,
                apellido=apellido,
                email=email,
                password=password
            )

            flash(
                f"El cliente {cliente.nombre} "
                f"{cliente.apellido} se registró correctamente.",
                "success"
            )

            return redirect(
                url_for("admin.clientes")
            )

        except ValueError as error:
            flash(
                str(error),
                "danger"
            )

    return render_template(
        "admin/nuevo_cliente.html"
    )


# =========================================================
# TÉCNICOS
# =========================================================

@admin_bp.route(
    "/tecnicos/nuevo",
    methods=["GET", "POST"]
)
@login_required
def nuevo_tecnico():
    _validar_administrador()

    if request.method == "POST":

        nombre = request.form.get(
            "nombre",
            ""
        )

        apellido = request.form.get(
            "apellido",
            ""
        )

        email = request.form.get(
            "email",
            ""
        )

        password = request.form.get(
            "password",
            ""
        )

        try:
            tecnico = AdministracionService.registrar_tecnico(
                nombre=nombre,
                apellido=apellido,
                email=email,
                password=password
            )

            flash(
                f"El técnico {tecnico.nombre} "
                f"{tecnico.apellido} se registró correctamente.",
                "success"
            )

            return redirect(
                url_for("admin.tecnicos")
            )

        except ValueError as error:
            flash(
                str(error),
                "danger"
            )

    return render_template(
        "admin/nuevo_tecnico.html"
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