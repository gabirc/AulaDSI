from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/alunos")
def alunos():
    return jsonify(
        number=6,
        people=[
            {"name":"Gabriella", "idade":21},
            {"name":"Diego", "idade":27},
            {"name":"Diego", "idade":22},
            {"name":"Jorge", "idade":21},
            {"name":"Silvânia", "idade":22},
            {"name":"Rapahel", "idade":22}
       ] )