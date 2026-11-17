# Relevamiento de Requerimientos — FixDesk

## 1. Modalidad de relevamiento

Para definir los requerimientos de FixDesk se simuló una entrevista con el responsable de un pequeño servicio técnico dedicado a la reparación de notebooks, celulares y tablets.

El objetivo de la entrevista fue comprender cómo se administra actualmente el ingreso de equipos, la asignación de reparaciones, el trabajo de los técnicos y la comunicación con los clientes.

La entrevista permitió identificar problemas del proceso actual y convertirlos posteriormente en requerimientos funcionales y no funcionales del sistema.

---

## 2. Contexto de la entrevista

El cliente explicó que actualmente gran parte de la información de las reparaciones se administra mediante anotaciones, mensajes y registros separados.

Cada vez que ingresa un equipo se necesita registrar quién es su propietario, qué problema presenta, quién será responsable de repararlo y cuál es su estado actual.

Uno de los principales inconvenientes detectados es la dificultad para consultar rápidamente el historial de una reparación y comunicarle al cliente en qué etapa se encuentra su equipo.

---

## 3. Entrevista simulada

**Analista:** ¿Qué información necesitan registrar cuando reciben un equipo?

**Cliente:** Principalmente los datos del cliente, el tipo de equipo, la marca, el modelo, el número de serie cuando esté disponible y una descripción del problema informado.

---

**Analista:** ¿Qué tipos de equipos reciben habitualmente?

**Cliente:** Principalmente notebooks, celulares y tablets.

---

**Analista:** ¿Quién registra inicialmente el equipo?

**Cliente:** La persona encargada de administrar el servicio técnico cuando el cliente entrega físicamente el dispositivo.

---

**Analista:** ¿Qué sucede después de registrar el equipo?

**Cliente:** Se genera una orden de reparación y se asigna a un técnico para que pueda diagnosticarlo.

---

**Analista:** ¿Puede cambiar el técnico asignado?

**Cliente:** Sí. Puede suceder que un técnico no pueda continuar con la reparación o que sea necesario reasignar el trabajo.

---

**Analista:** ¿Qué información debería registrar el técnico?

**Cliente:** El diagnóstico del problema, las tareas realizadas y cualquier observación importante.

---

**Analista:** ¿Necesitan conocer el estado de cada reparación?

**Cliente:** Sí. Es fundamental saber si el equipo recién ingresó, está siendo diagnosticado, está en reparación o ya está listo para retirar.

---

**Analista:** ¿Cuáles serían los estados principales?

**Cliente:** Recibido, en diagnóstico, en reparación, listo para retirar y finalizado. También debería existir la posibilidad de cancelar una reparación.

---

**Analista:** ¿Necesitan conservar los cambios de estado anteriores?

**Cliente:** Sí. Nos interesa poder saber qué pasó con una reparación y cuándo cambió de estado.

---

**Analista:** ¿Los clientes deberían poder ingresar al sistema?

**Cliente:** Sí, pero solamente para consultar sus propios equipos, reparaciones y notificaciones. No deberían modificar información técnica.

---

**Analista:** ¿Qué debería ocurrir cuando un equipo está listo?

**Cliente:** El cliente debería recibir una notificación dentro del sistema indicando que su equipo se encuentra listo para retirar.

---

**Analista:** ¿El sistema debería manejar pagos o facturación?

**Cliente:** No es necesario para esta primera versión. Queremos enfocarnos en la gestión y seguimiento de las reparaciones.

---

**Analista:** ¿Los registros deberían eliminarse cuando un cliente deja de utilizar el servicio?

**Cliente:** Preferimos conservarlos para mantener el historial. Sería mejor poder desactivar usuarios o equipos sin eliminar la información.

---

**Analista:** ¿Necesitan establecer prioridades?

**Cliente:** Sí. Algunas reparaciones pueden ser normales y otras requieren atención más rápida.

---

**Analista:** ¿Sería útil disponer de una fecha estimada de finalización?

**Cliente:** Sí, porque permitiría organizar mejor el trabajo y brindar una referencia al cliente.

---

## 4. Requerimientos identificados

A partir de la entrevista se identificaron los siguientes requerimientos principales:

- Existencia de tres roles: administrador, técnico y cliente.
- Registro de clientes.
- Registro de equipos.
- Soporte para notebook, celular y tablet.
- Creación de órdenes de reparación.
- Asignación y reasignación de técnicos.
- Registro de diagnósticos.
- Registro de tareas realizadas.
- Manejo de prioridades.
- Manejo de estados.
- Historial de cambios de estado.
- Notificaciones internas.
- Consulta de reparaciones por parte del cliente.
- Fecha estimada de finalización.
- Baja lógica de usuarios y equipos.
- Restricción de acceso según rol.
- Persistencia de la información en una base de datos.

---

## 5. Requerimientos descartados para esta versión

Durante el relevamiento también se determinaron funcionalidades que podrían formar parte de futuras versiones pero que no estarán incluidas inicialmente:

- Facturación.
- Gestión de pagos.
- Caja.
- Stock de repuestos.
- Gestión de proveedores.
- Compras.
- Reserva de turnos.
- Chat en tiempo real.

Estas funcionalidades fueron descartadas para mantener el alcance del sistema enfocado específicamente en la gestión del proceso de reparación.

---

## 6. Resultado del relevamiento

El relevamiento permitió determinar que la principal necesidad del cliente es disponer de un sistema centralizado que permita conocer en todo momento:

- Qué equipo ingresó.
- A qué cliente pertenece.
- Qué problema presenta.
- Qué técnico lo tiene asignado.
- Qué diagnóstico posee.
- Qué tareas fueron realizadas.
- En qué estado se encuentra.
- Qué cambios atravesó durante la reparación.

A partir de estos requerimientos se definió el alcance funcional de FixDesk y se desarrollaron los modelos UML y el diseño de persistencia correspondientes.