# FixDesk — Sistema de Gestión de Servicio Técnico de Equipos Informáticos

## 1. Introducción

FixDesk es un sistema web orientado a la gestión integral de un servicio técnico de equipos informáticos. Su propósito es centralizar el registro de clientes, equipos y órdenes de reparación, permitiendo realizar el seguimiento completo de cada equipo desde su recepción hasta la finalización del servicio.

El sistema busca reemplazar el seguimiento manual realizado mediante anotaciones, planillas o comunicaciones informales, proporcionando información organizada, persistente y accesible según el rol de cada usuario.

---

## 2. Objetivo del sistema

El objetivo principal de FixDesk es brindar una herramienta que permita administrar de forma ordenada el proceso de reparación de equipos tecnológicos.

El sistema permitirá:

- Registrar clientes.
- Registrar los equipos pertenecientes a cada cliente.
- Crear órdenes de reparación.
- Asignar técnicos responsables.
- Registrar diagnósticos.
- Registrar tareas realizadas sobre una reparación.
- Gestionar los distintos estados de una orden.
- Mantener un historial de cambios.
- Informar al cliente sobre el progreso de su reparación.
- Generar notificaciones internas cuando se produzcan cambios relevantes.

---

## 3. Problema identificado

En pequeños y medianos servicios técnicos es frecuente que la información relacionada con los equipos recibidos, los clientes y las reparaciones sea administrada mediante planillas, mensajes, anotaciones o herramientas no especializadas.

Esto puede provocar:

- Pérdida de información.
- Dificultad para conocer el estado actual de una reparación.
- Falta de trazabilidad sobre las tareas realizadas.
- Errores en la asignación de técnicos.
- Dificultad para consultar reparaciones anteriores.
- Falta de información actualizada para el cliente.

FixDesk propone centralizar esta información en una única aplicación.

---

## 4. Alcance

FixDesk permitirá administrar reparaciones correspondientes exclusivamente a tres tipos de equipos:

- Notebook.
- Celular.
- Tablet.

El sistema tendrá tres tipos de usuarios:

- Administrador.
- Técnico.
- Cliente.

El sistema abarcará desde la recepción y registro inicial del equipo hasta la finalización o cancelación de la orden de reparación.

No estarán incluidos dentro del alcance:

- Facturación.
- Cobros.
- Pagos.
- Gestión de caja.
- Inventario de repuestos.
- Gestión de proveedores.
- Compras.
- Reserva de turnos.
- Chat en tiempo real.

---

## 5. Usuarios y roles

### 5.1 Administrador

El administrador posee el mayor nivel de permisos dentro del sistema.

Podrá:

- Iniciar y cerrar sesión.
- Visualizar un panel general.
- Registrar clientes.
- Editar clientes.
- Activar o desactivar clientes.
- Registrar técnicos.
- Editar técnicos.
- Activar o desactivar técnicos.
- Registrar equipos.
- Editar información de equipos.
- Crear órdenes de reparación.
- Asignar un técnico a una orden.
- Reasignar una orden a otro técnico.
- Consultar todas las órdenes.
- Filtrar órdenes por estado, cliente o técnico.
- Consultar diagnósticos y tareas realizadas.
- Modificar estados de una reparación.
- Cancelar órdenes.

Los registros históricos no serán eliminados físicamente de la base de datos.

---

### 5.2 Técnico

El técnico será responsable de realizar y documentar el trabajo técnico sobre las órdenes que le hayan sido asignadas.

Podrá:

- Iniciar y cerrar sesión.
- Visualizar su panel de trabajo.
- Consultar las órdenes que tiene asignadas.
- Consultar información del equipo.
- Consultar información básica del cliente propietario.
- Registrar un diagnóstico.
- Modificar el diagnóstico.
- Registrar tareas realizadas.
- Agregar observaciones.
- Modificar el estado de una reparación.
- Consultar el historial de estados.

No podrá:

- Crear clientes.
- Crear otros técnicos.
- Modificar usuarios.
- Eliminar órdenes.
- Consultar órdenes asignadas a otros técnicos sin autorización.
- Asignarse órdenes arbitrariamente.

---

### 5.3 Cliente

El cliente contará con acceso de consulta sobre sus propios equipos y reparaciones.

Podrá:

