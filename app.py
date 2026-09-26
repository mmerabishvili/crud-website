from flask import Flask

app = Flask(__name__)

@app.route('/')
def simple_route():
    return "Hello, User ^_^!"

@app.route('/about')
def about_route():
    return "There is displayed information about the company!"