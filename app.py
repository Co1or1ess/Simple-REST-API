from flask import Flask, request

app = Flask(__name__)

@app.route("/hello")
def hello():
    return {"message": "Hello world!"}

@app.route("/add")
def add():
    x = int(request.args.get("x", 0))
    y = int(request.args.get("y", 0))
    return {"result": x + y}

if __name__ == "__main__":
    app.run(debug=True)
