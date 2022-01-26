# Controller will be built Wednesday

from flask_app import app # NEED this line for app.route() among other things
from flask import render_template, redirect, request
from flask_app.models import ninja, dojo # Import your models here

# Controllers contan all the logic for all your routes.  They call on the models, which
# will handle all the interactions with the database.

# We will be using @app.route() here.

# Let's figure out the routes we'll need in these controllers - along with whether it's a GET or POST request:
# 1A. Show all ninjas
# 1B. Show one ninja - with a team
# 2A. Page with form to add a ninja
# 2B. Route to actually add to database
# 3A. Page to edit a ninja
# 3B. Route to edit in the database
# 4. Delete a ninja

# we'll write out the logic in the lecture.

@app.route("/ninjas")
def show_all_ninjas():
    all_ninjas = ninja.Ninja.grab_all_ninjas_with_dojos() # We'll link teams in the lecture!
    return render_template("all_ninjas.html", all_ninjas = all_ninjas)

@app.route("/ninjas/<int:id>")
def show_one_ninja(id):
    data = {
        "id": id
    }
    one_ninja = ninja.Ninja.grab_one_ninja_with_team(data)
    return render_template("show_ninja.html", this_ninja=one_ninja)

# Page to SHOW THE FORM where you will add a ninja
@app.route("/ninjas/new")
def show_add_ninja_form():
    all_dojos = dojo.Dojo.grab_all_dojos()
    return render_template("add_ninja.html", all_dojos = all_dojos)

# Route to add the ninja to the DATABASE
@app.route("/ninjas/add_to_database", methods=["POST"])
def add_ninja_to_db():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"],
    }
    ninja.Ninja.create_one(data)
    return redirect("/dojos")

# Route tp show the form where we'll edit an individual ninja
@app.route("/ninjas/<int:id>/edit_page")
def edit_ninja_form(id):
    data = {
        "id": id
    }
    all_teams = team.Team.grab_all_teams()
    this_ninja = ninja.ninja.grab_one_ninja_with_team(data) # This WILL change so the team IS added
    return render_template("edit_ninja.html", this_ninja = this_ninja, all_teams = all_teams)

# Route to edit in the DATABASE
@app.route("/ninjas/<int:id>/edit", methods=["POST"])
def edit_ninja_in_db(id):
    data = {
        "id": id, # Need to pass in the ninja id to know which one we'll edit
        "first_name": request.form["first_name"], 
        "last_name": request.form["last_name"], 
        "number": request.form["number"],
        "position": request.form["position"], 
        "team_id": request.form["team_id"],
    }
    ninja.ninja.edit_one_ninja(data)
    return redirect("/ninjas")

# Route to edit in the DATABASE
@app.route("/ninjas/<int:id>/delete", methods=["POST"])
def delete_ninja(id):
    data = {
        "id": id
    }
    delete_ninja(data)