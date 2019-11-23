from flask import Flask, render_template 

app = Flask(__name__)   

@app.route('/')          
def hello_world():
    return 'Hello! Please go to /table for display'  

@app.route('/table')
def render_table():
    student_info = [
        {'name' : 'Michael', 'last_name' : 'Choi'},
        {'name' : 'John', 'last_name' : 'Supsupin'},
        {'name' : 'Mark', 'last_name' : 'Guillen'},
        {'name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("index.html", students = student_info)

if __name__=="__main__":     
    app.run(debug=True)  