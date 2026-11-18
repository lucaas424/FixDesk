from sqlalchemy import select

from app.extensions import db
from app.models import Notificacion


class NotificacionRepository:

    @staticmethod
    def buscar_por_id(notificacion_id):
        return db.session.get(Notificacion, notificacion_id)
    
    @staticmethod
    def agregar(notificacion):
        db.session.add(notificacion)
        return notificacion
    
    @staticmethod
    def listar_por_cliente(cliente_id):
        sentencia = select(Notificacion).where(
            Notificacion.cliente_id == cliente_id
        ).order_by(
            Notificacion.fecha_creacion.desc()
        )

        return db.session.execute(
            sentencia
        ).scalars().all()

    @staticmethod
    def listar_no_leidas_por_cliente(cliente_id):
        sentencia = select(Notificacion).where(
            Notificacion.cliente_id == cliente_id,
            Notificacion.leida.is_(False)
        ).order_by(
            Notificacion.fecha_creacion.desc()
        )

        return db.session.execute(
            sentencia
        ).scalars().all()

    @staticmethod
    def listar_por_orden(orden_id):
        sentencia = select(Notificacion).where(
            Notificacion.orden_id == orden_id
        ).order_by(
            Notificacion.fecha_creacion.desc()
        )

        return db.session.execute(
            sentencia
        ).scalars().all()

    @staticmethod
    def guardar(notificacion):
        db.session.add(notificacion)
        db.session.commit()
        return notificacion

    @staticmethod
    def confirmar_cambios():
        db.session.commit()

    @staticmethod
    def rollback():
        db.session.rollback()