from langchain_ollama import OllamaLLM
import subprocess
import sys

# --------------- CONFIG ----------------
MODEL_NAME = "granite3.3:2b"  # choose a valid model installed in Ollama
MESSAGE = "What are some of the pros and cons of Python as a programming language?"

# --------------- HELPER FUNCTIONS ----------------

def check_ollama_server():
    """Check if Ollama server is running by listing models"""
    try:
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print("Ollama server is not running. Start it with `ollama server start`.")
            return False
        return True
    except FileNotFoundError:
        print("Ollama CLI not found. Make sure Ollama is installed and in PATH.")
        return False

def check_model(model_name):
    """Check if the model exists locally"""
    result = subprocess.run(
        ["ollama", "list"],
        capture_output=True,
        text=True
    )
    models = result.stdout.splitlines()
    for line in models:
        if model_name in line:
            return True
    return False

# --------------- MAIN ----------------

if not check_ollama_server():
    sys.exit(1)

if not check_model(MODEL_NAME):
    print(f"Model '{MODEL_NAME}' not found. Pulling it now...")
    subprocess.run(["ollama", "pull", MODEL_NAME], check=True)
    print(f"Model '{MODEL_NAME}' pulled successfully!")

# Initialize Ollama LLM via LangChain
llm = OllamaLLM(model=MODEL_NAME)

try:
    # Generate response
    res = llm.invoke(MESSAGE)
    print("✅ Response from Ollama:")
    print(res)
except Exception as e:
    print("❌ Error while invoking the model:", e)
