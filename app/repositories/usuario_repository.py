from sqlalchemy import select

from app.extensions import db
from app.models import Usuario, RolUsuario


class UsuarioRepository:

    @staticmethod
    def buscar_por_id(usuario_id):
        return db.session.get(Usuario, usuario_id)

    @staticmethod
    def buscar_por_email(email):
        sentencia = select(Usuario).where(
            Usuario.email == email
        )

        return db.session.execute(
            sentencia
        ).scalar_one_or_none()

    @staticmethod
    def listar_todos():
        sentencia = select(Usuario).order_by(
            Usuario.apellido,
            Usuario.nombre
        )

        return db.session.execute(
            sentencia
        ).scalars().all()

    @staticmethod
    def listar_por_rol(rol):
        if isinstance(rol, str):
            rol = RolUsuario(rol)

        sentencia = select(Usuario).where(
            Usuario.rol == rol
        ).order_by(
            Usuario.apellido,
            Usuario.nombre
        )

        return db.session.execute(
            sentencia
        ).scalars().all()

    @staticmethod
    def guardar(usuario):
        db.session.add(usuario)
        db.session.commit()
        return usuario

    @staticmethod
    def confirmar_cambios():
        db.session.commit()

    @staticmethod
    def rollback():
        db.session.rollback()