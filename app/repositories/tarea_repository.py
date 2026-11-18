from sqlalchemy import select

from app.extensions import db
from app.models import TareaReparacion


class TareaRepository:

    @staticmethod
    def buscar_por_id(tarea_id):
        return db.session.get(TareaReparacion, tarea_id)

    @staticmethod
    def listar_por_orden(orden_id):
        sentencia = select(TareaReparacion).where(
            TareaReparacion.orden_id == orden_id
        ).order_by(
            TareaReparacion.fecha_realizacion.desc()
        )

        return db.session.execute(
            sentencia
        ).scalars().all()

    @staticmethod
    def guardar(tarea):
        db.session.add(tarea)
        db.session.commit()
        return tarea

    @staticmethod
    def confirmar_cambios():
        db.session.commit()

    @staticmethod
    def rollback():
        db.session.rollback()