# Persistencia de Datos — FixDesk

## 1. Tecnología seleccionada

FixDesk utilizará una base de datos relacional **MySQL** como mecanismo principal de persistencia.

La comunicación entre la aplicación desarrollada en Python y la base de datos se realizará utilizando:

- SQLAlchemy.
- Flask-SQLAlchemy.
- PyMySQL.

La base de datos utilizada por el sistema se denominará:

**fixdesk_db**

---

## 2. Tipo de persistencia

El sistema implementará persistencia relacional.

La información será almacenada en tablas relacionadas mediante claves primarias y claves foráneas.

Los principales datos persistidos serán:

- Usuarios.
- Clientes.
- Técnicos.
- Equipos.
- Órdenes de reparación.
- Diagnósticos.
- Tareas de reparación.
- Historial de estados.
- Notificaciones.

---

## 3. Estrategia de acceso a datos

FixDesk utilizará una capa Repository para centralizar las operaciones relacionadas con la persistencia.

Los controladores no accederán directamente a MySQL.

El flujo de acceso será:

**Controller → Service → Repository → SQLAlchemy → MySQL**

Esta separación evita mezclar la lógica de negocio con las operaciones de acceso a datos.

---

## 4. ORM

Se utilizará SQLAlchemy como ORM (Object Relational Mapping).

Las entidades del dominio serán representadas mediante clases Python que posteriormente serán vinculadas con las tablas correspondientes de MySQL.

Esto permitirá realizar operaciones sobre entidades utilizando objetos de Python sin escribir consultas SQL manuales para cada operación básica.

---

## 5. Relaciones principales

La base de datos almacenará las siguientes relaciones principales:

- Un cliente puede poseer múltiples equipos.
- Un equipo pertenece a un único cliente.
- Un equipo puede tener múltiples órdenes de reparación.
- Una orden puede estar asignada a un técnico.
- Un técnico puede tener múltiples órdenes.
- Una orden puede contener un diagnóstico.
- Una orden puede contener múltiples tareas.
- Una orden mantiene múltiples registros de historial.
- Un cliente puede recibir múltiples notificaciones.
- Una orden puede generar múltiples notificaciones.

---

## 6. Integridad de datos

La integridad será controlada mediante:

- Claves primarias.
- Claves foráneas.
- Restricciones de unicidad.
- Validaciones de datos.
- Relaciones entre entidades.

El correo electrónico de cada usuario deberá ser único.

El diagnóstico estará asociado a una única orden de reparación.

---

## 7. Baja lógica

FixDesk evitará eliminar físicamente determinados registros que posean información histórica.

Los usuarios, clientes, técnicos y equipos utilizarán un indicador de estado activo/inactivo.

De esta manera será posible conservar la trazabilidad de reparaciones anteriores aunque un usuario deje de utilizar el sistema.

---

## 8. Seguridad de conexión

Los datos sensibles de conexión no estarán escritos directamente dentro del código fuente.

Se utilizará un archivo de variables de entorno `.env` para almacenar:

- Host.
- Puerto.
- Nombre de la base.
- Usuario.
- Contraseña.
- Clave secreta de la aplicación.

El archivo `.env` será excluido del repositorio mediante `.gitignore`.

Se proporcionará un archivo `.env.example` sin credenciales reales para documentar la configuración necesaria.

---

## 9. Respaldo y portabilidad

La estructura de la base de datos podrá exportarse mediante un archivo SQL.

En la entrega del sistema se incluirá el archivo correspondiente a la base de datos para permitir su reconstrucción en otro entorno MySQL.

---

## 10. Conclusión

La utilización de MySQL junto con SQLAlchemy permitirá que FixDesk disponga de una persistencia estructurada y consistente.

La separación mediante repositorios permitirá mantener desacoplada la lógica de negocio del mecanismo específico de almacenamiento, facilitando el mantenimiento y futuras modificaciones.