from fastapi import FastAPI
from app.agent import graph

app = FastAPI()


@app.get("/")
def agent():
    return graph.invoke({"my_var": "Hello", "customer_name": "John"})
