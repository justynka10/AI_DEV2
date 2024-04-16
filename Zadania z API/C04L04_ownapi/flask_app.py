from flask import Flask, request
from functions import get_response_to_user_request

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