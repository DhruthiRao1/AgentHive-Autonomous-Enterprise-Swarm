from agents.planner import planner
from agents.retriever import retrieve
from agents.resolver import resolve
from agents.validator import validate

def run_swarm(ticket):
    plan = planner(ticket)
    kb = retrieve(ticket)
    resolution = resolve(ticket, kb)
    result = validate(resolution)
    return {
        'plan': plan,
        'result': result
    }
