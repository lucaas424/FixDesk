from sqlalchemy import select

from app.extensions import db
from app.models import Diagnostico


class DiagnosticoRepository:

    @staticmethod
    def buscar_por_id(diagnostico_id):
        return db.session.get(Diagnostico, diagnostico_id)

    @staticmethod
    def buscar_por_orden(orden_id):
        sentencia = select(Diagnostico).where(
            Diagnostico.orden_id == orden_id
        )

        return db.session.execute(
            sentencia
        ).scalar_one_or_none()

    @staticmethod
    def guardar(diagnostico):
        db.session.add(diagnostico)
        db.session.commit()
        return diagnostico

    @staticmethod
    def confirmar_cambios():
        db.session.commit()

    @staticmethod
    def rollback():
        db.session.rollback()