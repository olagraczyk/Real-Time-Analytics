from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Witaj w moim API!"})

@app.route('/mojastrona')
def mojastrona():
    return jsonify({"message": "To jest moja podstrona!"})

@app.route('/hello')
def hellopage():
    name = request.args.get('name')
    if name:
        return jsonify({"message": f"Hello {name}!"})
    else:
        return jsonify({"message": "Hello!"})

@app.route('/api/v1.0/predict')
def predict():
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)
    if (num1+num2) > 5.8:
        prediction = 1
    else:
        prediction = 0
        
    return jsonify({
        "prediction": prediction,
        "features": {
            "num1": num1,
            "num2": num2
        }
    })
        
if __name__ == '__main__':
    app.run()
