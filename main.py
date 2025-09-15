from langchain_ollama import OllamaLLM

# Initialize the Ollama LLM
llm = OllamaLLM(model="granite3.3:2b")  # replace with your chosen Ollama model

# Input message
message = "What are some of the pros and cons of Python as a programming language?"

# Generate response using the updated method
res = llm.invoke(message)

print(res)
