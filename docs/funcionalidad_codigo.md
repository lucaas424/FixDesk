# Funcionalidad a Nivel de Código — FixDesk

## 1. Organización general

FixDesk será desarrollado utilizando Python y Flask mediante una arquitectura organizada en capas.

La estructura principal estará compuesta por:

- Models.
- Controllers.
- Services.
- Repositories.
- Views/Templates.
- Patterns.
- Utils.

Cada módulo tendrá una responsabilidad específica para evitar concentración excesiva de lógica y mantener un bajo acoplamiento entre componentes.

---

## 2. Models

Los modelos representarán las principales entidades del dominio y serán utilizados también para su persistencia mediante SQLAlchemy.

### Usuario

Será la clase base de los usuarios del sistema.

Contendrá información común como:

- Identificador.
- Nombre.
- Apellido.
- Correo electrónico.
- Contraseña cifrada.
- Rol.
- Estado activo/inactivo.
- Fecha de creación.

También contendrá comportamientos comunes relacionados con autenticación y activación/desactivación.

### Administrador

Especialización de Usuario.

Representará al usuario con mayores permisos administrativos dentro de FixDesk.

Podrá gestionar clientes, técnicos, equipos y órdenes de reparación.

### Tecnico

Especialización de Usuario.

Representará al personal encargado de diagnosticar y reparar equipos.

Tendrá acceso a las órdenes que le hayan sido asignadas.

### Cliente

Especialización de Usuario.

Representará al propietario de uno o varios equipos.

Podrá consultar sus dispositivos, órdenes de reparación y notificaciones.

### Equipo

Representará un dispositivo registrado en el servicio técnico.

Contendrá:

- Tipo.
- Marca.
- Modelo.
- Número de serie.
- Estado activo/inactivo.
- Cliente propietario.

Los tipos admitidos serán:

- NOTEBOOK.
- CELULAR.
- TABLET.

### OrdenReparacion

Será una de las entidades centrales del sistema.

Representará el proceso de reparación de un equipo y almacenará:

- Problema reportado.
- Prioridad.
- Estado actual.
- Técnico asignado.
- Fecha de recepción.
- Fecha estimada.
- Fecha de finalización.
- Observaciones.

También contendrá operaciones relacionadas con cambios de estado, prioridad, asignación y cancelación.

### Diagnostico

Almacenará el diagnóstico técnico asociado a una orden de reparación.

Cada orden podrá poseer como máximo un diagnóstico.

### TareaReparacion

Representará una tarea realizada por un técnico durante el proceso de reparación.

Una orden podrá poseer múltiples tareas.

### HistorialEstado

Registrará cada cambio de estado ocurrido sobre una orden.

Almacenará:

- Estado anterior.
- Estado nuevo.
- Fecha del cambio.
- Usuario responsable.

### Notificacion

Representará los avisos internos enviados a los clientes.

Permitirá almacenar el mensaje, la fecha y si fue leído o no.

---

## 3. Controllers

Los controladores recibirán las solicitudes provenientes de la interfaz web.

Sus responsabilidades principales serán:

- Recibir solicitudes HTTP.
- Obtener parámetros y formularios.
- Validar el acceso del usuario.
- Delegar la lógica de negocio a los servicios.
- Seleccionar la respuesta o vista correspondiente.

Se prevén controladores como:

- AuthController.
- ClienteController.
- EquipoController.
- OrdenController.

Los controladores no contendrán directamente la lógica principal del negocio ni realizarán consultas directas a MySQL.

---

## 4. Services

La capa Service contendrá la lógica de negocio de FixDesk.

Se prevén servicios como:

- AuthService.
- ClienteService.
- EquipoService.
- OrdenService.
- NotificacionService.

Por ejemplo, OrdenService será responsable de:

- Crear órdenes.
- Asignar técnicos.
- Validar cambios de estado.
- Cambiar prioridades.
- Registrar historial.
- Coordinar la generación de notificaciones.

---

## 5. Repositories

