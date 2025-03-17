from fastapi import FastAPI, HTTPException, Depends, Header
from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
API_KEYS = {
    "user1": os.getenv("API_KEY_USER1"),
    "user2": os.getenv("API_KEY_USER2"),
}

app = FastAPI()

# API Key Authentication
def verify_api_key(api_key: str = Header(None)):
    if api_key not in API_KEYS.values():
        raise HTTPException(status_code=401, detail="Invalid API key")

# Initialize LangChain LLM with Ollama
def get_llm(model_name: str):
    return Ollama(model=model_name)

@app.get("/")
def home():
    return {"message": "LangChain + Ollama API is running"}

@app.post("/generate/")
def generate_text(model: str, prompt: str, api_key: str = Depends(verify_api_key)):
    llm = get_llm(model)
    response = llm.invoke(prompt)
    return {"response": response}
