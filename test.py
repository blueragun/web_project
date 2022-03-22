
from flask import Flask

app = Flask(__name__)
app.debug = True
test = 1

@app.route("/hello")
def hello():
    test += 1
    if test > 4:
        return test / 0
    else :
        return "<h1>project</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="2888")
