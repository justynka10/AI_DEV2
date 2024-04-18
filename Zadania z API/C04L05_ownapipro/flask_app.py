from flask import Flask, request
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory # "pływające okno" 
from langchain.chains import ConversationChain

from dotenv import load_dotenv
load_dotenv(override=True)

chat = ChatOpenAI(
    model="gpt-4")
memory = ConversationBufferWindowMemory()
chain = ConversationChain(llm=chat, memory=memory)

def get_response_to_user_request(question):

    response = chain.invoke(input=question)
    return response['response']

#############################
app = Flask(__name__)

@app.route('/', methods=['POST'])
def generate_response_to_user_question():
    if request.method == 'POST':
        # Get user question
        print("Request JSON data:", request.json)
        print("User question is: ", request.json['question'])

        # Generate answer
        answer = get_response_to_user_request(question=request.json['question'])
        print("Answer to user question is", answer)
        formatted_answer = {"reply":answer}
    return formatted_answer
               

# Start flask app
if __name__ == '__main__':
    app.run(port=5000)