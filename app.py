from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Swahili AI Assistant!"}
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a data model for user input
class ChatRequest(BaseModel):
    user_input: str

@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.user_input
    
    # Replace this with your chatbot logic
    if user_message.lower() == "hello":
        bot_response = "Habari! Naweza kukusaidiaje leo?"
    elif user_message.lower() == "how are you?":
        bot_response = "Niko salama! Asante kwa kuuliza."
    else:
        bot_response = "Samahani, bado sijakuelewa vizuri."

    return {"response": bot_response}
import logging

logging.basicConfig(level=logging.INFO)

@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.user_input
    logging.info(f"User input: {user_message}")

    # Replace this with chatbot logic
    if user_message.lower() == "hello":
        bot_response = "Habari! Naweza kukusaidiaje leo?"
    else:
        bot_response = "Samahani, bado sijakuelewa vizuri."

    logging.info(f"Bot response: {bot_response}")
    return {"response": bot_response}
import logging
logging.basicConfig(level=logging.INFO)
@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.user_input
    logging.info(f"User input: {user_message}")

    # Chatbot logic
    if user_message.lower() == "hello":
        bot_response = "Habari! Naweza kukusaidiaje leo?"
    else:
        bot_response = "Samahani, bado sijakuelewa vizuri."

    logging.info(f"Bot response: {bot_response}")
    return {"response": bot_response}
