from api_calls import get_fixtures_data
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/fixtures')
def fixtures_page():
    data = get_fixtures_data()
    # __import__('pprint').pprint(data)
    return render_template('fixtures.html', rounds=data)


@app.route('/standings')
def standings_page():
    return 'standings page...'


@app.route('/events')
def events_page():
    return 'events page...'


if __name__ == '__main__':
    app.run()
