from flask import Flask, request, flash
import userCon

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        userCon.add_user(username, password)
    return "not post"



if __name__ == "__main__":
    app.run()
