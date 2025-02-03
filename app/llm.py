from langchain_openai import ChatOpenAI
from typing import TypedDict
from langgraph.graph import MessagesState
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import SystemMessage


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, max_tokens=100)


class State(MessagesState):
    my_var: str
    customer_name: str


system_message = SystemMessage(
    content="You are a helpful assistant expert in software engineer and javascript, all my questions should be answered oriented to this topic and should be no longer than 3 lines.",
)


def node_llm(state: State) -> State:
    print("State", State)
    return {"messages": [llm.invoke([system_message] + state["messages"])]}


builder = StateGraph(State)
builder.add_node("node_llm", node_llm)

builder.add_edge(START, "node_llm")
builder.add_edge("node_llm", END)


graph = builder.compile()
