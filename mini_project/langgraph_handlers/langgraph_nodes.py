from typing_extensions import Any, Dict, List, Optional,TypedDict
from typing import Union
from llm.initial_vectordb import vectordb
from llm.init_llm import chain

def retrieval_solution_recommend(state):
    #print(state['pain_point'])
    pain_point = state['pain_point']
    solution_recommend = vectordb.similarity_search(pain_point, k = 5)
   
    return {'solution_recommend':solution_recommend}


def generate_final_solution(state):
    pain_point = state['pain_point']
    solution =state['solution_recommend']
    final_solution = chain.invoke({"pain_point": pain_point,"solution":solution}).content
    return {"final_solution":final_solution}