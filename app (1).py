from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Resume Objective Generator API")

class ResumeData(BaseModel):
    name: str
    role: str
    skills: str
    experience: str

@app.get("/")
def home():
    return {"message": "Resume Objective Generator API is Running"}

@app.post("/generate")
def generate_objective(data: ResumeData):
    objective = (
        f"Motivated and dedicated {data.role} with "
        f"{data.experience} years of experience and expertise in "
        f"{data.skills}. Seeking an opportunity to contribute my skills, "
        f"enhance my knowledge, and grow professionally while adding value "
        f"to the organization."
    )

    return {
        "name": data.name,
        "objective": objective
    }