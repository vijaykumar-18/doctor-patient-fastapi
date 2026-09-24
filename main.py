from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(
    title="Doctor and Patient API",
    description="API for managing doctor and patient records",
    version="1.0.0"
)

doctors = []
patients = []

class Doctor(BaseModel):
    name: str
    specialization: str
    email: EmailStr
    is_active: bool = True


class Patient(BaseModel):
    name: str
    age: int = Field(gt=0)
    phone: str


doctors = [
    {
        "id": 1,
        "name": "Dr. shankar",
        "specialization": "Cardiology",
        "email": "ravi@gmail.com",
        "is_active": True
    }
]

patients = [
    {
        "id": 1,
        "name": "sampath",
        "age": 22,
        "phone": "9876543210"
    }
]

patients = [
    {
        "id": 2,
        "name": "sanju",
        "age": 12,
        "phone": "9876663210"
    }
]

@app.post("/doctors")
def create_doctor(doctor: Doctor):

    doctor_id = len(doctors) + 1

    doctor_data = {
        "id": doctor_id,
        **doctor.model_dump()
    }

    doctors.append(doctor_data)

    return {
        "message": "Doctor created successfully",
        "doctor": doctor_data
    }


@app.get("/doctors")
def get_doctors():

    return {
        "doctors": doctors
    }


@app.get("/doctors/{doctor_id}")
def get_doctor(doctor_id: int):

    for doctor in doctors:
        if doctor["id"] == doctor_id:
            return doctor

    raise HTTPException(
        status_code=404,
        detail="Doctor not found"
    )



@app.post("/patients")
def create_patient(patient: Patient):

    patient_id = len(patients) + 1

    patient_data = {
        "id": patient_id,
        **patient.model_dump()
    }

    patients.append(patient_data)

    return {
        "message": "Patient created successfully",
        "patient": patient_data
    }


@app.get("/patients")
def get_patients():

    return {
        "patients": patients
    }
