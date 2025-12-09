
# DoorDuino Windows Setup Guide (No Arduino Required)

This guide explains how to fully install, configure, and run the DoorDuino backend project on **Windows 10 or Windows 11**—even if you do not have Arduino hardware.  
It includes instructions for installing Git, Python, PostgreSQL, cloning the repository, setting up a virtual environment, running the collector in simulation mode, and launching the Flask web server.

---

# 🧰 1. Install Required Tools

You will need:

- Git for Windows
- Python 3.x
- PostgreSQL 14+
- (Optional) Visual Studio Code

---

# 🧩 1.1 Install Git for Windows

Download Git:

👉 https://git-scm.com/download/win

Run the installer using the **default recommended settings**.

Verify the installation:

```cmd
git --version
```

---

# 🐍 1.2 Install Python 3

Download Python:

👉 https://www.python.org/downloads/windows/

During installation:

✔️ **Check "Add Python to PATH"**

Then select:

- Customize Installation → Enable all optional features → Install

Verify:

```cmd
python --version
```

---

# 🗄️ 1.3 Install PostgreSQL for Windows

Download PostgreSQL:

👉 https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

Installer steps:

- Select latest version or 14.x  
- Keep all defaults  
- Set a password for the `postgres` administrative user  
- Install pgAdmin (default)

Check PostgreSQL is running:

1. Press **Win + R**
2. Type:

```
services.msc
```

3. Look for:

```
postgresql-x64-14
```

Status should be **Running**.

---

# 📂 2. Clone the DoorDuino Repository

Open Command Prompt, PowerShell, or Git Bash.

Choose a folder (example: Desktop):

```cmd
cd %USERPROFILE%\Desktop
```

Clone the repository (HTTPS preferred for beginners):

```cmd
git clone https://github.com/<your-username>/DoorDuino.git
cd DoorDuino
```

---

# 🐍 3. Create a Python Virtual Environment

Inside the project folder:

```cmd
python -m venv .venv
```

Activate it:

### Command Prompt:
```cmd
.venv\Scripts\activate
```

### PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks it:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```

Then activate again.

You should now see:

```
(.venv)
```

---

# 📦 4. Install Python Dependencies

```cmd
pip install -r backend\requirements.txt
```

---

# 🗄️ 5. Create the PostgreSQL Database

---

## Option A — Use pgAdmin (Graphical Interface)

1. Open **pgAdmin**
2. Connect to your PostgreSQL server
3. Create a new database:
   - Right-click **Databases**
   - Select **Create → Database**
   - Name: `doorlog`
4. Open **Tools → Query Tool**
5. Run:

```sql
CREATE USER dooruser WITH PASSWORD 'doorpassword';
GRANT ALL PRIVILEGES ON DATABASE doorlog TO dooruser;
```

6. Connect pgAdmin to `doorlog`
7. Create the table:

```sql
CREATE TABLE IF NOT EXISTS door_events (
    id SERIAL PRIMARY KEY,
    event_time TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    state VARCHAR(10) NOT NULL CHECK (state IN ('OPEN', 'CLOSED')),
    source VARCHAR(50)
);
```

---

## Option B — Use psql (Command Line)

```cmd
psql -U postgres
```

Enter your postgres password.

Inside psql:

```sql
CREATE DATABASE doorlog;
CREATE USER dooruser WITH PASSWORD 'doorpassword';
GRANT ALL PRIVILEGES ON DATABASE doorlog TO dooruser;
\q
```

Apply the schema:

```cmd
psql -U dooruser -d doorlog -f db\init.sql
```

---

# 🔌 6. Run the Collector (Simulated Arduino)

No Arduino required — just type events manually.

From inside the activated virtual environment:

```cmd
cd backend
python collector.py
```

You should see:

```
Collector running. Type OPEN or CLOSED and press Enter.
Press CTRL + C to exit.
```

Simulate events:

```
OPEN
CLOSED
OPEN
```

Each event will be written into PostgreSQL.

---

# 🧪 7. Verify Events Are Logged

---

## Option A — Using pgAdmin

1. Expand `doorlog` database  
2. Select **Schemas → Tables → door_events**  
3. Right-click → **View/Edit Data → All Rows**

You should see logged entries.

---

## Option B — Using psql

```cmd
psql -U dooruser -d doorlog
SELECT * FROM door_events ORDER BY event_time DESC;
\q
```

---

# 🌐 8. Run the Flask Web Dashboard

Open a new terminal window:

```cmd
cd DoorDuino
.venv\Scripts\activate
cd backend
python server.py
```

Output will show:

```
 * Running on http://127.0.0.1:5000
```

Open that URL in your browser.

You should see a dashboard displaying your door event history.

---

# 🛑 9. Stopping the Programs

Stop Collector:

```
CTRL + C
```

Stop Flask:

```
CTRL + C
```

Stop PostgreSQL (optional):

1. Press Win + R  
2. Type: `services.msc`  
3. Find `postgresql-x64-14`  
4. Right-click → Stop  

---

# ❗ 10. Troubleshooting for Windows

---

### ❌ "python not recognized"
You forgot to check **Add Python to PATH** during installation.  
Reinstall Python.

---

### ❌ Virtual environment will not activate in PowerShell

Run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```

---

### ❌ Flask cannot connect to the database
Ensure PostgreSQL is running:

1. **Win + R**
2. Type `services.msc`
3. Start:  
   `postgresql-x64-14`

---

### ❌ collector.py freezes the terminal
Try:

```
CTRL + C
```

If unresponsive:

```
CTRL + Z
taskkill /IM python.exe /F
```

---

# 🎉 Success!

You have now successfully:

- Installed Git, Python, and PostgreSQL on Windows  
- Cloned the DoorDuino repository  
- Set up a virtual environment  
- Created the database and table  
- Simulated door events  
- Viewed them on a Flask dashboard  

All **with no Arduino hardware required**.

If you'd like a macOS + Linux + Windows unified README, or a PDF version of this guide, just ask!
