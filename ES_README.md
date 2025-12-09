
# DoorDuino — Guía de Configuración (macOS)

DoorDuino es un prototipo backend simple que simula el monitoreo de eventos de apertura/cierre de una puerta usando Python, PostgreSQL y Flask — **sin necesidad de hardware Arduino**.  
Este proyecto incluye un colector simulado, una base de datos PostgreSQL y un panel web para visualizar la actividad de la puerta.

Estructura del proyecto:

```
door-monitor/
├── README.md
├── .gitignore
├── arduino/
│   └── door_sensor.ino
├── backend/
│   ├── collector.py        # lee del puerto serial del Arduino y escribe en Postgres
│   ├── server.py           # servidor web Flask
│   ├── requirements.txt    # dependencias de Python
│   └── templates/
│       └── index.html      # interfaz web
└── db/
    └── init.sql            # SQL para crear tabla(s)
```

---

## 📘 Cómo Ejecutar Este Proyecto (Guía Completa)

Estas instrucciones permiten que **cualquier persona** clone y ejecute el proyecto desde cero.

---

# 🧰 1. Instalar las Herramientas Necesarias

### 1.1 Instalar Homebrew (macOS)

Homebrew permite instalar PostgreSQL, Python, Git y más.

```bash
/bin/bash -c "$(curl -fsSL httpsraw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Luego ejecutar los comandos que Homebrew indique, típicamente:

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

Verificar:

```bash
brew --version
```

---

### 1.2 Instalar Git, Python y PostgreSQL

```bash
brew install git python postgresql@14
brew services start postgresql@14
```

Verificar que PostgreSQL esté activo:

```bash
brew services list
```

---

# 📂 2. Clonar el Repositorio

```bash
cd ~/Developer
git clone https://github.com/<tu-usuario>/DoorDuino.git
cd DoorDuino
```

---

# 🐍 3. Crear y Activar el Entorno Virtual de Python

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

# 📦 4. Instalar Dependencias de Python

```bash
pip install -r backend/requirements.txt
```

---

# 🗄️ 5. Crear la Base de Datos PostgreSQL

Ingresar a PostgreSQL:

```bash
psql -d postgres
```

Ejecutar:

```sql
CREATE DATABASE doorlog;
CREATE USER dooruser WITH PASSWORD 'doorpassword';
GRANT ALL PRIVILEGES ON DATABASE doorlog TO dooruser;
\q
```

---

# 📜 6. Aplicar el Esquema de Base de Datos

```bash
psql -d doorlog -U dooruser -f db/init.sql
```

Esto crea la tabla `door_events`.

---

# 🔌 7. Ejecutar el Colector (Simulación de Arduino)

```bash
cd backend
python collector.py
```

Verás:

```
Collector running. Type OPEN or CLOSED and press Enter.
Press CTRL + C to exit.
```

Escribe:

```
OPEN
CLOSED
OPEN
```

Cada evento se registra en la base de datos.

---

# 🧪 8. Verificar los Eventos en PostgreSQL

```bash
psql -d doorlog -U dooruser
SELECT * FROM door_events ORDER BY event_time DESC;
\q
```

---

# 🌐 9. Ejecutar el Panel Web con Flask

Abrir una nueva ventana de Terminal:

```bash
cd ~/Developer/DoorDuino
source .venv/bin/activate
cd backend
python server.py
```

Visitar:

👉 http://127.0.0.1:5000/

Verás una tabla con los eventos recientes.

---

# 🛑 10. Detener Todo

Detener el colector:

```
CTRL + C
```

Detener Flask:

```
CTRL + C
```

Detener PostgreSQL (opcional):

```bash
brew services stop postgresql@14
```

---

# ❗ Solución de Problemas

### PostgreSQL no inicia
```bash
brew services cleanup
brew services start postgresql@14
```

### collector.py se congela
```bash
CTRL + C
CTRL + Z
kill %1
```

### Flask no puede conectar a la BD
- Confirmar que PostgreSQL esté corriendo
- Revisar credenciales en `collector.py` y `server.py`

---

# 🎉 ¡Listo!

Ahora tienes:
- Una base de datos PostgreSQL funcionando  
- Un colector simulado  
- Un panel web Flask operativo  

Todo sin hardware adicional.

---

Si deseas una versión con diagramas, badges de GitHub o una guía combinada para macOS y Windows, solo dímelo.
