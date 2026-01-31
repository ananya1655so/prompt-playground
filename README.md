Prompt Playground

# Problem Statement
Designing effective AI prompts is difficult. Small changes in wording can lead to very different outputs, but there is no simple way to compare or evaluate prompts.

# Solution
Prompt Playground is a tool that allows users to create multiple versions of prompts, run them on the same input, compare outputs side by side, score prompt quality, and improve weak prompts using structured formats.

# Features
• Prompt version comparison  
• Prompt quality scoring  
• Prompt improvement suggestions  
• Fully local execution  

# Architecture
Frontend (Streamlit) → Backend (FastAPI) → Prompt Engine

# Tech Stack
• Python  
• FastAPI  
• Streamlit  

# Setup Instructions

1. Clone the repository
git clone <repository-url>
cd prompt-playground

2. Create and activate virtual environment
python -m venv venv

Windows:
venv\Scripts\activate

Mac / Linux:
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run backend
uvicorn backend.main:app --reload

5. Run frontend (in a new terminal)
python -m streamlit run frontend/app.py

The application will open automatically in the browser.

# Reproducibility
This project runs fully locally. A mock AI engine is used to demonstrate prompt comparison and evaluation logic, ensuring the project can be easily run and reviewed during the hackathon without external API dependencies.

# Prompt Strategy
Prompt evaluation focuses on clarity, specificity, constraints, and output structure. Prompt templates used for evaluation and improvement are stored in the prompts/ folder.

# Future Scope
• Integrate real LLM APIs for evaluation  
• Add more evaluation metrics  
• Support additional prompt versions and comparisons
• Support additional prompt versions and comparisons  
