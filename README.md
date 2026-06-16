# Blender-Full

A full-stack Blender AI assistant powered by a fine-tuned Qwen 2.5 Coder model, FastAPI, PostgreSQL, React, and Vite.

## Features

* AI-powered Blender Python (BPY) code generation
* Fine-tuned Qwen 2.5 Coder LoRA model
* Conversation history storage using PostgreSQL
* React-based chat interface
* FastAPI backend
* Local GPU inference using CUDA
* Multi-chat session management

---

## Architecture

```text
Frontend (React + Vite)
            |
            v
Backend (FastAPI + PostgreSQL)
            |
            v
Qwen 2.5 Coder + LoRA Adapter
            |
            v
Generated Blender Python Code
```

---

## Repository Structure

```text
Blender-full/
│
├── backend/
│   ├── checkpoint-2109/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── backend_requirements.txt
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## Requirements

### Software

* Python 3.11.9
* Node.js 18+
* PostgreSQL 14+
* NVIDIA GPU with CUDA support
* Git

### Tested GPU

* NVIDIA T400 4GB

---

## PostgreSQL Setup

Create a database:

```sql
CREATE DATABASE blender;
```

Update the database connection inside:

```text
backend/database.py
```

Example:

```python
engine = create_engine(
    "postgresql://<username>:<password>@localhost:5432/blender"
)
```

---

## Backend Setup

Navigate to backend:

```bash
cd backend
```

Create virtual environment:

```bash
py -3.11 -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r backend_requirements.txt
```

Install CUDA-enabled PyTorch:

```bash
pip uninstall torch torchvision torchaudio -y

pip install torch==2.5.1+cu121 torchvision==0.20.1+cu121 torchaudio==2.5.1+cu121 --index-url https://download.pytorch.org/whl/cu121
```

Verify CUDA:

```bash
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

Expected:

```text
2.5.1+cu121
True
```

Run backend:

```bash
uvicorn main:app --reload --port 8001
```

Backend Swagger:

```text
http://127.0.0.1:8001/docs
```

---

## Frontend Setup

Navigate to frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run frontend:

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

## Model Information

Base Model:

```text
Qwen/Qwen2.5-Coder-1.5B-Instruct
```

Fine-Tuning:

```text
LoRA Adapter
```

Checkpoint Location:

```text
backend/checkpoint-2109
```

---

## Running the Application

Start backend:

```bash
cd backend
venv\Scripts\activate
uvicorn main:app --reload --port 8001
```

Start frontend:

```bash
cd frontend
npm run dev
```

Open:

```text
http://localhost:5173
```

---

## Troubleshooting

### CUDA Not Available

Verify:

```bash
python -c "import torch; print(torch.cuda.is_available())"
```

Expected:

```text
True
```

---

### PEFT Version Error

Install:

```bash
pip install peft==0.19.1
```

---

### Missing PostgreSQL Database

Create:

```sql
CREATE DATABASE blender;
```

---

## License

This project is intended for educational and research purposes.
