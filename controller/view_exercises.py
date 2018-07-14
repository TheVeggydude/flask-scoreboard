from flask import render_template
from database.exercise import Exercise as Exercise
from json import dumps


def view_exercises():
    exercises = Exercise.query.all()
    exercises = None if len(exercises) is 0 else dumps(exercises)

    return render_template('exercises.html', exercises=exercises)
