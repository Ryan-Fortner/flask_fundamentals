from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    session.modified = True
    session['visits'] = 0
    return redirect('/show')

@app.route('/show')
def counter():
    session.modified = True
    session['visits'] += 1
    return render_template('index.html')

@app.route('/reset')
def reset():
    session.modified = True
    return redirect('/')


@app.route('/add_two')
def add_two():
    session.modified = True
    session['visits'] +=2
    return render_template('index.html')

@app.route('/pick', methods=['POST'])
def pick_visits():
    session.modified = True
    return render_template('index.html', number_visits=session['visits']+int(request.form['number']))




if __name__=="__main__":   
    app.run(debug=True)  