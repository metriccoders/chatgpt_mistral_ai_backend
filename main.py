from llama_cpp import Llama
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel



#Path to mistral-ai.Q2_K.gguf model in your local machine
model_path = "PATH_TO_THE_MODEL"
app = FastAPI()
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


LLM = Llama(model_path=model_path)


class QueryItem(BaseModel):
    query: str
    

@app.post("/answers/")
def fetch_answer(queryItem: QueryItem):
    question = queryItem.query
    output = LLM(question, max_tokens=1000)
    return output["choices"][0]["text"]