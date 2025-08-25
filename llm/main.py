from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
import uvicorn
import os  # Added for environment variable usage

app = FastAPI()


class Prompt(BaseModel):
    prompt: str


@app.post("/generate")
def generate_text(prompt: Prompt):
    try:
        # Use environment variables for host and model, with fallbacks
        ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
        ollama_model = os.getenv("OLLAMA_MODEL", "llama3:latest")

        response = requests.post(
            f"{ollama_host}/api/generate",  # f-string for host
            json={"model": ollama_model, "prompt": prompt.prompt},  # Use ollama_model
            stream=True,
            timeout=120  # Give model time to respond
        )
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)

        output = ""
        for line in response.iter_lines():
            if line:
                data = line.decode("utf-8").strip()
                if data.startswith("data: "):
                    data = data[len("data: "):]
                if data == "[DONE]":
                    break
                try:
                    chunk = json.loads(data)
                    output += chunk.get("response") or chunk.get("text") or ""
                except json.JSONDecodeError:
                    print(f"Warning: Could not decode JSON from line: {data}")  # Added for debugging
                    continue

        return {"response": output.strip() or "(Empty response from model)"}

    except requests.RequestException as e:
        return {"error": f"Ollama request failed: {str(e)}"}


if __name__ == "__main__":
    # For development, reload=True can be useful. For production, use reload=False.
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)