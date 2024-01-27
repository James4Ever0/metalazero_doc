from flask import Flask
app = Flask(__name__)
host, port = "0.0.0.0", 5999
@app.route("/")
def hello():
    return "lazero name resolution server"

if __name__ == "__main__":
    app.run(host=host,port=port)