- Iniciar y cerrar sesión.
- Consultar sus equipos registrados.
- Consultar sus órdenes de reparación.
- Visualizar el estado actual de una reparación.
- Visualizar el diagnóstico.
- Consultar las tareas realizadas.
- Consultar el historial de estados.
- Visualizar sus notificaciones.

No podrá modificar información técnica ni administrativa.

---

## 6. Flujo general de una reparación

El flujo principal será el siguiente:

1. El administrador registra al cliente.
2. El administrador registra el equipo perteneciente al cliente.
3. El administrador crea una orden de reparación indicando el problema informado.
4. Se establece la prioridad de la orden.
5. Se asigna un técnico.
6. El técnico recibe la orden.
7. El técnico registra el diagnóstico.
8. El técnico registra las tareas realizadas.
9. El estado de la orden se modifica durante el proceso.
10. El cliente puede consultar el progreso.
11. Al producirse cambios relevantes, el sistema genera notificaciones internas.
12. La orden finaliza cuando el equipo es entregado o el servicio es cancelado.

---

## 7. Estados de una orden

Una orden podrá encontrarse en los siguientes estados:

- RECIBIDO.
- EN DIAGNÓSTICO.
- EN REPARACIÓN.
- LISTO PARA RETIRAR.
- FINALIZADO.
- CANCELADO.

El sistema almacenará tanto el estado actual como el historial de los cambios realizados.

---

## 8. Prioridad de las órdenes

Cada orden tendrá un nivel de prioridad:

- BAJA.
- NORMAL.
- ALTA.
- URGENTE.

La prioridad permitirá organizar las reparaciones y determinar cuáles deben ser atendidas con mayor rapidez.

---

## 9. Requerimientos funcionales

### RF01 — Autenticación

El sistema deberá permitir que los usuarios registrados inicien sesión mediante correo electrónico y contraseña.

### RF02 — Control de acceso

El sistema deberá limitar las funcionalidades disponibles según el rol del usuario autenticado.

### RF03 — Gestión de clientes

El administrador deberá poder registrar, modificar, activar y desactivar clientes.

### RF04 — Gestión de técnicos

El administrador deberá poder registrar, modificar, activar y desactivar técnicos.

### RF05 — Gestión de equipos

El administrador deberá poder registrar equipos correspondientes a clientes existentes.

Cada equipo deberá contener como mínimo:

- Tipo.
- Marca.
- Modelo.
- Número de serie o identificador.
- Cliente propietario.

### RF06 — Historial de equipos

Un mismo equipo podrá poseer múltiples órdenes de reparación a lo largo del tiempo.

### RF07 — Creación de órdenes

El administrador deberá poder crear una orden asociada a un equipo existente.

### RF08 — Asignación de técnicos

El administrador deberá poder asignar o reasignar un técnico a una orden.

### RF09 — Diagnóstico

El técnico asignado deberá poder registrar y modificar el diagnóstico correspondiente a una reparación.

### RF10 — Tareas de reparación

El técnico deberá poder registrar una o más tareas realizadas sobre una orden.

### RF11 — Gestión de estados

El técnico y el administrador podrán actualizar el estado de una orden.

### RF12 — Historial de estados

Cada modificación de estado deberá almacenarse indicando:

- Estado anterior.
- Estado nuevo.
- Fecha y hora.
- Usuario responsable.

### RF13 — Notificaciones

Cuando se produzcan determinados cambios en una orden, el sistema deberá generar una notificación interna para el cliente.

### RF14 — Consulta del cliente

El cliente deberá poder visualizar solamente los equipos y órdenes que le pertenecen.

### RF15 — Filtros

El administrador deberá poder filtrar las órdenes según:

- Estado.
- Técnico.
- Cliente.
- Prioridad.

### RF16 — Fecha estimada

Las órdenes podrán contener una fecha estimada de finalización.

### RF17 — Baja lógica

Los clientes y técnicos no deberán eliminarse físicamente de la base de datos. El sistema utilizará estados activo/inactivo.

---

## 10. Requerimientos no funcionales

### RNF01 — Seguridad

Las contraseñas no deberán almacenarse en texto plano.

### RNF02 — Protección de credenciales

Las credenciales correspondientes a la base de datos y configuración sensible deberán almacenarse mediante variables de entorno.

### RNF03 — Validación

Los datos ingresados por los usuarios deberán ser validados antes de ser procesados.

### RNF04 — Sanitización

