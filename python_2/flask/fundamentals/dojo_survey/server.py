from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    
    session['name'] = request.form['name']
    session['locaation'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    print(session)
    return redirect('/result')

    
# adding this method
@app.route('/result')
def show_user():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)

