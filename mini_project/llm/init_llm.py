import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from core_settings.settings import settings


os.environ['GOOGLE_API_KEY'] = settings.GOOGLE_API_KEY

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature = 0)

prompt = """
You are a Solution Consultant at Filum.ai.
Based on the customer’s Pain Point below, propose the most suitable Filum.ai solution base on solution recommend, explaining why it fits and how it can help address their challenges.
Be clear, professional, and customer-centric in your recommendation.

Example:
  - Pain Point: "We're struggling to collect customer feedback consistently after a purchase."
Only return format Potential Filum.ai and how it helps below
  - Potential Filum.ai Solution: "Automated Post-Purchase Surveys (VoC - Surveys)" – How it helps: Trigger surveys automatically via email/SMS after a transaction.
Pain Point : {pain_point}
Solution: {solution}

"""
prompt_llm = PromptTemplate.from_template(prompt)
# question = "Manually analyzing thousands of open-ended survey responses for common themes is too time-consuming"
# solution = vectordb.similarity_search(question,k = 5)
chain = prompt_llm | llm


