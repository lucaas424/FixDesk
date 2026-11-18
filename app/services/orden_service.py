from app.models import (
    OrdenReparacion,
    HistorialEstado,
    PrioridadOrden,
    EstadoOrden,
    RolUsuario,
)
from app.repositories import (
    OrdenRepository,
    EquipoRepository,
    UsuarioRepository,
    HistorialRepository,
)
from app.patterns import (
    NotificacionObserver,
    PrioridadBajaStrategy,
    PrioridadNormalStrategy,
    PrioridadAltaStrategy,
    PrioridadUrgenteStrategy,
)

class OrdenService:

    OBSERVADORES = (
        NotificacionObserver(),
    )
    ESTRATEGIAS_PRIORIDAD = {
        PrioridadOrden.BAJA: PrioridadBajaStrategy(),
        PrioridadOrden.NORMAL: PrioridadNormalStrategy(),
        PrioridadOrden.ALTA: PrioridadAltaStrategy(),
        PrioridadOrden.URGENTE: PrioridadUrgenteStrategy(),
    }

    TRANSICIONES_VALIDAS = {
        EstadoOrden.RECIBIDO: {
            EstadoOrden.EN_DIAGNOSTICO,
            EstadoOrden.CANCELADO,
        },
        EstadoOrden.EN_DIAGNOSTICO: {
            EstadoOrden.EN_REPARACION,
            EstadoOrden.CANCELADO,
        },
        EstadoOrden.EN_REPARACION: {
            EstadoOrden.LISTO_PARA_RETIRAR,
            EstadoOrden.CANCELADO,
        },
        EstadoOrden.LISTO_PARA_RETIRAR: {
            EstadoOrden.FINALIZADO,
            EstadoOrden.CANCELADO,
        },
        EstadoOrden.FINALIZADO: set(),
        EstadoOrden.CANCELADO: set(),
    }

    @staticmethod
    def crear_orden(
        equipo_id,
        tecnico_id,
        problema_reportado,
        prioridad=PrioridadOrden.NORMAL,
        fecha_estimada=None,
        observaciones=None
    ):
        equipo = EquipoRepository.buscar_por_id(equipo_id)

        if equipo is None:
            raise ValueError("El equipo indicado no existe.")

        if not equipo.activo:
            raise ValueError("El equipo indicado está inactivo.")

        tecnico = UsuarioRepository.buscar_por_id(tecnico_id)

        if tecnico is None:
            raise ValueError("El técnico indicado no existe.")

        if tecnico.rol != RolUsuario.TECNICO:
            raise ValueError(
                "El usuario indicado no corresponde a un técnico."
            )

        if not tecnico.activo:
            raise ValueError("El técnico indicado está inactivo.")

        problema_reportado = problema_reportado.strip()

        if not problema_reportado:
            raise ValueError(
                "El problema reportado es obligatorio."
            )

        if isinstance(prioridad, str):
            try:
                prioridad = PrioridadOrden(prioridad)
            except ValueError:
                raise ValueError("La prioridad indicada no es válida.")

        if observaciones is not None:
            observaciones = observaciones.strip()

        orden = OrdenReparacion(
            equipo_id=equipo.id,
            tecnico_id=tecnico.id,
            problema_reportado=problema_reportado,
            prioridad=prioridad,
            estado_actual=EstadoOrden.RECIBIDO,
            fecha_estimada=fecha_estimada,
            observaciones=observaciones
        )

        return OrdenRepository.guardar(orden)

    @staticmethod
    def obtener_orden(orden_id):
        orden = OrdenRepository.buscar_por_id(orden_id)

        if orden is None:
            raise ValueError("La orden indicada no existe.")

        return orden

    @staticmethod
    def listar_ordenes():
        return OrdenRepository.listar_todas()

    @staticmethod
    def listar_ordenes_tecnico(tecnico_id):
        return OrdenRepository.listar_por_tecnico(tecnico_id)

    @staticmethod
    def listar_ordenes_equipo(equipo_id):
        return OrdenRepository.listar_por_equipo(equipo_id)

    @staticmethod
    def asignar_tecnico(orden_id, tecnico_id):
        orden = OrdenService.obtener_orden(orden_id)

        tecnico = UsuarioRepository.buscar_por_id(tecnico_id)

        if tecnico is None:
            raise ValueError("El técnico indicado no existe.")

        if tecnico.rol != RolUsuario.TECNICO:
            raise ValueError(
                "El usuario indicado no corresponde a un técnico."
            )

        if not tecnico.activo:
            raise ValueError("El técnico indicado está inactivo.")

        orden.asignar_tecnico(tecnico)

        OrdenRepository.confirmar_cambios()

        return orden

    @staticmethod
    def cambiar_prioridad(orden_id, prioridad):
        orden = OrdenService.obtener_orden(orden_id)

        if isinstance(prioridad, str):
            try:
                prioridad = PrioridadOrden(prioridad)
            except ValueError:
                raise ValueError(
                    "La prioridad indicada no es válida."
                )

        estrategia = OrdenService.ESTRATEGIAS_PRIORIDAD.get(
            prioridad
        )

        if estrategia is None:
            raise ValueError(
                "No existe una estrategia para esa prioridad."
            )

        nueva_prioridad = estrategia.obtener_prioridad()

        orden.cambiar_prioridad(nueva_prioridad)

        OrdenRepository.confirmar_cambios()

        return orden

    @staticmethod
    def cambiar_estado(orden_id, nuevo_estado, usuario_id):
        orden = OrdenService.obtener_orden(orden_id)

        usuario = UsuarioRepository.buscar_por_id(usuario_id)

        if usuario is None:
            raise ValueError("El usuario indicado no existe.")

        if not usuario.activo:
            raise ValueError("El usuario indicado está inactivo.")

        if (
            usuario.rol == RolUsuario.TECNICO
            and orden.tecnico_id != usuario.id
        ):
            raise ValueError(
                "El técnico no está asignado a esta orden."
            )

        if usuario.rol == RolUsuario.CLIENTE:
            raise ValueError(
                "El cliente no tiene permiso para cambiar el estado."
            )

        if isinstance(nuevo_estado, str):
            try:
                nuevo_estado = EstadoOrden(nuevo_estado)
            except ValueError:
                raise ValueError("El estado indicado no es válido.")

        estado_anterior = orden.estado_actual

        estados_permitidos = OrdenService.TRANSICIONES_VALIDAS.get(
            estado_anterior,
            set()
        )

        if nuevo_estado not in estados_permitidos:
            raise ValueError(
                f"No se puede cambiar de "
                f"{estado_anterior.value} a {nuevo_estado.value}."
            )

        orden.cambiar_estado(nuevo_estado)

        historial = HistorialEstado(
            orden_id=orden.id,
            usuario_id=usuario.id,
            estado_anterior=estado_anterior,
            estado_nuevo=nuevo_estado
        )

        try:
            HistorialRepository.agregar(historial)

            for observador in OrdenService.OBSERVADORES:
                observador.actualizar(
                    orden,
                    estado_anterior,
                    nuevo_estado
                )

            OrdenRepository.confirmar_cambios()

        except Exception:
            OrdenRepository.rollback()
            raise

        return orden