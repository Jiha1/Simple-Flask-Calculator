from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

# Define calculator


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    a = request.form['a']
    b = request.form['b']
    operation = str(request.form['operation'])

    if operation == "+":
        result = float(a) + float(b)
    elif operation == "-":
        result = float(a) - float(b)
    elif operation == "/":
        result = float(a) / float(b)
    elif operation == "x":
        result = float(a) * float(b)
    else:
        result = "+, -, /, x only"

    return render_template('index.html', prediction_text=str(result))


if __name__ == "__main__":
    app.run(debug=True)
