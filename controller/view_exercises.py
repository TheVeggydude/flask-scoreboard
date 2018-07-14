from flask import render_template
from database.exercise import Exercise as Exercise


def view_exercises():
    exercises = Exercise.query.all()
    print(exercises)
