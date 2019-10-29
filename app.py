# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def demo():
    return 'Works! Python 3 Flask app, uWSGI web server with traffic routed through Nginx'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
