from datetime import datetime

from app.extensions import db


class Diagnostico(db.Model):
    __tablename__ = "diagnostico"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    orden_id = db.Column(
        db.Integer,
        db.ForeignKey("orden_reparacion.id"),
        nullable=False,
        unique=True
    )

    descripcion = db.Column(
        db.Text,
        nullable=False
    )

    fecha_creacion = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    fecha_actualizacion = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    orden = db.relationship(
        "OrdenReparacion",
        back_populates="diagnostico"
    )

    def actualizar(self, descripcion):
        self.descripcion = descripcion
        self.fecha_actualizacion = datetime.utcnow()

    def __repr__(self):
        return f"<Diagnostico orden={self.orden_id}>"