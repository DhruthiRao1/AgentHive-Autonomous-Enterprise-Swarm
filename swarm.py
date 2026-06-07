from agents.planner import planner
from agents.retriever import retrieve
from agents.resolver import resolve
from agents.validator import validate


def run_swarm(ticket):

    # Agent 1 - Planner
    plan = planner(ticket)

    # Agent 2 - Retriever
    knowledge = retrieve(ticket)

    # Agent 3 - Resolver
    resolution = resolve(ticket, knowledge)

    # Agent 4 - Validator
    validation = validate(resolution)

    confidence = validation.get("confidence", 95)

    return {
        "plan": plan,
        "knowledge": knowledge,
        "resolution": resolution,
        "confidence": confidence
    }
