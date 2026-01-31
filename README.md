# Prompt Playground

## Problem Statement
Designing effective AI prompts is difficult. Small changes in wording can lead to very different outputs, but there is no simple way to compare or evaluate prompts.

## Solution
Prompt Playground is a tool that allows users to:
- Create multiple versions of prompts
- Run them on the same input
- Compare outputs side-by-side
- Score prompt quality
- Improve weak prompts using structured formats

## Features
- Prompt version comparison
- Prompt quality scoring
- Prompt improvement suggestions
- Reproducible and local execution

## Architecture
Frontend (Streamlit) → Backend (FastAPI) → Prompt Engine

## Tech Stack
- Python
- FastAPI
- Streamlit

## Setup Instructions

1. Clone the repository
2. Create a virtual environment
   python -m venv venv
3. Activate environment
   - Windows: venv\\Scripts\\activate
   - Mac/Linux: source venv/bin/activate
4. Install dependencies
   pip install -r requirements.txt
5. Run backend
   uvicorn backend.main:app --reload
6. Run frontend
   streamlit run frontend/app.py

## Reproducibility
This project runs fully locally.
A mock AI engine is used to ensure:
- deterministic behavior
- no dependency on external APIs
- easy evaluation by judges

## Prompt Strategy
Prompt evaluation focuses on:
- clarity
- specificity
- constraints
- output structure

Prompt templates are stored in the `prompts/` folder.

## Future Scope
- Replace mock AI with real LLM APIs
- Add more evaluation metrics
- Support more prompt versions
- Replace mock AI with real LLM APIs
- Add more evaluation metrics
- Support more prompt versions
