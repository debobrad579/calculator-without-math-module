from flask import Flask, jsonify, render_template, request
from util import *
from constants import *
from number_theoretic import *
from exponential import *
from trigonometric import *
from special import *


@format_complex
def solve(equation):
    try:
        return eval(append_multiplication(equation.replace("^", "**").replace("Ψ", "+")))
    except Exception as error:
        return error


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api", methods=["GET"])
def api_all():
    if request.args.get("equation"):
        equation = request.args.get("equation")
        return jsonify({"equation": str(solve(equation)).replace("j", "i")})


if __name__ == "__main__":
    app.run(debug=True)
