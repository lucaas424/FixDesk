from sqlalchemy import select

from app.extensions import db
from app.models import Equipo


class EquipoRepository:

    @staticmethod
    def buscar_por_id(equipo_id):
        return db.session.get(Equipo, equipo_id)

    @staticmethod
    def listar_todos():
        sentencia = select(Equipo).order_by(
            Equipo.marca,
            Equipo.modelo
        )

        return db.session.execute(
            sentencia
        ).scalars().all()

    @staticmethod
    def listar_por_cliente(cliente_id):
        sentencia = select(Equipo).where(
            Equipo.cliente_id == cliente_id
        ).order_by(
            Equipo.marca,
            Equipo.modelo
        )

        return db.session.execute(
            sentencia
        ).scalars().all()

    @staticmethod
    def buscar_por_numero_serie(numero_serie):
        sentencia = select(Equipo).where(
            Equipo.numero_serie == numero_serie
        )

        return db.session.execute(
            sentencia
        ).scalar_one_or_none()

    @staticmethod
    def guardar(equipo):
        db.session.add(equipo)
        db.session.commit()
        return equipo

    @staticmethod
    def confirmar_cambios():
        db.session.commit()

    @staticmethod
    def rollback():
        db.session.rollback()