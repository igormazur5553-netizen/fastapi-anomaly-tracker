import sqlite3, os
from fastapi import FastAPI

app = FastAPI()
DP_PATH = 'database/logs.db'

def init_db():
    if not os.path.exists('database'):
        os.makedirs('database')
    with sqlite3.connect(DP_PATH) as db:
        cursor = db.cursor()
        query = '''CREATE TABLE IF NOT EXISTS anomaly_logs (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            station_id TEXT,
            temperature REAL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP )'''
        cursor.execute(query)

init_db()

@app.get("/")
def read_root():
    return {
        'status': 'online',
        'message': 'Сервер успешно запущен!',
        'developer': 'Игорь Мазур'
    }

@app.get("/station/{station_id}")
def get_custom_station(station_id: str, temperature: float = 20.0):
    is_anomaly = temperature > 80.0
    if is_anomaly:
        msg = 'Внимание! Превышен температурный режим!'
        with sqlite3.connect(DP_PATH) as db:
            cursor = db.cursor()
            query = 'INSERT INTO anomaly_logs (station_id, temperature) VALUES (?, ?)'
            cursor.execute(query, (station_id, temperature))
    else:
        msg = 'Станция работает стабильно.'

    return {
        'status': 'processed',
        'requested_station': station_id,
        'current_temperature': temperature,
        'anomalies_detected': is_anomaly,
        'system_message': msg
    }

@app.get("/logs")
def get_anomaly_logs():
    with sqlite3.connect(DP_PATH) as db:
        cursor = db.cursor()
        query = 'SELECT station_id, temperature, timestamp FROM anomaly_logs ORDER BY id DESC'
        cursor.execute(query)
        rows = cursor.fetchall()

    return [
        {'station_id': row[0], 'temperature': row[1], 'timestamp': row[2]}
        for row in rows
    ]