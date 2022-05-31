from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello_world():
    if (request.method == 'GET'):
        data = {"data": "Hello World"}
        return jsonify(data)

@app.route('/about',methods=['GET'])
def about_page():
    if (request.method == 'GET'):
        info = {'name': 'Jimit',
                'address': 'India',
                'email': 'jimit123@gmail.com',
                'state':'kerala'}
        return jsonify(info)

@app.route('/input', methods=['POST'])
def input():
    body = request.json
    return body

@app.route('/numbers', methods=['POST'])
def numbers():
    numbers = request.json
    sum = 0
    for number in numbers['num']:
        sum = sum + number
    return str(sum)

if __name__ == '__main__':
    app.run(debug=True)