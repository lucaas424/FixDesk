from datetime import datetime

from app.extensions import db
from app.models.enums import EstadoOrden


class HistorialEstado(db.Model):
    __tablename__ = "historial_estado"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    orden_id = db.Column(
        db.Integer,
        db.ForeignKey("orden_reparacion.id"),
        nullable=False
    )

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuario.id"),
        nullable=False
    )

    estado_anterior = db.Column(
        db.Enum(EstadoOrden),
        nullable=False
    )

    estado_nuevo = db.Column(
        db.Enum(EstadoOrden),
        nullable=False
    )

    fecha_cambio = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    orden = db.relationship(
        "OrdenReparacion",
        back_populates="historial_estados"
    )

    usuario = db.relationship(
        "Usuario",
        back_populates="historial_cambios",
        foreign_keys=[usuario_id]
    )

    def __repr__(self):
        return (
            f"<HistorialEstado orden={self.orden_id} "
            f"{self.estado_anterior.value} -> "
            f"{self.estado_nuevo.value}>"
        )