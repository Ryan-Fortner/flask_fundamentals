from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    print('Charging {"first_name"} {"last_name"} for {int(strawberry_form)+int(raspberry_form)+int(apple_form)} fruits')
    strawberry_form=request.form['strawberry']
    raspberry_form=request.form['raspberry']
    apple_form=request.form['apple']
    first_name_form=request.form["first_name"]
    last_name_form=request.form["last_name"]
    student_id_form=request.form["student_id"]
    return render_template("checkout.html", strawberry_checkout=strawberry_form, raspberry_checkout=raspberry_form, apple_checkout=apple_form, first_name_checkout=first_name_form, last_name_checkout=last_name_form, student_id_checkout=student_id_form,
    count_checkout=(int(strawberry_form)+int(raspberry_form)+int(apple_form)))

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    