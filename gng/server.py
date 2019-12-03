from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key = "Burritos"

@app.route("/")
def landing():
    if 'server_number' not in session:
        session['server_number'] = random.randint(1,100)
    return render_template("index.html")

@app.route("/guess", methods=['POST'])
def evalute_guess():
    user_guess = int(request.form['guess']) # POST data from server
    session['server_number'] # Number server is thinking of

    if user_guess > session['server_number']:
        session['result'] = "too high"
    elif user_guess < session['server_number']:
        session['result'] = "too low"
    else:
        session['result'] = "correct"
        session.pop('server_number')

    return redirect("/")

@app.route("/reset_game")
def reset_game():
    session.clear()
    return redirect("/")

if __name__ =="__main__":
    app.run(debug=True)