import uvicorn
from fastapi import FastAPI, Request
from backend.src.graphs.graph_builder import GraphBuilder
from backend.src.llms.groq_llm import GroqModel

import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

@app.post("/blogs")
async def create_blogs(request: Request):
    data = await request.json()
    topic = data.get("topic", "")

    # get llm
    groqllm = GroqModel()
    llm = groqllm.get_llm()

    # get graph
    graph = GraphBuilder(llm).setup_graph(usecase= "topic")
    result = graph.invoke({"topic": topic})

    return result


if __name__ == "__main__":
    uvicorn.run("app:app", host= "0.0.0.0", port= 8000, reload= True)
    