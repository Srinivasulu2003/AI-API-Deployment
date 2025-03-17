# LLM API Deployment using FastAPI, LangChain, and Ollama

This repository contains a secure and scalable AI API using open-source LLMs.

## Features
✅ LangChain for AI model orchestration  
✅ Ollama for running local LLMs  
✅ FastAPI for API development  
✅ API Key authentication  
✅ Cloudflare Tunnel / Ngrok for remote access  
✅ Google Colab & Web integration  

## Installation
```bash
pip install -r requirements.txt
```

### Install Ollama
#### macOS
```bash
brew install ollama
```
#### Linux
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```
#### Windows
Download and install Ollama from [official site](https://ollama.ai/).

### Pull a Model
```bash
ollama pull mistral
```

## Running the API
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Exposing API Securely
### Using Cloudflare Tunnel
```bash
cloudflared tunnel --url http://localhost:8000
```
### Using Ngrok
```bash
ngrok http 8000
```

## Testing API
Use Python Requests:
```python
import requests
API_URL = "https://your-api.cloudflare-tunnel.com/generate/"
API_KEY = "your-secure-key-1"
headers = {"api_key": API_KEY}
data = {"model": "mistral", "prompt": "Tell me a joke."}
response = requests.post(API_URL, json=data, headers=headers)
print(response.json())
```

## Next Steps
✅ Integrate with a frontend web app  
✅ Deploy on Google Cloud / AWS  
✅ Experiment with different AI models  

🚀 Happy Coding! 🔥
```

├── .gitignore
```
.env
__pycache__/
*.pyc
*.pyo
*.log
