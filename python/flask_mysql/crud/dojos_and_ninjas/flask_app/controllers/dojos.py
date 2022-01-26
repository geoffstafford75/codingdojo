from werkzeug.wrappers import response
from flask_app import app # NEED this line for app.route() among other things
from flask import render_template, redirect, request
from flask_app.models import dojo # Import your models here

# Controllers contan all the logic for all your routes.  They call on the models, which
# will handle all the interactions with the database.

# We will be using @app.route() here.

# Let's figure out the routes we'll need in these controllers - along with whether it's a GET or POST request:
# 1A. Show all dojos
# 1B. Show one dojo - eventually with players later this week - to be added Wednesday
# 2A. Page with form to add a dojo
# 2B. Route to actually add to database
# 3A. Page to edit a dojo
# 3B. Route to edit in the database
# 4. Delete a dojo 

# we'll write out the logic in the lecture.
@app.route("/")
def index():
    return redirect("/dojos")

@app.route("/dojos")
def show_all_dojos():
    all_dojos = dojo.Dojo.grab_all_dojos()
    return render_template("all_dojos.html", all_dojos = all_dojos)

@app.route("/dojo/<int:id>/delete", methods=["POST"])
def delete_dojo(id):
    data = {
        "id": id
    }
    dojo.Dojo.delete_dojo(data)
    return redirect("/dojos")

@app.route("/dojos/<int:id>")
def show_one_dojos(id):
    data = {
        "id": id
    }
    one_dojo = dojo.Dojo.grab_one_dojo_with_ninjas(data)
    return render_template("show_dojo.html", this_dojo=one_dojo)

# Route to add the team to the DATABASE
@app.route("/dojos/add_to_database", methods=["POST"])
def add_team_to_db():
    data = {
        "name": request.form["dojo_name"],
    }
    dojo.Dojo.create_one(data)
    # print(request.form)
    return redirect("/dojos")

# Route tp show the form where we'll edit an individual team
@app.route("/dojos/<int:id>/edit_page")
def edit_dojos_form(id):
    data = {
        "id": id
    }
    this_dojo = dojo.Dojo.grab_one_dojo_without_ninjas(data)
    return render_template("edit_dojo.html", this_dojo = this_dojo)

# Route to edit in the DATABASE
@app.route("/dojos/<int:id>/edit", methods=["POST"])
def edit_dojo_in_db(id):
    data = {
        "id": id, # Need to pass in the team id to know which one we'll edit
        "name": request.form["dojo_name"],
    }
    dojo.Dojo.edit_one_dojo(data)
    return redirect("/dojos")

