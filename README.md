# AgentHive: Autonomous Enterprise Operations Swarm

## Live Demo

https://agenthive-autonomous-enterprise-swarm-5ya3kdqsupfz5yteuqtg2v.streamlit.app

---

## Problem Statement

Enterprise IT teams spend significant time resolving repetitive incidents, searching knowledge bases, validating solutions, and coordinating across multiple systems.

Traditional AI assistants operate as single agents and struggle with complex workflows requiring planning, retrieval, reasoning, and validation.

---

## Solution

AgentHive is a Multi-Agent AI Swarm that orchestrates specialized agents to collaboratively solve enterprise incidents.

The swarm consists of:

* Planner Agent
* Retriever Agent
* Resolver Agent
* Validator Agent

Each agent performs a dedicated task and contributes to the final response.

---

## Architecture

User Request

↓

Planner Agent

↓

Retriever Agent

↓

Resolver Agent

↓

Validator Agent

↓

Final Response

---

## Agent Responsibilities

### Planner Agent

Breaks incidents into actionable tasks.

### Retriever Agent

Retrieves relevant enterprise knowledge.

### Resolver Agent

Generates recommended resolutions.

### Validator Agent

Validates the generated solution and assigns confidence.

---

## Technology Stack

* Python
* Streamlit
* LangGraph
* OpenAI / Azure OpenAI
* FAISS Vector Search
* GitHub
* Streamlit Cloud

---

## Dataset

The project contains enterprise IT incidents including:

* VPN Issues
* Outlook Issues
* Password Resets
* Printer Problems
* Teams Login Failures

---

## Deployment

Public Demo:

https://agenthive-autonomous-enterprise-swarm-5ya3kdqsupfz5yteuqtg2v.streamlit.app

---

## Future Enhancements

* Azure OpenAI Integration
* Enterprise RAG
* Agent Voting
* Dynamic Agent Creation
* Agent Memory
* Multi-Agent Collaboration

---

## Team

Dhruthi S

Microsoft Build AI 2026 Submission
