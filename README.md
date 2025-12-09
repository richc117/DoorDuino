
# DoorDuino

DoorDuino is a simple backend prototype that simulates monitoring door open/close events using Python, PostgreSQL, and Flask — **no Arduino hardware required**.  
This project includes a simulated collector, a PostgreSQL database, and a web dashboard to visualize door activity.

## 📘 How to Run This Project (Complete Guide)

These instructions allow **anyone** to clone and run this project from scratch.

---

# 🧰 1. Install Required Tools

### 1.1 Install Homebrew (macOS)

Homebrew lets you install PostgreSQL, Python, Git, and more.

```bash
/bin/bash -c "$(curl -fsSL httpsraw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then run the commands Homebrew prints, typically:

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

Verify:

```bash
brew --version
```

---

### 1.2 Install Git, Python, PostgreSQL

```bash
brew install git python postgresql@14
brew services start postgresql@14
```

Verify PostgreSQL is running:

```bash
brew services list
```

---

# 📂 2. Clone the Repository

```bash
cd ~/Developer
git clone https://github.com/<your-username>/DoorDuino.git
cd DoorDuino
```

---

# 🐍 3. Create and Activate the Python Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

# 📦 4. Install Python Dependencies

```bash
pip install -r backend/requirements.txt
```

---

# 🗄️ 5. Create the PostgreSQL Database

Enter PostgreSQL:

```bash
psql -d postgres
```

Run:

```sql
CREATE DATABASE doorlog;
CREATE USER dooruser WITH PASSWORD 'doorpassword';
GRANT ALL PRIVILEGES ON DATABASE doorlog TO dooruser;
\q
```

---

# 📜 6. Apply the Database Schema

```bash
psql -d doorlog -U dooruser -f db/init.sql
```

This creates the `door_events` table.

---

# 🔌 7. Run the Collector (Simulated Arduino)

```bash
cd backend
python collector.py
```

You will see:

```
Collector running. Type OPEN or CLOSED and press Enter.
Press CTRL + C to exit.
```

Type:

```
OPEN
CLOSED
OPEN
```

Each event logs to the database.

---

# 🧪 8. Verify Events in PostgreSQL

```bash
psql -d doorlog -U dooruser
SELECT * FROM door_events ORDER BY event_time DESC;
\q
```

---

# 🌐 9. Run the Flask Web Dashboard

Open a new Terminal window:

```bash
cd ~/Developer/DoorDuino
source .venv/bin/activate
cd backend
python server.py
```

Visit:

👉 http://127.0.0.1:5000/

You will see a table of recent door events.

---

# 🛑 10. Stopping Everything

Stop collector:

```
CTRL + C
```

Stop Flask:

```
CTRL + C
```

Stop PostgreSQL (optional):

```bash
brew services stop postgresql@14
```

---

# ❗ Troubleshooting

### PostgreSQL won’t start
```bash
brew services cleanup
brew services start postgresql@14
```

### collector.py frozen
```bash
CTRL + C
CTRL + Z
kill %1
```

### Flask cannot connect to DB
- Ensure PostgreSQL is running
- Check DB credentials in `collector.py` and `server.py`

---

# 🎉 You're Done!

You now have:
- A running PostgreSQL database  
- A simulated Arduino collector  
- A working Flask dashboard  

All running locally with no hardware required.

---

If you'd like a version with a project diagram, shields.io badges, or GitHub formatting enhancements, just ask!
