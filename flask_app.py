from flask import Flask, jsonify, request

app = Flask(__name__)

data = {"message": "Hello, World!"}

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/data', methods=['POST'])
def post_data():
    data.update(request.json)
    return jsonify(data)

@app.route('/data', methods=['PUT'])
def put_data():
    data.clear()
    data.update(request.json)
    return jsonify(data)

@app.route('/data', methods=['DELETE'])
def delete_data():
    data.clear()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
