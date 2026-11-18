from app.models import RolUsuario
from app.repositories import (
    EquipoRepository,
    UsuarioRepository,
)

from app.services.orden_service import OrdenService


class AdministracionService:

    @staticmethod
    def listar_ordenes():
        return OrdenService.listar_ordenes()

    @staticmethod
    def listar_equipos():
        return EquipoRepository.listar_todos()

    @staticmethod
    def listar_clientes():
        return UsuarioRepository.listar_por_rol(
            RolUsuario.CLIENTE
        )

    @staticmethod
    def listar_tecnicos():
        return UsuarioRepository.listar_por_rol(
            RolUsuario.TECNICO
        )

    @staticmethod
    def crear_orden(
        equipo_id,
        tecnico_id,
        problema_reportado,
        prioridad,
        observaciones=None
    ):
        return OrdenService.crear_orden(
            equipo_id=equipo_id,
            tecnico_id=tecnico_id,
            problema_reportado=problema_reportado,
            prioridad=prioridad,
            observaciones=observaciones
        )