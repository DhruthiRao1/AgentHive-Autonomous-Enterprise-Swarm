# AgentHive Architecture

User Request
      |
      v
Planner Agent
      |
      v
Retriever Agent
      |
      v
Resolver Agent
      |
      v
Validator Agent
      |
      v
Final Response

Agent Responsibilities

Planner Agent
- Breaks user request into tasks

Retriever Agent
- Searches knowledge base

Resolver Agent
- Generates solution

Validator Agent
- Validates response
- Generates confidence score

Technology Stack
- Python
- Streamlit
- LangGraph
- OpenAI / Azure OpenAI
- FAISS
