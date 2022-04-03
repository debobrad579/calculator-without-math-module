from flask import Flask, jsonify, render_template, request
from constants import *
from number_theoretic import *
from exponential import *
from trigonometric import *


app = Flask(__name__)


@format_complex
def solve(equation: str):
    equation = equation.replace("^", "**").replace("j", "1j")
    return eval(equation)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/api', methods=['GET'])
def api_all():
    if request.args.get('equation'):
        equation = request.args.get('equation')
        return jsonify({"equation": str(solve(equation.replace("Ψ", "+"))).replace("j", "i")})


if __name__ == '__main__':
    app.run(debug=True)
