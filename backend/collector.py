
import psycopg2
import sys

DB_DSN = "dbname=doorlog user=dooruser password=doorpassword host=localhost"

def main():
    conn = psycopg2.connect(DB_DSN)
    conn.autocommit = True
    cur = conn.cursor()

    print("Type OPEN or CLOSED and press Enter:")

    for line in sys.stdin:
        state = line.strip().upper()

        if state not in ("OPEN", "CLOSED"):
            print("Invalid input:", state)
            continue

        cur.execute(
            "INSERT INTO door_events (state, source) VALUES (%s, %s)",
            (state, "simulated_door"),
        )
        print("Logged:", state)

if __name__ == "__main__":
    main()
# Trying another simpler hack instead of connecting to a serial port
# import serial
# import psycopg2

# SERIAL_PORT = "/dev/ttys004"   # or /dev/ttyUSB0, adjust based on your Arduino
# BAUD_RATE = 9600

# DB_DSN = "dbname=doorlog user=dooruser password=doorpassword host=localhost"

# def main():
#     conn = psycopg2.connect(DB_DSN)
#     conn.autocommit = True
#     cur = conn.cursor()

#     ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

#     print("Listening for door state changes...")

#     while True:
#         line = ser.readline().decode("utf-8").strip()
#         if not line:
#             continue

#         state = line.upper()
#         if state not in ("OPEN", "CLOSED"):
#             print("Unknown message:", line)
#             continue

#         cur.execute(
#             "INSERT INTO door_events (state, source) VALUES (%s, %s)",
#             (state, "front_door"),
#         )
#         print("Logged:", state)

# if __name__ == "__main__":
#     main()