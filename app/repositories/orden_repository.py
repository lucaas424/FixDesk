from sqlalchemy import select

from app.extensions import db
from app.models import (
    OrdenReparacion,
    EstadoOrden,
    PrioridadOrden,
)


class OrdenRepository:

    @staticmethod
    def buscar_por_id(orden_id):
        return db.session.get(OrdenReparacion, orden_id)

    @staticmethod
    def listar_todas():
        sentencia = select(OrdenReparacion).order_by(
            OrdenReparacion.fecha_recepcion.desc()
        )

        return db.session.execute(
            sentencia
        ).scalars().all()

    @staticmethod
    def listar_por_tecnico(tecnico_id):
        sentencia = select(OrdenReparacion).where(
            OrdenReparacion.tecnico_id == tecnico_id
        ).order_by(
            OrdenReparacion.fecha_recepcion.desc()
        )

        return db.session.execute(
            sentencia
        ).scalars().all()

    @staticmethod
    def listar_por_equipo(equipo_id):
        sentencia = select(OrdenReparacion).where(
            OrdenReparacion.equipo_id == equipo_id
        ).order_by(
            OrdenReparacion.fecha_recepcion.desc()
        )

        return db.session.execute(
            sentencia
        ).scalars().all()

    @staticmethod
    def listar_por_estado(estado):
        if isinstance(estado, str):
            estado = EstadoOrden(estado)

        sentencia = select(OrdenReparacion).where(
            OrdenReparacion.estado_actual == estado
        ).order_by(
            OrdenReparacion.fecha_recepcion.desc()
        )

        return db.session.execute(
            sentencia
        ).scalars().all()

    @staticmethod
    def listar_por_prioridad(prioridad):
        if isinstance(prioridad, str):
            prioridad = PrioridadOrden(prioridad)

        sentencia = select(OrdenReparacion).where(
            OrdenReparacion.prioridad == prioridad
        ).order_by(
            OrdenReparacion.fecha_recepcion.desc()
        )

        return db.session.execute(
            sentencia
        ).scalars().all()

    @staticmethod
    def guardar(orden):
        db.session.add(orden)
        db.session.commit()
        return orden

    @staticmethod
    def confirmar_cambios():
        db.session.commit()

    @staticmethod
    def rollback():
        db.session.rollback()