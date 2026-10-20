# Industrial CIP-Station Anomaly Tracker (FastAPI Backend Case)

A high-performance REST API backend built with Python and FastAPI, designed to simulate real-time sensor data tracking from industrial CIP (Cleaning-in-Place) stations and automatically log critical temperature anomalies into a SQLite database.

## 🛠 Tech Stack
- **Language:** Python 3.x
- **Framework:** FastAPI
- **ASGI Server:** Uvicorn
- **Database:** SQLite3 (Native data access via resource context managers)

## 🚀 Core Functionality
- **Dynamic Routing:** Processes real-time parameters (station ID and temperature constraints) directly from network endpoints.
- **Automated Logging:** Embedded conditional logic automatically captures temperature thresholds (>80°C) and writes structured failure logs to the relational database.
- **Self-Generated Interactive Documentation:** Out-of-the-box API inspection and manual execution testing endpoints via Swagger UI (`/docs`).
- **Clean JSON Serialization:** Explicit tuple-to-dictionary data mapping for historical log inspection requests.

## 📦 Project Structure
```text
├── database/          # Local storage directory for automated SQLite binaries
└── main.py            # Main application script (endpoints routing, initialization & DB hooks)
```

## ⚙️ Installation & Launch

1. Clone the repository:
   ```bash
   git clone https://github.com/igormazur5553-netizen/fastapi-anomaly-tracker
   cd fastapi-anomaly-tracker
   ```

2. Run the production ASGI server:
   ```bash
   uvicorn main:app --reload
   ```
