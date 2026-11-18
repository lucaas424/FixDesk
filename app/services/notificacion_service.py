from app.models import RolUsuario
from app.repositories import (
    NotificacionRepository,
    UsuarioRepository,
)


class NotificacionService:

    @staticmethod
    def listar_notificaciones_cliente(cliente_id):
        cliente = UsuarioRepository.buscar_por_id(cliente_id)

        if cliente is None:
            raise ValueError("El cliente indicado no existe.")

        if cliente.rol != RolUsuario.CLIENTE:
            raise ValueError(
                "El usuario indicado no corresponde a un cliente."
            )

        return NotificacionRepository.listar_por_cliente(
            cliente_id
        )

    @staticmethod
    def listar_no_leidas(cliente_id):
        cliente = UsuarioRepository.buscar_por_id(cliente_id)

        if cliente is None:
            raise ValueError("El cliente indicado no existe.")

        if cliente.rol != RolUsuario.CLIENTE:
            raise ValueError(
                "El usuario indicado no corresponde a un cliente."
            )

        return NotificacionRepository.listar_no_leidas_por_cliente(
            cliente_id
        )

    @staticmethod
    def marcar_como_leida(notificacion_id, cliente_id):
        notificacion = NotificacionRepository.buscar_por_id(
            notificacion_id
        )

        if notificacion is None:
            raise ValueError(
                "La notificación indicada no existe."
            )

        if notificacion.cliente_id != cliente_id:
            raise ValueError(
                "La notificación no pertenece a este cliente."
            )

        notificacion.marcar_como_leida()

        NotificacionRepository.confirmar_cambios()

        return notificacion