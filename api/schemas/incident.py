from pydantic import BaseModel, Field

class IncidentRequest(BaseModel):
    short_description: str
    description: str

class IncidentResponse(BaseModel):
    incident_id: str | None = None
    solution_description: str
    confidence_score: float

