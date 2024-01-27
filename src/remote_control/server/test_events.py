from flask import Flask

app = Flask(__name__)
host="0.0.0.0"
port=19243

def homepage():
    with open("test_events.html","r") as f:
        return f.read()

@app.route("/")
def index():
    return homepage()

if __name__ == "__main__":
    app.run(host=host,port=port)
