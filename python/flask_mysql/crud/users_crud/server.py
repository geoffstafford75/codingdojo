from flask import Flask, render_template, request, redirect, session
# import the class from friend.py
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    return redirect("users")

@app.route('/users')
def users():
    users = User.get_all()
    print(users)
    return render_template("users.html", users = users)

@app.route('/users/new')
def user_form():
    return render_template("new.html")

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

@app.route('/users/update', methods=["POST"])
def update_user():
    print(request.form)
    User.update(request.form)
    return redirect("/users/show/6")

@app.route('/users/edit/<int:id>')
def edit_user(id):
    data = {
        "id": id
    }
    return render_template("edit.html",user = User.get_one(data))

@app.route('/users/show/<int:id>')
def show_user(id):
    data = {
        "id": id
    }
    return render_template("user.html",user = User.get_one(data))

@app.route('/users/delete/<int:id>')
def delete_user(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect("/users")
            
if __name__ == "__main__":
    app.run(debug=True)

