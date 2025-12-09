
# Guía de Configuración de DoorDuino en Windows (Sin Arduino)

Esta guía explica cómo instalar, configurar y ejecutar completamente el backend del proyecto DoorDuino en **Windows 10 o Windows 11**, incluso si no tienes hardware Arduino.  
Incluye instrucciones para instalar Git, Python, PostgreSQL, clonar el repositorio, configurar un entorno virtual, ejecutar el colector en modo de simulación y lanzar el servidor web Flask.

---

# 🧰 1. Instalar las Herramientas Necesarias

Necesitarás:

- Git para Windows  
- Python 3.x  
- PostgreSQL 14+  
- (Opcional) Visual Studio Code  

---

# 🧩 1.1 Instalar Git para Windows

Descargar Git:

👉 https://git-scm.com/download/win

Ejecutar el instalador con las **configuraciones recomendadas por defecto**.

Verificar instalación:

```cmd
git --version
```

---

# 🐍 1.2 Instalar Python 3

Descargar Python:

👉 https://www.python.org/downloads/windows/

Durante la instalación:

✔️ **Marcar la opción "Add Python to PATH"**

Luego seleccionar:

- Customize Installation → Activar todas las características → Install

Verificar:

```cmd
python --version
```

---

# 🗄️ 1.3 Instalar PostgreSQL para Windows

Descargar PostgreSQL:

👉 https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

Pasos del instalador:

- Seleccionar versión reciente o 14.x  
- Mantener todas las opciones por defecto  
- Elegir una contraseña para el usuario administrativo `postgres`  
- Instalar pgAdmin (por defecto)

Confirmar que PostgreSQL esté corriendo:

1. Presionar **Win + R**  
2. Escribir:

```
services.msc
```

3. Buscar:

```
postgresql-x64-14
```

El estado debe ser **Running**.

---

# 📂 2. Clonar el Repositorio DoorDuino

Abrir Command Prompt, PowerShell o Git Bash.

Elegir una carpeta (ejemplo: Escritorio):

```cmd
cd %USERPROFILE%\Desktop
```

Clonar el repositorio (HTTPS recomendado):

```cmd
git clone https://github.com/<tu-usuario>/DoorDuino.git
cd DoorDuino
```

---

# 🐍 3. Crear un Entorno Virtual de Python

Dentro de la carpeta del proyecto:

```cmd
python -m venv .venv
```

Activar el entorno:

### En Command Prompt:
```cmd
.venv\Scripts\activate
```

### En PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea el script:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```

Luego activar nuevamente.

El prompt debe mostrar:

```
(.venv)
```

---

# 📦 4. Instalar Dependencias de Python

```cmd
pip install -r backend\requirements.txt
```

---

# 🗄️ 5. Crear la Base de Datos PostgreSQL

---

## Opción A — Usar pgAdmin (Interfaz Gráfica)

1. Abrir **pgAdmin**
2. Conectarse al servidor PostgreSQL
3. Crear una nueva base de datos:
   - Clic derecho en **Databases**
   - **Create → Database**
   - Nombre: `doorlog`
4. Abrir **Tools → Query Tool**
5. Ejecutar:

```sql
CREATE USER dooruser WITH PASSWORD 'doorpassword';
GRANT ALL PRIVILEGES ON DATABASE doorlog TO dooruser;
```

6. Conectarse a `doorlog` en pgAdmin
7. Crear la tabla:

```sql
CREATE TABLE IF NOT EXISTS door_events (
    id SERIAL PRIMARY KEY,
    event_time TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    state VARCHAR(10) NOT NULL CHECK (state IN ('OPEN', 'CLOSED')),
    source VARCHAR(50)
);
```

---

## Opción B — Usar psql (Línea de Comando)

```cmd
psql -U postgres
```

Ingresar contraseña.

Dentro de psql:

```sql
CREATE DATABASE doorlog;
CREATE USER dooruser WITH PASSWORD 'doorpassword';
GRANT ALL PRIVILEGES ON DATABASE doorlog TO dooruser;
\q
```

Aplicar el esquema:

```cmd
psql -U dooruser -d doorlog -f db\init.sql
```

---

# 🔌 6. Ejecutar el Colector (Simulación de Arduino)

No se requiere Arduino — solo escribir eventos a mano.

Dentro del entorno virtual activado:

```cmd
cd backend
python collector.py
```

Verás:

```
Collector running. Type OPEN or CLOSED and press Enter.
Press CTRL + C to exit.
```

Simular eventos:

```
OPEN
CLOSED
OPEN
```

Cada evento se guarda en PostgreSQL.

---

# 🧪 7. Verificar Eventos Registrados

---

## Opción A — Usando pgAdmin

1. Expandir base de datos `doorlog`  
2. Ir a **Schemas → Tables → door_events**  
3. Clic derecho → **View/Edit Data → All Rows**

---

## Opción B — Usando psql

```cmd
psql -U dooruser -d doorlog
SELECT * FROM door_events ORDER BY event_time DESC;
\q
```

---

# 🌐 8. Ejecutar el Servidor Web Flask

Abrir una nueva terminal:

```cmd
cd DoorDuino
.venv\Scripts\activate
cd backend
python server.py
```

Verás:

```
 * Running on http://127.0.0.1:5000
```

Abrir en el navegador:

👉 http://127.0.0.1:5000/

---

# 🛑 9. Detener los Programas

Detener el colector:

```
CTRL + C
```

Detener Flask:

```
CTRL + C
```

Detener PostgreSQL (opcional):

1. Win + R  
2. `services.msc`  
3. Buscar: `postgresql-x64-14`  
4. Clic derecho → Stop  

---

# ❗ 10. Problemas Comunes y Soluciones

### ❌ "python not recognized"
Solución: reinstalar Python y marcar **Add Python to PATH**.

---

### ❌ PowerShell no permite activar el entorno virtual

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```

---

### ❌ Flask no puede conectar a la base de datos
Comprobar que PostgreSQL esté corriendo:

1. Win + R  
2. `services.msc`  
3. Iniciar: `postgresql-x64-14`

---

### ❌ collector.py congela la terminal

```
CTRL + C
```

Si no responde:

```
CTRL + Z
taskkill /IM python.exe /F
```

---

# 🎉 ¡Éxito!

Ahora has logrado:

- Instalar Git, Python y PostgreSQL en Windows  
- Clonar el repositorio DoorDuino  
- Configurar un entorno virtual  
- Crear la base de datos y tabla  
- Simular eventos de puerta  
- Verlos en el panel web Flask  

Todo **sin necesidad de Arduino**.

Si deseas combinar las guías macOS + Windows en un README bilingüe o exportarlo a PDF, solo dímelo.

