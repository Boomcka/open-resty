from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Python backend!"

@app.route("/echo")
def echo():
    return {
        "path": request.path,
        "args": request.args
    }

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)