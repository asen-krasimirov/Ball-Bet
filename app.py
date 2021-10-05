from api_calls import get_fixtures_data, get_fixtures_by_club_name, sort_data_by_round
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/fixtures')
def fixtures_page():

    club_name = request.args.get('club-name')
    if club_name is not None:
        data = get_fixtures_by_club_name(club_name)
    else:
        data = get_fixtures_data()

    data = sort_data_by_round(data)
    return render_template('fixtures.html', rounds=data)


@app.route('/standings')
def standings_page():
    return 'standings page...'


@app.route('/events')
def events_page():
    return 'events page...'


if __name__ == '__main__':
    app.run()
