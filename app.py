from flask import Flask, render_template, request
from flask_cors import CORS
from markupsafe import Markup
import openai
import markdown
import markdown.extensions.fenced_code
import markdown.extensions.codehilite

openai.api_key = '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'
app = Flask(__name__)
CORS(app)
messages = []
@app.route('/')
def home():

    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_bot_response():
    user_input = request.form['user_input']
    print(user_input)
    messages.append({'role': 'user', 'content': user_input})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    print(completion)
    ai_response = completion.choices[0].message['content']
    # print(ai_response)
    messages.append({'role': 'assistant', 'content': ai_response})
    print(messages)
    return  Markup(markdown.markdown(ai_response, extensions=['fenced_code', 'codehilite']))
    
@app.route('/reset')
def reset():
    global messages
    messages = []
    return "Conversation history has been reset."
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
