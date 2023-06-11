from flask import Flask

app = Flask('app')


@app.route('/')
def hello():
    return 'Hello, World!'