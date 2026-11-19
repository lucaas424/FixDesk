from app.models import RolUsuario
from app.repositories import (
    EquipoRepository,
    UsuarioRepository,
)

from app.services.auth_service import AuthService
from app.services.orden_service import OrdenService
from app.services.equipo_service import EquipoService


class AdministracionService:

    @staticmethod
    def listar_ordenes():
        return OrdenService.listar_ordenes()

    @staticmethod
    def obtener_orden(orden_id):
        return OrdenService.obtener_orden(orden_id)

    @staticmethod
    def listar_equipos():
        return EquipoRepository.listar_todos()

    @staticmethod
    def registrar_equipo(
        cliente_id,
        tipo,
        marca,
        modelo,
        numero_serie
    ):
        return EquipoService.registrar_equipo(
            cliente_id=cliente_id,
            tipo=tipo,
            marca=marca,
            modelo=modelo,
            numero_serie=numero_serie
        )

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

    @staticmethod
    def asignar_tecnico(orden_id, tecnico_id):
        return OrdenService.asignar_tecnico(
            orden_id,
            tecnico_id
        )

    @staticmethod
    def cambiar_prioridad(orden_id, prioridad):
        return OrdenService.cambiar_prioridad(
            orden_id,
            prioridad
        )

    @staticmethod
    def registrar_tecnico(
        nombre,
        apellido,
        email,
        password
    ):
        return AuthService.registrar_usuario(
            nombre=nombre,
            apellido=apellido,
            email=email,
            password=password,
            rol=RolUsuario.TECNICO
        )
    @staticmethod
    def registrar_cliente(
        nombre,
        apellido,
        email,
        password
    ):
        return AuthService.registrar_usuario(
            nombre=nombre,
            apellido=apellido,
            email=email,
            password=password,
            rol=RolUsuario.CLIENTE
        )