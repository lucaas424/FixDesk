from datetime import datetime

from app.extensions import db


class Notificacion(db.Model):
    __tablename__ = "notificacion"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    cliente_id = db.Column(
        db.Integer,
        db.ForeignKey("usuario.id"),
        nullable=False
    )

    orden_id = db.Column(
        db.Integer,
        db.ForeignKey("orden_reparacion.id"),
        nullable=False
    )

    mensaje = db.Column(
        db.String(255),
        nullable=False
    )

    leida = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    fecha_creacion = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    cliente = db.relationship(
        "Cliente",
        back_populates="notificaciones",
        foreign_keys=[cliente_id]
    )

    orden = db.relationship(
        "OrdenReparacion",
        back_populates="notificaciones"
    )

    def marcar_como_leida(self):
        self.leida = True

    def __repr__(self):
        return (
            f"<Notificacion cliente={self.cliente_id} "
            f"orden={self.orden_id}>"
        )