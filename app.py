from api_calls import get_fixtures_data, get_fixtures_by_club_name, sort_data_by_round, get_all_club_names, \
    get_group_standings, get_live_matches, get_match_events

from flask import Flask, render_template, request, url_for, redirect
from tasks import send_contact_email

app = Flask(__name__)


@app.route('/')
def root_page():
    return redirect(url_for('home_page'))


@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    if request.method == 'POST':
        form = request.form.to_dict()
        is_send_successfully = send_contact_email(
            sender_email=form['sender-email'],
            message_content=form['feed-back-content'],
        )

        if not is_send_successfully:
            render_template('forms/fail_contact_result.html')

        return render_template('forms/success_contact_result.html')

    return render_template('forms/contact.html')


@app.route('/fixtures')
def fixtures_page():
    club_name = request.args.get('club-name')
    if club_name is not None:
        data = get_fixtures_by_club_name(club_name)
    else:
        data = get_fixtures_data()

    club_names = get_all_club_names(data)
    data = sort_data_by_round(data)
    return render_template('fixtures.html', rounds=data, club_names=club_names)


@app.route('/standings')
def standings_page():
    group = request.args.get('group') or 'A'
    group_data = get_group_standings(group)
    return render_template('standings.html', group_data=group_data)


@app.route('/live-matches')
def live_matches_page():
    live_matches = get_live_matches()

    return render_template('live-matches-browser.html', live_matches=live_matches)


@app.route('/live-matches/<match_id>')
def live_events_page(match_id):
    all_data = get_match_events(match_id)
    all_data['event'] = reversed(all_data['event'])

    return render_template(
        'live-match-events.html',
        match_info=all_data['match'],
        events=all_data['event']
    )


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
