from app.models import Equipo, TipoEquipo, RolUsuario
from app.repositories import EquipoRepository, UsuarioRepository


class EquipoService:

    @staticmethod
    def registrar_equipo(
        cliente_id,
        tipo,
        marca,
        modelo,
        numero_serie
    ):
        cliente = UsuarioRepository.buscar_por_id(cliente_id)

        if cliente is None:
            raise ValueError("El cliente indicado no existe.")

        if cliente.rol != RolUsuario.CLIENTE:
            raise ValueError(
                "El usuario indicado no corresponde a un cliente."
            )

        if isinstance(tipo, str):
            try:
                tipo = TipoEquipo(tipo)
            except ValueError:
                raise ValueError("El tipo de equipo no es válido.")

        marca = marca.strip()
        modelo = modelo.strip()
        numero_serie = numero_serie.strip()

        if not marca:
            raise ValueError("La marca es obligatoria.")

        if not modelo:
            raise ValueError("El modelo es obligatorio.")

        if not numero_serie:
            raise ValueError("El número de serie es obligatorio.")

        equipo_existente = EquipoRepository.buscar_por_numero_serie(
            numero_serie
        )

        if equipo_existente is not None:
            raise ValueError(
                "Ya existe un equipo con ese número de serie."
            )

        equipo = Equipo(
            cliente_id=cliente.id,
            tipo=tipo,
            marca=marca,
            modelo=modelo,
            numero_serie=numero_serie,
            activo=True
        )

        return EquipoRepository.guardar(equipo)

    @staticmethod
    def obtener_equipo(equipo_id):
        equipo = EquipoRepository.buscar_por_id(equipo_id)

        if equipo is None:
            raise ValueError("El equipo indicado no existe.")

        return equipo

    @staticmethod
    def listar_equipos_cliente(cliente_id):
        return EquipoRepository.listar_por_cliente(cliente_id)

    @staticmethod
    def actualizar_equipo(
        equipo_id,
        marca=None,
        modelo=None,
        numero_serie=None
    ):
        equipo = EquipoService.obtener_equipo(equipo_id)

        if marca is not None:
            marca = marca.strip()

        if modelo is not None:
            modelo = modelo.strip()

        if numero_serie is not None:
            numero_serie = numero_serie.strip()

            existente = EquipoRepository.buscar_por_numero_serie(
                numero_serie
            )

            if existente is not None and existente.id != equipo.id:
                raise ValueError(
                    "Ya existe otro equipo con ese número de serie."
                )

        equipo.actualizar_datos(
            marca=marca,
            modelo=modelo,
            numero_serie=numero_serie
        )

        EquipoRepository.confirmar_cambios()

        return equipo

    @staticmethod
    def activar_equipo(equipo_id):
        equipo = EquipoService.obtener_equipo(equipo_id)
        equipo.activar()
        EquipoRepository.confirmar_cambios()
        return equipo

    @staticmethod
    def desactivar_equipo(equipo_id):
        equipo = EquipoService.obtener_equipo(equipo_id)
        equipo.desactivar()
        EquipoRepository.confirmar_cambios()
        return equipo