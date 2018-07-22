from platform import python_version
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'
    #return python_version()


if __name__ == '__main__':
    app.run()
