from flask import Flask, jsonify, render_template
import psycopg2
import psycopg2.extras

DB_DSN = "dbname=doorlog user=dooruser password=doorpassword host=localhost"

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(DB_DSN)

@app.route("/api/events")
def api_events():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("""
        SELECT id, event_time, state, source
        FROM door_events
        ORDER BY event_time DESC
        LIMIT 100;
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    events = [
        {
            "id": r["id"],
            "event_time": r["event_time"].isoformat(),
            "state": r["state"],
            "source": r["source"],
        }
        for r in rows
    ]
    return jsonify(events)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)