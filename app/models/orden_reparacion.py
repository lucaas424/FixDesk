from datetime import datetime

from app.extensions import db
from app.models.enums import PrioridadOrden, EstadoOrden


class OrdenReparacion(db.Model):
    __tablename__ = "orden_reparacion"

    id = db.Column(db.Integer, primary_key=True)

    equipo_id = db.Column(
        db.Integer,
        db.ForeignKey("equipo.id"),
        nullable=False
    )

    tecnico_id = db.Column(
        db.Integer,
        db.ForeignKey("usuario.id"),
        nullable=True
    )

    problema_reportado = db.Column(
        db.Text,
        nullable=False
    )

    prioridad = db.Column(
        db.Enum(PrioridadOrden),
        nullable=False,
        default=PrioridadOrden.NORMAL
    )

    estado_actual = db.Column(
        db.Enum(EstadoOrden),
        nullable=False,
        default=EstadoOrden.RECIBIDO
    )

    fecha_recepcion = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    fecha_estimada = db.Column(
        db.Date,
        nullable=True
    )

    fecha_finalizacion = db.Column(
        db.DateTime,
        nullable=True
    )

    observaciones = db.Column(
        db.Text,
        nullable=True
    )

    equipo = db.relationship(
        "Equipo",
        back_populates="ordenes"
    )

    tecnico = db.relationship(
        "Tecnico",
        back_populates="ordenes_asignadas",
        foreign_keys=[tecnico_id]
    )

    diagnostico = db.relationship(
        "Diagnostico",
        back_populates="orden",
        uselist=False,
        cascade="all, delete-orphan"
    )
    tareas = db.relationship(
        "TareaReparacion",
        back_populates="orden",
        cascade="all, delete-orphan",
        lazy=True
    )
    historial_estados = db.relationship(
        "HistorialEstado",
        back_populates="orden",
        cascade="all, delete-orphan",
        lazy=True
    )
    notificaciones = db.relationship(
        "Notificacion",
        back_populates="orden",
        cascade="all, delete-orphan",
        lazy=True
    )
    def asignar_tecnico(self, tecnico):
        self.tecnico = tecnico

    def cambiar_estado(self, nuevo_estado):
        self.estado_actual = nuevo_estado

        if nuevo_estado == EstadoOrden.FINALIZADO:
            self.fecha_finalizacion = datetime.utcnow()

    def cambiar_prioridad(self, nueva_prioridad):
        self.prioridad = nueva_prioridad

    def cancelar(self):
        self.estado_actual = EstadoOrden.CANCELADO
        self.fecha_finalizacion = datetime.utcnow()

    def __repr__(self):
        return (
            f"<OrdenReparacion {self.id} "
            f"- {self.estado_actual.value}>"
        )