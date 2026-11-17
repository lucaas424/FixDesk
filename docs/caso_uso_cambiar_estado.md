# Caso de Uso: Cambiar estado de reparación

## 1. Identificación

**Nombre:** Cambiar estado de reparación  
**Código:** CU-01  
**Sistema:** FixDesk  
**Actor principal:** Técnico  
**Actor secundario:** Administrador  
**Objetivo:** Modificar el estado actual de una orden de reparación y registrar la modificación realizada.

---

## 2. Precondiciones

- El usuario debe haber iniciado sesión.
- El usuario debe poseer permisos para modificar el estado de una orden.
- La orden de reparación debe existir.
- La orden no debe encontrarse en estado FINALIZADO o CANCELADO.
- En el caso del técnico, la orden debe estar asignada a dicho técnico.

---

## 3. Postcondiciones

- El nuevo estado queda almacenado en la orden.
- Se registra el cambio en el historial de estados.
- Se almacena la fecha y hora de la modificación.
- Se registra el usuario responsable del cambio.
- Cuando corresponda, se genera una notificación interna para el cliente.

---

## 4. Curso normal

1. El técnico inicia sesión en FixDesk.

2. El sistema valida las credenciales y muestra el panel correspondiente al técnico.

3. El técnico accede a la sección **Órdenes asignadas**.

4. El sistema muestra las órdenes de reparación asignadas al técnico.

5. El técnico selecciona una orden.

6. El sistema muestra la información de la orden:
   - Equipo.
   - Cliente.
   - Problema reportado.
   - Prioridad.
   - Estado actual.
   - Diagnóstico.
   - Tareas registradas.
   - Historial de estados.

7. El técnico selecciona la opción **Cambiar estado**.

8. El sistema muestra los estados disponibles según el estado actual de la orden.

9. El técnico selecciona el nuevo estado.

10. El técnico confirma la operación.

11. El sistema valida que la transición de estado sea permitida.

12. El sistema actualiza el estado actual de la orden.

13. El sistema crea un nuevo registro en el historial indicando:
    - Estado anterior.
    - Estado nuevo.
    - Fecha y hora.
    - Usuario responsable.

14. Si el nuevo estado requiere informar al cliente, el sistema genera automáticamente una notificación interna.

15. El sistema confirma que el estado fue actualizado correctamente.

16. El técnico visualiza la orden con su nuevo estado.

---

## 5. Curso alternativo A — Transición de estado no permitida

**Comienza en el paso 11 del curso normal.**

11A. El sistema detecta que la transición solicitada no está permitida.

12A. El sistema no modifica la orden.

13A. El sistema informa al técnico que no es posible realizar el cambio seleccionado.

14A. El sistema mantiene el estado anterior.

15A. El técnico puede seleccionar otro estado válido o cancelar la operación.

---

## 6. Curso alternativo B — Orden finalizada o cancelada

**Comienza en el paso 5 del curso normal.**

5B. El técnico selecciona una orden cuyo estado es FINALIZADO o CANCELADO.

6B. El sistema muestra la información de la orden en modo de consulta.

7B. La opción para cambiar el estado se encuentra deshabilitada.

8B. El sistema informa que la orden no admite nuevos cambios de estado.

9B. Finaliza el caso de uso sin realizar modificaciones.

---

## 7. Curso alternativo C — Técnico no autorizado

**Comienza al intentar acceder a una orden.**

1C. El técnico intenta acceder a una orden que no se encuentra asignada a su usuario.

2C. El sistema verifica que el técnico no posee autorización sobre la orden.

3C. El sistema rechaza la operación.

4C. El sistema muestra un mensaje indicando que el usuario no posee permisos suficientes.

5C. No se modifica ningún dato.

---

## 8. Regla especial de notificación

Cuando el estado de una orden cambie a:

**LISTO PARA RETIRAR**

el sistema generará automáticamente una notificación para el cliente propietario del equipo.

Ejemplo:

**“Tu equipo ya se encuentra listo para retirar.”**