El sistema deberá aplicar controles sobre las entradas recibidas para reducir riesgos relacionados con datos maliciosos o inválidos.

### RNF05 — Usabilidad

La interfaz deberá ser clara, consistente y de fácil navegación.

### RNF06 — Persistencia

La información deberá almacenarse en una base de datos relacional MySQL.

### RNF07 — Mantenibilidad

El código deberá organizarse utilizando separación de responsabilidades y componentes independientes.

### RNF08 — Trazabilidad

Los cambios relevantes realizados sobre las órdenes deberán poder ser consultados posteriormente.

### RNF09 — Compatibilidad

La aplicación deberá poder utilizarse desde navegadores web modernos.

### RNF10 — Manejo de errores

El sistema deberá controlar errores y presentar mensajes comprensibles al usuario sin exponer información interna sensible.

---

## 11. Reglas de negocio

1. Un cliente puede tener uno o varios equipos.

2. Un equipo pertenece a un único cliente.

3. Un equipo puede poseer múltiples órdenes de reparación a lo largo de su vida útil.

4. Una orden pertenece a un único equipo.

5. Una orden puede estar asignada a un técnico por vez.

6. Un técnico puede tener múltiples órdenes asignadas simultáneamente.

7. Una orden puede ser reasignada por un administrador.

8. Solamente el administrador puede registrar inicialmente un equipo.

9. Los clientes no pueden modificar información técnica de una reparación.

10. Las órdenes finalizadas permanecen almacenadas para conservar el historial.

11. Los usuarios desactivados no podrán iniciar sesión.

12. Cuando una orden cambie a LISTO PARA RETIRAR, el cliente deberá recibir una notificación interna.

13. Una orden CANCELADA no podrá continuar el flujo normal de reparación.

14. Los tipos de equipos admitidos serán exclusivamente NOTEBOOK, CELULAR y TABLET.

---

## 12. Persistencia

FixDesk utilizará una base de datos relacional MySQL.

El acceso a los datos desde la aplicación Python será realizado mediante SQLAlchemy.

La información almacenada incluirá usuarios, clientes, técnicos, equipos, órdenes, diagnósticos, tareas, historial de estados y notificaciones.

La base de datos mantendrá las relaciones entre las diferentes entidades y garantizará la persistencia de la información incluso después de cerrar la aplicación.

---

## 13. Arquitectura propuesta

La aplicación será desarrollada utilizando una arquitectura basada en MVC, complementada con capas de servicio y repositorio.

La solución será dividida conceptualmente en:

- Modelo.
- Vista.
- Controlador.
- Servicios.
- Repositorios.
- Persistencia.

Esta separación permitirá mantener responsabilidades claras entre los diferentes componentes del sistema.

---

## 14. Tecnologías

Las tecnologías seleccionadas para el desarrollo serán:

- Python.
- Flask.
- Flask-SQLAlchemy.
- SQLAlchemy.
- PyMySQL.
- MySQL.
- HTML.
- CSS.
- Bootstrap.
- JavaScript.
- Jinja2.
- Git.
- GitHub.
- Postman.

Para la documentación de diagramas UML se utilizará PlantUML.

---

## 15. Tiempo estimado de desarrollo

El desarrollo completo del sistema se estima en aproximadamente seis semanas académicas, distribuidas entre:

- Análisis y relevamiento.
- Diseño del sistema.
- Diseño de base de datos.
- Desarrollo de la aplicación.
- Pruebas.
- Correcciones.
- Documentación.

---

## 16. Solución propuesta

FixDesk propone una solución web centralizada para administrar las diferentes etapas de una reparación técnica.

La solución permitirá que cada usuario acceda únicamente a las funciones correspondientes a su rol, manteniendo separados los procesos administrativos, técnicos y de consulta.

La utilización de una base de datos permitirá conservar el historial completo de clientes, equipos y reparaciones, aportando trazabilidad y evitando la pérdida de información.

El sistema también permitirá mejorar la comunicación con los clientes mediante la consulta del estado de sus reparaciones y la generación de notificaciones internas.

---

## 17. Resultado esperado

Al finalizar el desarrollo, FixDesk deberá permitir gestionar de forma completa el ciclo básico de una reparación:

**Recepción del equipo → Creación de orden → Asignación → Diagnóstico → Reparación → Equipo listo → Finalización.**

Toda la información relevante deberá quedar registrada y disponible según los permisos de cada usuario.