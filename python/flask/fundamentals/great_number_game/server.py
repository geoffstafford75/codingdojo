from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it secret' # set a secret key for security purposes

# our index route will handle rendering our form
@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1,100)
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    print("User's Guess")
    session['guess'] = int(request.form['guess'])
    return redirect('/')

    
# adding this method
@app.route('/clear')
def clear_session():
    session.clear()
    return redirect ('/')

if __name__ == "__main__":
    app.run(debug=True)

