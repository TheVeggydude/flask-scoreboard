from flask import render_template
from database.exercise import Exercise as Exercise


def view_exercises():
    exercises = Exercise.query.order_by(Exercise.index.asc()).all()
    exercises = None if len(exercises) is 0 else exercises

    return render_template('exercises.html', exercises=exercises)
