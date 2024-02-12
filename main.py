from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/bye')
def say_bye():
    return 'bye'

@app.route('/<name>')
def greet(name):
    return f'Congratulations {name}'

if __name__ == '__main__':
    app.run(debug=True)