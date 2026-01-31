import random

def mock_llm_response(prompt: str, user_input: str):
    return (
        f"Response generated for input: {user_input}\n\n"
        f"Using prompt:\n{prompt}"
    )

def score_prompt(prompt: str):
    return {
        "clarity": random.randint(6, 9),
        "specificity": random.randint(6, 9),
        "constraints": random.randint(5, 9),
        "output_format": random.randint(5, 9)
    }

def improve_prompt(prompt: str):
    return f"""
Role: You are an expert assistant.
Task: {prompt}
Constraints: Be clear and concise.
Output Format: Bullet points.
"""
