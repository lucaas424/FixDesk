# FixDesk

FixDesk es un sistema web de gestión de servicio técnico de equipos informáticos desarrollado como proyecto académico.

La aplicación permite administrar clientes, técnicos, equipos y órdenes de reparación, realizando el seguimiento completo del proceso desde la recepción del equipo hasta la finalización de la reparación.

## Funcionalidades principales

El sistema trabaja con tres roles de usuario:

### Administrador

El administrador puede:

- Consultar todas las órdenes de reparación.
- Crear nuevas órdenes.
- Registrar clientes.
- Registrar técnicos.
- Registrar equipos y asociarlos a un cliente.
- Consultar clientes, técnicos y equipos.
- Asignar o reasignar técnicos a las órdenes.
- Modificar la prioridad de una orden.
- Consultar el estado general de las reparaciones.

### Técnico

El técnico puede:

- Consultar únicamente las órdenes que tiene asignadas.
- Ver el detalle de cada reparación.
- Cambiar el estado de una orden según las transiciones permitidas.
- Registrar y actualizar el diagnóstico técnico.
- Registrar las tareas realizadas durante la reparación.
- Consultar el historial de estados de la orden.

El flujo normal de una orden es:

```text
RECIBIDO
   ↓
EN_DIAGNOSTICO
   ↓
EN_REPARACION
   ↓
LISTO_PARA_RETIRAR
   ↓
FINALIZADO
```

También existe el estado `CANCELADO` cuando corresponde.

Una orden finalizada o cancelada ya no admite modificaciones técnicas.

### Cliente

El cliente puede:

- Consultar sus equipos registrados.
- Consultar sus reparaciones.
- Ver el detalle y seguimiento de sus órdenes.
- Consultar el diagnóstico técnico.
- Consultar las tareas realizadas.
- Consultar el historial de estados.
- Recibir notificaciones cuando un equipo queda listo para retirar.
- Marcar las notificaciones como leídas.

Los clientes solo pueden acceder a información correspondiente a sus propios equipos y reparaciones.

## Arquitectura

El proyecto utiliza una arquitectura organizada por capas:

```text
Controllers
    ↓
Services
    ↓
Repositories
    ↓
Models
    ↓
MySQL
```

### Controllers

Gestionan las solicitudes HTTP, validan el acceso según el rol del usuario y coordinan la interacción entre la interfaz y los servicios.

### Services

Contienen las reglas de negocio del sistema, como:

- Creación de órdenes.
- Validación de transiciones de estado.
- Asignación de técnicos.
- Gestión de prioridades.
- Registro de diagnósticos.
- Registro de tareas.
- Gestión administrativa.

### Repositories

Encapsulan el acceso y persistencia de datos utilizando SQLAlchemy.

### Models

Representan las entidades principales del dominio:

- Usuario
- Cliente
- Técnico
- Administrador
- Equipo
- Orden de reparación
- Diagnóstico
- Tarea de reparación
- Historial de estados
- Notificación

## Patrones de diseño

El proyecto implementa patrones de diseño para resolver responsabilidades específicas.

### Strategy

Se utiliza el patrón Strategy para el manejo de las prioridades de las órdenes:

- BAJA
- NORMAL
- ALTA
- URGENTE

Cada prioridad posee una estrategia específica.

### Observer

Se utiliza el patrón Observer para generar notificaciones cuando una orden alcanza un estado relevante.

Por ejemplo, cuando una reparación pasa a `LISTO_PARA_RETIRAR`, el sistema genera una notificación para el cliente correspondiente.

## Tecnologías utilizadas

- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy
- Flask-WTF
- SQLAlchemy
- MySQL
- PyMySQL
- Jinja2
- HTML
- CSS
- Git
- GitHub
- PlantUML

## Estructura general del proyecto

```text
FixDesk/
│
├── app/
│   ├── controllers/
│   ├── models/
│   ├── patterns/
│   ├── repositories/
│   ├── services/
│   ├── static/
│   ├── templates/
│   ├── utils/
│   ├── __init__.py
│   └── extensions.py
│
├── database/
│   └── fixdesk_db.sql
│
├── docs/
│   └── uml/
│
├── .env.example
├── .gitignore
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/lucaas424/FixDesk.git
cd FixDesk
```

### 2. Crear un entorno virtual

En Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Configuración de MySQL

El proyecto utiliza MySQL como sistema gestor de base de datos.

En la carpeta:

```text
database/
```

se encuentra el archivo:

```text
fixdesk_db.sql
```

Este archivo contiene el backup de la base de datos utilizado por la aplicación.

Puede importarse utilizando MySQL Workbench o mediante la terminal de MySQL.

## Variables de entorno

Crear un archivo `.env` en la raíz del proyecto tomando como referencia `.env.example`.

Ejemplo:

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=fixdesk_db
DB_USER=root
DB_PASSWORD=tu_password_mysql
SECRET_KEY=tu_secret_key
```

Las credenciales reales no se almacenan en GitHub.

## Ejecutar la aplicación

Con el entorno virtual activado:

```bash
python run.py
```

Luego acceder desde el navegador a:

```text
http://127.0.0.1:5000
```

## Seguridad y control de acceso

FixDesk implementa autenticación mediante Flask-Login.

El sistema diferencia permisos según el rol:

- ADMINISTRADOR
- TECNICO
- CLIENTE

Las rutas sensibles están protegidas y el sistema valida que cada usuario pueda acceder únicamente a las operaciones autorizadas para su rol.

También se utiliza protección CSRF en los formularios mediante Flask-WTF.

Las contraseñas no se almacenan en texto plano.

## Reglas de negocio principales

Entre las reglas implementadas se encuentran:

- Solo un administrador puede realizar operaciones administrativas.
- Solo los técnicos pueden modificar el proceso técnico de una reparación.
- Un técnico solo puede trabajar sobre órdenes que tenga asignadas.
- Un cliente no puede modificar órdenes.
- Un cliente solo puede acceder a sus propios equipos y reparaciones.
- Las transiciones de estado deben respetar el flujo definido.
- Las órdenes finalizadas o canceladas quedan cerradas.
- No pueden registrarse diagnósticos o tareas en una orden cerrada.
- Los números de serie de los equipos no pueden duplicarse.
- Los correos electrónicos de los usuarios no pueden duplicarse.

## Documentación UML

La carpeta:

```text
docs/uml/
```

contiene los diagramas utilizados para documentar el sistema, incluyendo diagramas relacionados con el caso de uso de gestión de órdenes y el flujo de secuencia.

## Base de datos

Las principales tablas utilizadas son:

- `usuario`
- `equipo`
- `orden_reparacion`
- `diagnostico`
- `tarea_reparacion`
- `historial_estado`
- `notificacion`

La persistencia se gestiona mediante SQLAlchemy sobre una base de datos MySQL.

## Estado del proyecto

El sistema permite completar el ciclo principal de servicio técnico:

```text
Registro de cliente
        ↓
Registro de equipo
        ↓
Creación de orden
        ↓
Asignación de técnico
        ↓
Diagnóstico
        ↓
Reparación y tareas
        ↓
Equipo listo para retirar
        ↓
Notificación al cliente
        ↓
Finalización de la orden
```

El proyecto incluye control de acceso por roles, persistencia en base de datos, historial de estados, notificaciones y reglas de negocio para proteger la integridad del flujo de reparación.