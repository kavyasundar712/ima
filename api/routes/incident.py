from fastapi.routing import APIRoute
from schemas.incident import IncidentRequest, IncidentResponse
from services.incident_service import process_incident
inc_route = APIRoute(path="/incidents", tags="incidents")

@inc_route.post("/info", response_model=IncidentResponse)
def post_info(request: IncidentRequest):
    new_description = request.short_description + request.description

    solution = process_incident(new_description)

    return solution





