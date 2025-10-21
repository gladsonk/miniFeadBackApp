# 🧠 Feedback API — Backend (FastAPI + MongoDB)

This is the backend service for the **Feedback Application**, built using **FastAPI**, **MongoDB**, and **Poetry** for dependency management.  
It follows **Test-Driven Development (TDD)** principles and provides REST APIs to submit and retrieve user feedback.

---

## 🚀 Tech Stack

- **FastAPI** — High-performance Python web framework
- **MongoDB (Motor)** — Asynchronous NoSQL database driver
- **Poetry** — Dependency and virtual environment manager
- **Pytest** — Testing framework
- **Dotenv** — Environment configuration loader

---
## 🧩 Project Structure

```text
backend/
├── app/
│   ├── __init__.py        # Package marker
│   ├── main.py            # Entry point for FastAPI
│   ├── database.py        # MongoDB connection setup
│   ├── schemas.py         # Pydantic models (data validation)
│   └── routes/
│       └── feedback.py    # Feedback API routes
├── tests/
│   └── test_feedback.py   # Unit tests (pytest)
├── .env                   # Environment variables
├── pyproject.toml         # Poetry dependencies
├── poetry.lock            # Locked dependency versions
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Prerequisites

- Python 3.10+
- [Poetry](https://python-poetry.org/docs/)
- MongoDB running locally or via Docker

---

### 2️⃣ Clone Repository

```bash
git clone https://github.com/your-username/feedback-app.git
cd feedback-app/backend
```

### 3️⃣ Setup Environment
Install dependencies using Poetry:
```bash
poetry install
```

Activate the virtual environment:
```bash
poetry shell
```

### 4️⃣ Configure Environment Variables
Create a .env file in the backend/ directory:
```env
MONGO_URL=mongodb://localhost:27017
DB_NAME=feedback_db
```

### 5️⃣ Run Development Server
```bash
poetry run start
```

API will be available at → http://127.0.0.1:8000

Open interactive docs:
* Swagger UI → http://127.0.0.1:8000/docs
* ReDoc → http://127.0.0.1:8000/redoc


