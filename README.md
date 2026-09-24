# Doctor and Patient API

## Project Overview

This project is a simple REST API developed using FastAPI to manage doctor and patient records.

The API supports creating and retrieving doctors and patients with data validation using Pydantic.

## Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn
* In-memory storage

## Features

### Doctor APIs

* Create a doctor
* Get all doctors
* Get a doctor by ID

### Patient APIs

* Create a patient
* Get all patients

## API Endpoints

| Method | Endpoint               | Description                      |
| ------ | ---------------------- | -------------------------------- |
| POST   | `/doctors`             | Create a new doctor              |
| GET    | `/doctors`             | Get all doctors                  |
| GET    | `/doctors/{doctor_id}` | Get doctor by ID                 |
| POST   | `/patients`            | Create a new patient             |
| GET    | `/patients`            | Get all patients                 |
| GET    | `/`                    | Check whether the API is running |

## Validation

The project uses Pydantic for validation.

### Doctor

* Name is required
* Specialization is required
* Email must be valid
* `is_active` defaults to `true`

### Patient

* Name is required
* Age must be greater than 0
* Phone number is required

## Error Handling

The API uses `HTTPException` for handling errors.

For example, if a doctor ID does not exist:

```json
{
  "detail": "Requested doctor was not found"
}
```

The API returns a `404` status code.

## How to Run

### 1. Create and activate the virtual environment

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 2. Install required packages

```bash
pip install fastapi uvicorn email-validator
```

### 3. Start the FastAPI server

```bash
python -m uvicorn main:app --reload
```

### 4. Open Swagger UI

Open the following URL in your browser:

```text
http://127.0.0.1:8000/docs
```

Swagger UI can be used to test all the API endpoints.

## Project Structure

```text
doctor-patient-fastapi/
│
├── main.py
├── README.md
├── .gitignore
└── venv/
```

The `venv` folder should not be uploaded to GitHub.

## Storage

This project uses in-memory Python lists to store doctor and patient information.

The data will be lost when the application is restarted.

## Author

Vijay Kumar
