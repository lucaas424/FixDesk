from datetime import datetime

from app.extensions import db
from app.models.enums import TipoEquipo


class Equipo(db.Model):
    __tablename__ = "equipo"

    id = db.Column(db.Integer, primary_key=True)

    cliente_id = db.Column(
        db.Integer,
        db.ForeignKey("usuario.id"),
        nullable=False
    )

    tipo = db.Column(
        db.Enum(TipoEquipo),
        nullable=False
    )

    marca = db.Column(
        db.String(80),
        nullable=False
    )

    modelo = db.Column(
        db.String(100),
        nullable=False
    )

    numero_serie = db.Column(
        db.String(120),
        nullable=False
    )

    activo = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    fecha_registro = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    cliente = db.relationship(
        "Cliente",
        back_populates="equipos",
        foreign_keys=[cliente_id]
    )

    ordenes = db.relationship(
        "OrdenReparacion",
        back_populates="equipo",
        lazy=True
    )

    def actualizar_datos(self, marca=None, modelo=None, numero_serie=None):
        if marca is not None:
            self.marca = marca

        if modelo is not None:
            self.modelo = modelo

        if numero_serie is not None:
            self.numero_serie = numero_serie

    def activar(self):
        self.activo = True

    def desactivar(self):
        self.activo = False

    def __repr__(self):
        return (
            f"<Equipo {self.tipo.value} "
            f"{self.marca} {self.modelo}>"
        )