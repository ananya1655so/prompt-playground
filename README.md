# Prompt Playground 

**Prompt Playground** is a lightweight, local-first tool that helps users **compare, evaluate, and improve AI prompts side-by-side**.
It focuses on *understanding why one prompt performs better than another*, not just viewing outputs.

# Problem Statement

Designing effective AI prompts is difficult.

Small changes in wording, structure, or constraints can drastically change AI responses, yet:
* There is no simple way to **compare multiple prompts** on the same input.
* Prompt quality is rarely **measured or explained**.
* Beginners struggle to understand *why* a prompt fails.

# Solution

Prompt Playground provides a **structured environment** to:
* Compare multiple prompt versions
* Run them on identical input
* Score prompt quality
* Suggest improvements based on best practices

All while running **fully locally**, with no external API dependencies.

# Key Features

* Side-by-side prompt comparison
* Prompt quality scoring
* Prompt improvement suggestions
* Clean, beginner-friendly UI
* Fully local & reproducible execution
* Extendable architecture for real LLMs

# Why Prompt Playground Is Better

* Most tools focus on *outputs* Prompt Playground focuses on *prompt quality*
* Encourages prompt engineering best practices
* Offline & API-free → perfect for hackathons
* Simple architecture, easy to extend
* Beginner-friendly but technically sound

# Architecture Overview

User
 ↓
Streamlit Frontend
 ↓
FastAPI Backend
 ↓
Prompt Engine (Evaluation + Improvement Logic)


#  Project Structure

prompt-playground/
├── backend/
│   ├── main.py
│   ├── schemas.py
│   └── prompt_engine.py
│
├── frontend/
│   └── app.py
│
├── prompts/
│   ├── scoring_prompt.txt
│   └── rewrite_prompt.txt
│
├── requirements.txt
└── README.md


# Frontend (Streamlit)

**Responsibilities**

* Collect user input (prompts + shared input)
* Trigger comparison or improvement
* Display:

  * Outputs
  * Scores
  * Improved prompt suggestions

**Why Streamlit?**

* Extremely fast UI development
* Perfect for hackathon demos
* No frontend framework overhead

#  Backend (FastAPI)

**Responsibilities**
* Receive prompts and input
* Run evaluation logic
* Score prompts
* Generate improved prompt suggestions

**Why FastAPI?**
* Lightweight
* Fast
* Clean API separation
* Easy future LLM integration

#  Prompt Engine (Mock AI)
To ensure **full reproducibility**, a **mock AI engine** is used.

### Why mock AI?

* No API keys required
* No rate limits
* Judges can run instantly
* Logic remains realistic and extensible

The system is designed so real LLM APIs can be plugged in later.

# Prompt Strategy
Prompt evaluation focuses on:

* Clarity
* Specificity
* Constraints
* Output structure

Prompt templates are stored in the `prompts/` folder for transparency and reproducibility.

## Tech Stack
* Python
* FastAPI
* Streamlit

# Setup Instructions (Build Reproducibility)

### Clone the repository

```bash
git clone <repository-link>
cd prompt-playground
```

### (Optional) Create virtual environment

```bash
python -m venv venv
```

**Activate**

* Mac/Linux: `source venv/bin/activate`
* Windows: `venv\Scripts\activate`

## Install dependencies

```bash
pip install -r requirements.txt
```

## Start backend (Terminal 1)

```bash
uvicorn backend.main:app --reload

## Start frontend (Terminal 2)

```bash
python -m streamlit run frontend/app.py

The app opens automatically in the browser.


## How Judges Should Test This

1. Enter two prompt versions
2. Enter a common input
3. Click **Run Comparison**
4. Observe:

   * Side-by-side outputs
   * Prompt quality scores
   * Improvement suggestions

# Final Output

* Visual comparison of prompts
* Clear scoring feedback
* Improved prompt version

# Future Scope

* Integrate real LLM APIs
* Add more evaluation metrics
* Support more prompt versions
* Export results for learning & sharing

# Conclusion
Prompt Playground turns prompt engineering from **guesswork into structured learning** making it easier, clearer, and more effective for everyone.
