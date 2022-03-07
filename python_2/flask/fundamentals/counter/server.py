from flask import Flask, render_template, request, redirect, session
from flask.sessions import NullSession

app = Flask(__name__)
app.secret_key = 'asdf;lkjzxcvmnbpoiuqwerty' # set a secret key for security purposes

# our index route will handle rendering our form
@app.route('/')
def views():
    if 'page_views' in session:
        session['page_views'] += 1
    else:
        session['page_views'] = 0

    return render_template("index.html")

@app.route('/add_two')
def plus_two():
    if 'page_views' in session:
        session['page_views'] += 1
    else:
        session['page_views'] = 2
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

