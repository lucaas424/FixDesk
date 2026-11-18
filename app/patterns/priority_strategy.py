from abc import ABC, abstractmethod

from app.models import PrioridadOrden


class PrioridadStrategy(ABC):

    @abstractmethod
    def obtener_prioridad(self):
        pass


class PrioridadBajaStrategy(PrioridadStrategy):

    def obtener_prioridad(self):
        return PrioridadOrden.BAJA


class PrioridadNormalStrategy(PrioridadStrategy):

    def obtener_prioridad(self):
        return PrioridadOrden.NORMAL


class PrioridadAltaStrategy(PrioridadStrategy):

    def obtener_prioridad(self):
        return PrioridadOrden.ALTA


class PrioridadUrgenteStrategy(PrioridadStrategy):

    def obtener_prioridad(self):
        return PrioridadOrden.URGENTE