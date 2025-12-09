-- Database initialization script for DoorDuino project
-- Run with:  psql -d doorlog -U dooruser -f db/init.sql

-- Stores each open/close event sent from the Arduino
CREATE TABLE IF NOT EXISTS door_events (
    id SERIAL PRIMARY KEY,
    event_time TIMESTAMPTZ NOT NULL DEFAULT NOW(),  -- server timestamp
    state VARCHAR(10) NOT NULL CHECK (state IN ('OPEN', 'CLOSED')),
    source VARCHAR(50)                              -- e.g., front_door, garage, etc.
);