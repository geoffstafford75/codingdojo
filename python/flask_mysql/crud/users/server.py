from flask import Flask, render_template, request, redirect, session
# import the class from friend.py
from user import User
app = Flask(__name__)
@app.route('/users')
def all_users():
    users = User.get_all()
    print(users)
    return render_template("read.html", users = users)

@app.route('/users/new')
def user_form():
    return render_template("create.html")

@app.route('/users/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the User class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')
            
if __name__ == "__main__":
    app.run(debug=True)

