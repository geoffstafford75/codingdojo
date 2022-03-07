from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it secret and safe' # set a secret key for security purposes

# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process_gold', methods=['POST'])
def process_gold():
    form = request.form['form']
    print(form)
    gold = 0
    activity_date = datetime.datetime.now().strftime("%c")

    if form == "farm":
        gold = random.randint(10,20)
    elif form == 'cave':
        gold = random.randint(5,10)
    elif form == "house":
        gold = random.randint(2,5)
    elif form == "casino":
        gold = random.randint (-50,50)

    # Initialize session activity "
    if 'activity' not in session:
        session['activity'] = ''

    if gold > 0:
        session['activity'] = f"<li class='list-group-item text-success'>Earned {gold} gold from the {form}! ({activity_date})</li>" + session['activity']
    else:
        session['activity'] = f"<li class='list-group-item text-danger'>Entered a {form} and lost {gold} gold ... Ouch. ({activity_date})</li>" + session['activity']

    if 'total_gold' in session:
        session['total_gold'] += gold
    else:
        session['total_gold'] = 0

    print(session)

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    session['total_gold'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

