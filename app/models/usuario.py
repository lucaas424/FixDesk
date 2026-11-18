from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db
from app.models.enums import RolUsuario


class Usuario(UserMixin, db.Model):
    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.Enum(RolUsuario), nullable=False)
    activo = db.Column(db.Boolean, nullable=False, default=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    __mapper_args__ = {
        "polymorphic_on": rol
    }
    historial_cambios = db.relationship(
        "HistorialEstado",
        back_populates="usuario",
        foreign_keys="HistorialEstado.usuario_id",
        lazy=True
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verificar_password(self, password):
        return check_password_hash(self.password_hash, password)

    def activar(self):
        self.activo = True

    def desactivar(self):
        self.activo = False

    @property
    def is_active(self):
        return self.activo

    def __repr__(self):
        return f"<Usuario {self.email}>"


class Administrador(Usuario):
    __mapper_args__ = {
        "polymorphic_identity": RolUsuario.ADMINISTRADOR
    }

    def gestionar_sistema(self):
        return True


class Tecnico(Usuario):
    __mapper_args__ = {
        "polymorphic_identity": RolUsuario.TECNICO
    }

    ordenes_asignadas = db.relationship(
        "OrdenReparacion",
        back_populates="tecnico",
        foreign_keys="OrdenReparacion.tecnico_id",
        lazy=True
    )


class Cliente(Usuario):
    __mapper_args__ = {
        "polymorphic_identity": RolUsuario.CLIENTE
    }

    equipos = db.relationship(
        "Equipo",
        back_populates="cliente",
        foreign_keys="Equipo.cliente_id",
        lazy=True
    )

    notificaciones = db.relationship(
        "Notificacion",
        back_populates="cliente",
        foreign_keys="Notificacion.cliente_id",
        lazy=True
    )