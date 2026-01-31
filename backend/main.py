from fastapi import FastAPI
from .schemas import PromptRequest
from .prompt_engine import mock_llm_response, score_prompt, improve_prompt

app = FastAPI()

@app.post("/run")
def run_prompts(data: PromptRequest):
    outputs = []
    scores = []

    for prompt in data.prompts:
        outputs.append(mock_llm_response(prompt, data.user_input))
        scores.append(score_prompt(prompt))

    return {
        "outputs": outputs,
        "scores": scores
    }

@app.post("/improve")
def improve_prompt_api(data: PromptRequest):
    improved = improve_prompt(data.prompts[0])
    return {"improved_prompt": improved}
