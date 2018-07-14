from scoreboard import flask_app
from controller import view_exercises


@flask_app.route('/')
@flask_app.route('/index')
def index():
    return view_exercises()
