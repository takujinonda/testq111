from platform import python_version
from flask import Flask
import os
import subprocess

app = Flask(__name__)


@app.route('/')
def hello_world():
    #cmd = os.environ['BATCH_SHIPYARD_CMD']
    #stdout = subprocess.check_output(cmd)
    #print(stdout)
    return 'Hello, World!'
    #return python_version()


if __name__ == '__main__':
    app.run()
