from flask import Flask, render_template, request
import os

app = Flask(__name__)

def check(lst):
    return lst == lst[::-1]

def execute(payload):
    try:
        blacklist = ['__builtins__', '__import__', 'eval', 'exec', 'import', 'from', 'os', 'sys', 'system', 'timeit', 'base64commands','subprocess', 'pty','chr', 'platform', 'open', 'read', 'write','dir','globals', 'type','lower']
        if any(func in payload for func in blacklist):
            return "Not Allowed"
        result = eval(payload)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

def check_blacklist(input_str):
    blacklist = set([';', '|', '&', '>', '<', '`', '$','*', '{', '}'])
    return any(char in blacklist for char in input_str)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None 
    if request.method == 'POST':
        user_input = request.form['user_input']

        if check_blacklist(user_input):
            result = "Invalid input"
        else:
            user_input=execute(user_input)
            if len(user_input) < 1000 and not check(user_input):
            	result = "You're not getting out."
             
            elif len(user_input) == 1000 and check(user_input):
                result = os.environ['FLAG']
            else:
                result = "Invalid"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
