from app.models import (
    Administrador,
    Tecnico,
    Cliente,
    RolUsuario,
)
from app.repositories import UsuarioRepository


class AuthService:

    @staticmethod
    def autenticar(email, password):
        if not email or not password:
            return None

        email = email.strip().lower()

        usuario = UsuarioRepository.buscar_por_email(email)

        if usuario is None:
            return None

        if not usuario.activo:
            return None

        if not usuario.verificar_password(password):
            return None

        return usuario

    @staticmethod
    def registrar_usuario(
        nombre,
        apellido,
        email,
        password,
        rol
    ):
        nombre = nombre.strip()
        apellido = apellido.strip()
        email = email.strip().lower()

        if not nombre:
            raise ValueError("El nombre es obligatorio.")

        if not apellido:
            raise ValueError("El apellido es obligatorio.")

        if not email:
            raise ValueError("El email es obligatorio.")

        if not password or len(password) < 8:
            raise ValueError(
                "La contraseña debe tener al menos 8 caracteres."
            )

        if isinstance(rol, str):
            try:
                rol = RolUsuario(rol)
            except ValueError:
                raise ValueError("El rol indicado no es válido.")

        usuario_existente = UsuarioRepository.buscar_por_email(email)

        if usuario_existente is not None:
            raise ValueError("Ya existe un usuario con ese email.")

        clases_por_rol = {
            RolUsuario.ADMINISTRADOR: Administrador,
            RolUsuario.TECNICO: Tecnico,
            RolUsuario.CLIENTE: Cliente,
        }

        clase_usuario = clases_por_rol.get(rol)

        if clase_usuario is None:
            raise ValueError("El rol indicado no es válido.")

        usuario = clase_usuario(
            nombre=nombre,
            apellido=apellido,
            email=email,
            activo=True
        )

        usuario.set_password(password)

        return UsuarioRepository.guardar(usuario)