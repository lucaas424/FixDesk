from sqlalchemy import select

from app.extensions import db
from app.models import HistorialEstado


class HistorialRepository:

    @staticmethod
    def buscar_por_id(historial_id):
        return db.session.get(HistorialEstado, historial_id)

    @staticmethod
    def agregar(historial):
        db.session.add(historial)
        return historial

    @staticmethod
    def listar_por_orden(orden_id):
        sentencia = select(HistorialEstado).where(
            HistorialEstado.orden_id == orden_id
        ).order_by(
            HistorialEstado.fecha_cambio.asc()
        )

        return db.session.execute(
            sentencia
        ).scalars().all()

    @staticmethod
    def listar_por_usuario(usuario_id):
        sentencia = select(HistorialEstado).where(
            HistorialEstado.usuario_id == usuario_id
        ).order_by(
            HistorialEstado.fecha_cambio.desc()
        )

        return db.session.execute(
            sentencia
        ).scalars().all()

    @staticmethod
    def guardar(historial):
        db.session.add(historial)
        db.session.commit()
        return historial

    @staticmethod
    def confirmar_cambios():
        db.session.commit()

    @staticmethod
    def rollback():
        db.session.rollback()