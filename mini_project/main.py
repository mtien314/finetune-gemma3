from langgraph_handlers.langgraph_edges import graph

#pain_point = "Manually analyzing thousands of open-ended survey responses for common themes is too time-consuming"

#pain_point = "It's difficult to get a single view of a customer's interaction history when they contact us."
#pain_point = "We're struggling to collect customer feedback consistently after a purchase."

#pain_point = "Our support agents are overwhelmed by the high volume of repetitive questions"
pain_point = "We have no clear idea which customer touchpoints are causing the most frustration"
result = graph.invoke({"pain_point": pain_point})
print("pain_point:", pain_point)
print("--------------------------")
print("answer:",result['final_solution'])