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

            with open(os.path.join(directory, filename), 'r') as file:
                body = file.readlines()
                index = body[0]
                title = body[1]

                text = ""
                for line in body[2:]:
                    text += line

            exercise = Exercise(title=title, index=int(index), body=text, visible=True)
            db.session.add(exercise)

    db.session.commit()

    print(str(len(Exercise.query.all())) + " items now in exercise db")
