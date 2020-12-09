from flask import Flask, render_template
from repositories import task_repository

# we gonna import Blueprint from flask
from flask import Blueprint

# we're creating an instance of Blueprint
# we gonna register this blueprint with our application

tasks_blueprint = Blueprint("tasks", __name__)

# INDEX

@tasks_blueprint.route('/tasks')
def tasks():
    # get all tasks from DB
    tasks = task_repository.select_all()
    return render_template("tasks/index.html", all_tasks=tasks)

# NEW
# GET '/tasks/new'
# RETURN to the browser a new HTML form
@tasks_blueprint.route('/tasks/new')
def new_task():
    return render_template("tasks/new.html")

# CREATE
# POST '/tasks'

# SHOW
# GET '/tasks'<id>

# EDIT
# GET '/tasks'<id>/edit'

# UPDATE
# POST '/tasks'<id>

# DELETE
# POST '/tasks'<id>