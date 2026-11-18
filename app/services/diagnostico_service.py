from app.models import Diagnostico, EstadoOrden, RolUsuario
from app.repositories import (
    DiagnosticoRepository,
    OrdenRepository,
    UsuarioRepository,
)


class DiagnosticoService:

    @staticmethod
    def registrar_diagnostico(
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
                "Solo un técnico puede registrar diagnósticos."
            )

        if orden.tecnico_id != usuario.id:
            raise ValueError(
                "El técnico no está asignado a esta orden."
            )

        if orden.estado_actual not in {
            EstadoOrden.EN_DIAGNOSTICO,
            EstadoOrden.EN_REPARACION,
        }:
            raise ValueError(
                "La orden no se encuentra en un estado válido "
                "para registrar un diagnóstico."
            )

        descripcion = descripcion.strip()

        if not descripcion:
            raise ValueError(
                "La descripción del diagnóstico es obligatoria."
            )

        diagnostico = DiagnosticoRepository.buscar_por_orden(
            orden.id
        )

        if diagnostico is None:
            diagnostico = Diagnostico(
                orden_id=orden.id,
                descripcion=descripcion
            )

            return DiagnosticoRepository.guardar(diagnostico)

        diagnostico.actualizar(descripcion)

        DiagnosticoRepository.confirmar_cambios()

        return diagnostico

    @staticmethod
    def obtener_diagnostico_orden(orden_id):
        return DiagnosticoRepository.buscar_por_orden(orden_id)