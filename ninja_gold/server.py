from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key = "Burritos"

@app.route("/")
def landing():
    if 'total_gold' not in session:
        session['total_gold'] = 0
    message = f"<p>Earned gold: {session['total_gold']}</p>"
    return render_template("index.html", message=message)

@app.route("/process_money", methods=['POST'])
def process_gold():
    if request.form['location'] =='farm':
        session['total_gold'] += random.randint(10,20)
    elif request.form['location'] =='cave':
        session['total_gold'] += random.randint(5,10)
    elif request.form['location'] =='house':
        session['total_gold'] += random.randint(2,5)
    elif request.form['location'] =='casino':
        session['total_gold'] += random.randint(-50,50)
    return redirect("/")



@app.route("/reset_game")
def reset_game():
    session.clear()
    return redirect("/")

if __name__ =="__main__":
    app.run(debug=True)