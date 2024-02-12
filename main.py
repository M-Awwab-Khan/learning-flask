from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1 style="text-align: center">Hello World</h1>'\
            '<p>This is a sample paragraph</p>'\
            '<img src="https://media.giphy.com/media/ukgcHmvflVWjwE8eU5/giphy.gif?cid=790b7611445wpyc5ewpievp0xxxi3922z1bne2bbvu8x3lqx&ep=v1_gifs_search&rid=giphy.gif&ct=g", width=200>'

@app.route('/bye')
def say_bye():
    return 'bye'

@app.route('/<name>')
def greet(name):
    return f'Congratulations {name}'

@app.route('/<name>/<int:age>')
def tell(name, age):
    return f'Hello, You are {name} and {age} years old.'

if __name__ == '__main__':
    app.run(debug=True)