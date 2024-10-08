from flask import Flask, jsonify, request
 
app = Flask(__name__)
 
# Home route
@app.route('/')
def home():
    return "Welcome to the Simple Python API!"
 
# GET endpoint
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})
 
# POST endpoint
@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({'you_sent': data}), 200
 
# Dynamic route with a parameter
@app.route('/api/user/<username>', methods=['GET'])
def get_user(username):
    return jsonify({'user': username})
 
if __name__ == '__main__':
    app.run(debug=True)
