from flask import Flask

app = Flask("mirocblog")

@app.route("/")
def index():
    return "Olá mundo"