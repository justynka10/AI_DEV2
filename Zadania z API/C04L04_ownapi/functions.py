from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

from dotenv import load_dotenv
load_dotenv(override=True)

def get_response_to_user_request(question):

    chat = ChatOpenAI(model="gpt-4")
    
    response = chat.invoke(input=[
        SystemMessage("Answer the user question"),
        HumanMessage(question)
        ])
    return(response.content)