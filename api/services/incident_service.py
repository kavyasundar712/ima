from core_agent.incident_agent import find_solution
import random
def create_ticket(ticket_id, desc):
    return

def process_incident(description):
    result=find_solution(description)
    confidence_score=result["confidence_score"]
    soln=result["recommended_solution"]

    if soln and confidence_score >=0.8:
        return {
            "status": "resolved",
            "solution_description":soln,
            "confidence":confidence_score,
            "ticket_id": ""
        }

    ticket_id = random.randint(10000,99999)

    create_ticket(ticket_id, description)

    return {
                "status": "escalated",
                "solution_description": "NA",
                "confidence": 1-confidence_score,
                "ticket_id": ""
            }
    


    return result

def resolve_incident(desription):
    return {"recommended_solution"}