from datetime import datetime

from app.extensions import db


class TareaReparacion(db.Model):
    __tablename__ = "tarea_reparacion"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    orden_id = db.Column(
        db.Integer,
        db.ForeignKey("orden_reparacion.id"),
        nullable=False
    )

    descripcion = db.Column(
        db.Text,
        nullable=False
    )

    fecha_realizacion = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    orden = db.relationship(
        "OrdenReparacion",
        back_populates="tareas"
    )

    def actualizar(self, descripcion):
        self.descripcion = descripcion

    def __repr__(self):
        return f"<TareaReparacion orden={self.orden_id}>"