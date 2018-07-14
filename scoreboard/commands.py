import os
import click

from scoreboard import flask_app, db
from database.exercise import Exercise


@flask_app.cli.command('seed_exercises')
@click.argument('directory')
def seed_exercises(directory):

    # TODO - make command safer by checking for valid files before clearing database

    Exercise.query.delete()

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):

            file = open(os.path.join(directory, filename), 'r')
            exercise = Exercise(title=filename, index=1, body=file.read(), visible=True)

            db.session.add(exercise)

    db.session.commit()

    print(str(len(Exercise.query.all())) + " items in exercise db")
