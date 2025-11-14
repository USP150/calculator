from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def safe_float(value):
    try:
        return float(value)
    except ValueError:
        return None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculator", methods=["POST"])
def calculator():
    x = safe_float(request.form.get("x"))
    y = safe_float(request.form.get("y"))
    operation = request.form.get("operation")

    if x is None or y is None:
        return jsonify({"status": "error", "message": "Inputs must be numbers"}), 400

    if operation not in ["addition", "subtraction", "multiplication", "division"]:
        return jsonify({"status": "error", "message": "Invalid operation"}), 400

    try:
        if operation == "addition":
            result = x + y
        elif operation == "subtraction":
            result = x - y
        elif operation == "multiplication":
            result = x * y
        elif operation == "division":
            if y == 0:
                return jsonify({"status": "error", "message": "Cannot divide by zero"}), 400
            result = x / y

        return jsonify({"status": "success", "result": result})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
