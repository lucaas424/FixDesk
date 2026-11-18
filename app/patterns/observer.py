from abc import ABC, abstractmethod

from app.models import Notificacion, EstadoOrden
from app.repositories import NotificacionRepository


class OrdenObserver(ABC):

    @abstractmethod
    def actualizar(self, orden, estado_anterior, nuevo_estado):
        pass


class NotificacionObserver(OrdenObserver):

    def actualizar(self, orden, estado_anterior, nuevo_estado):
        if nuevo_estado != EstadoOrden.LISTO_PARA_RETIRAR:
            return None

        notificacion = Notificacion(
            cliente_id=orden.equipo.cliente_id,
            orden_id=orden.id,
            mensaje="Tu equipo ya se encuentra listo para retirar."
        )

        NotificacionRepository.agregar(notificacion)

        return notificacion