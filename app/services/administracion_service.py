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