Los repositorios serán responsables del acceso a los datos.

Se prevén:

- UsuarioRepository.
- EquipoRepository.
- OrdenRepository.
- HistorialRepository.
- NotificacionRepository.

Los Services utilizarán los Repositories para consultar o modificar información persistida.

Esta capa permitirá evitar que la lógica de negocio dependa directamente de consultas específicas a la base de datos.

---

## 6. Views y Templates

La interfaz web será desarrollada utilizando:

- HTML.
- CSS.
- Bootstrap.
- Jinja2.
- JavaScript cuando sea necesario.

Existirán diferentes vistas según el rol autenticado.

### Administrador

Dispondrá de acceso a:

- Gestión de clientes.
- Gestión de técnicos.
- Gestión de equipos.
- Gestión de órdenes.
- Filtros y consultas.

### Técnico

Dispondrá de acceso a:

- Órdenes asignadas.
- Diagnósticos.
- Tareas realizadas.
- Cambios de estado.
- Historial.

### Cliente

Dispondrá de acceso a:

- Sus equipos.
- Sus reparaciones.
- Estados.
- Diagnósticos.
- Notificaciones.

---

## 7. Patrón MVC

FixDesk aplicará el patrón Modelo-Vista-Controlador.

### Modelo

Representará los datos y entidades del dominio.

### Vista

Representará las páginas que visualiza el usuario.

### Controlador

Gestionará las solicitudes realizadas desde la interfaz y coordinará las operaciones correspondientes.

La arquitectura será complementada mediante las capas Service y Repository.

---

## 8. Patrón Singleton

Se utilizará Singleton para disponer de una única instancia centralizada de determinados componentes de configuración o acceso compartido.

Su finalidad será evitar la creación innecesaria de múltiples instancias de un mismo recurso.

---

## 9. Patrón Observer

Observer será utilizado en el proceso de actualización de una orden.

Cuando se produzca un cambio relevante de estado, el sistema podrá generar automáticamente una reacción asociada.

El principal caso será:

**Orden cambia a LISTO_PARA_RETIRAR → se genera una notificación para el cliente.**

De esta manera, el cambio de estado actúa como evento que dispara una actualización sobre otro componente del sistema.

---

## 10. Patrón Strategy

Strategy se utilizará para encapsular diferentes criterios relacionados con la prioridad de las órdenes.

Cada estrategia podrá determinar el tratamiento correspondiente a una prioridad:

- BAJA.
- NORMAL.
- ALTA.
- URGENTE.

Esto permitirá modificar o extender las reglas de priorización sin concentrarlas en una única estructura condicional extensa.

---

## 11. Seguridad

El sistema implementará:

- Contraseñas almacenadas mediante hash.
- Control de acceso según rol.
- Validación de formularios.
- Protección CSRF.
- Sanitización de entradas.
- Variables de entorno para credenciales.
- Restricción de acceso a información perteneciente a otros usuarios.

---

## 12. Manejo de errores

Los errores serán controlados evitando mostrar información sensible o detalles internos de implementación.

Se contemplarán situaciones como:

- Datos inválidos.
- Usuario sin permisos.
- Orden inexistente.
- Transición de estado inválida.
- Error de acceso a base de datos.

Las respuestas deberán proporcionar mensajes comprensibles para el usuario.

---

## 13. Logging

La aplicación contará con registros de logs destinados a facilitar la identificación de errores y eventos importantes.

Los logs podrán registrar:

- Errores de aplicación.
- Excepciones.
- Problemas de persistencia.
- Operaciones relevantes del sistema.

Los archivos generados dentro del directorio de logs no serán versionados en Git.

---

## 14. Flujo general del código

El flujo habitual de una operación será:

**Usuario → Vista → Controller → Service → Repository → SQLAlchemy → MySQL**

Una vez procesada la operación, la información volverá hacia la interfaz siguiendo el flujo inverso.

Esta organización permite mantener separadas las responsabilidades de presentación, lógica de negocio y persistencia.