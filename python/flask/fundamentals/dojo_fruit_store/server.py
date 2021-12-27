from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    numitems = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    return render_template("checkout.html",numitems=numitems,raspberry=int(request.form['raspberry']),strawberry=int(request.form['strawberry']),apple=int(request.form['apple']),first_name=request.form['first_name'],last_name=request.form['last_name'],student_id=request.form['student_id'], date=datetime.now().strftime("%B %-d, %Y, %-I:%-M:%-S %p"))

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    