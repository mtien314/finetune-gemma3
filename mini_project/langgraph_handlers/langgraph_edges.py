from langgraph.graph import StateGraph, START, END
from typing_extensions import Any, Dict, List, Optional,TypedDict
from typing import Union
from .langgraph_nodes import retrieval_solution_recommend, generate_final_solution

class State(TypedDict):
    pain_point: str
    solution_recommend: list[str]
    final_solution: str

graph_builder = StateGraph(State)
graph_builder.add_node("retrieval_solution_recommend", retrieval_solution_recommend)
graph_builder.add_node("generate_final_solution", generate_final_solution)


graph_builder.add_edge(START, "retrieval_solution_recommend")
graph_builder.add_edge("retrieval_solution_recommend","generate_final_solution")                       
graph_builder.add_edge("generate_final_solution",END)

graph = graph_builder.compile()


