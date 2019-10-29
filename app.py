# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def demo():
    return 'demo-flask test application using docker-compose'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
