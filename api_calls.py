import json
from datetime import datetime, timedelta

import requests


def sort_data_by_round(all_data):
    sorted_data = {}

    cur_index = 0
    cur_round = None
    while True:
        content = all_data[cur_index]
        if content['round'] not in sorted_data:
            cur_round = content['round']
            sorted_data[cur_round] = []

            continue

        sorted_data[cur_round].append(content)
        cur_index += 1
        if cur_index >= len(all_data):
            break

    return sorted_data


def get_fixtures_data(date='', competition_id='244'):
    def correct_time():
        for content in all_data:
            fixture_date = list(map(int, content['date'].split('-')))
            fixture_time = list(map(int, content['time'].split(':')))
            content['date'] = datetime(
                year=fixture_date[0], month=fixture_date[1], day=fixture_date[2],
                hour=fixture_time[0], minute=fixture_time[1]
            ) + timedelta(hours=3)

    def attach_club_logos():
        for content in all_data:
            content['home_logo'] = f'images/club_logos/{(content["home_name"])}.png'
            content['away_logo'] = f'images/club_logos/{(content["away_name"])}.png'

    url = 'https://livescore-api.com/api-client/fixtures/matches.json'  # Get all Fixtures URL
    querystring['competition_id'] = competition_id

    if date:  # format -> 'today' / '2021-10-19'
        querystring['date'] = date

    all_data = []

    cur_page = 1
    while True:
        """ Get all possible pages from the API. """
        querystring['page'] = str(cur_page)

        cur_data = requests.request('GET', url, params=querystring).text
        cur_data = json.loads(cur_data)['data']

        all_data += cur_data['fixtures']

        if not cur_data['next_page']:
            break

        cur_page += 1

    correct_time()
    attach_club_logos()
    return all_data


def get_fixtures_by_club_name(club_name):
    all_data = get_fixtures_data()
    collected_data = []

    for content in all_data:
        if content['home_name'] != club_name and content['away_name'] != club_name:
            continue

        collected_data.append(content)

    if not collected_data:
        collected_data = all_data

    return collected_data


api_key = 'AqwYEHLfTdMhQMWv'
api_secret = '70ezFej6TdHbhIQS9mQN3C2XPPeGCbbK'

# url = 'https://livescore-api.com/api-client/fixtures/matches.json'  # Get all Fixtures URL
# url = 'https://livescore-api.com/api-client/fixtures/matches.json?date=2021-10-19'

querystring = {
    'key': api_key,
    'secret': api_secret,
}

# __import__('pprint').pprint(get_fixtures_data())  # for debugging
