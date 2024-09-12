import json
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


cat=[{"name":"betty","age":20},{"name":"alex","age":21},{"name":"shadi","age":15}]

@app.route('/')
def hello():
    return cat

@app.route('/test')
def test():
    return "hello"
 
 
if __name__ == '__main__':
    app.run(debug=True)


