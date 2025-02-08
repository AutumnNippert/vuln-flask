from flask import Flask, render_template, request
import subprocess

messages = []

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/potato')
def potatoing():
    return 'Potato!'

@app.route('/get-file/<filename>')
def get_file(filename):
    with open(filename, 'r') as f:
        return f.read()
    
@app.route('/run-command', methods=['POST', 'GET'])
def run_command():
    result = ''
    if request.method == 'POST':
        result = subprocess.run(request.form['message'].split(' '), capture_output=True, text=True)
        result = result.stdout
    return render_template('run_command.html', value=result)

@app.route('/chat', methods=['POST', 'GET'])
def chat():
    if request.method == 'POST':
        message = request.form['message']
        if message:
            messages.append(message)  # Add the message to the chat history
    return render_template('chat.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='12345')