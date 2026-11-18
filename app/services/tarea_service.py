from app.models import TareaReparacion, EstadoOrden, RolUsuario
from app.repositories import (
    TareaRepository,
    OrdenRepository,
    UsuarioRepository,
)


class TareaService:

    @staticmethod
    def registrar_tarea(
        orden_id,
        descripcion,
        usuario_id
    ):
        orden = OrdenRepository.buscar_por_id(orden_id)

        if orden is None:
            raise ValueError("La orden indicada no existe.")

        usuario = UsuarioRepository.buscar_por_id(usuario_id)

        if usuario is None:
            raise ValueError("El usuario indicado no existe.")

        if usuario.rol != RolUsuario.TECNICO:
            raise ValueError(
                "Solo un técnico puede registrar tareas."
            )

        if orden.tecnico_id != usuario.id:
            raise ValueError(
                "El técnico no está asignado a esta orden."
            )

        if orden.estado_actual not in {
            EstadoOrden.EN_REPARACION,
            EstadoOrden.LISTO_PARA_RETIRAR,
        }:
            raise ValueError(
                "La orden no se encuentra en un estado válido "
                "para registrar tareas."
            )

        descripcion = descripcion.strip()

        if not descripcion:
            raise ValueError(
                "La descripción de la tarea es obligatoria."
            )

        tarea = TareaReparacion(
            orden_id=orden.id,
            descripcion=descripcion
        )

        return TareaRepository.guardar(tarea)

    @staticmethod
    def listar_tareas_orden(orden_id):
        return TareaRepository.listar_por_orden(orden_id)