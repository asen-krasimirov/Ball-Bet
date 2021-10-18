import json
import os
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


def attach_club_logos(data):
    for content in data:
        content['home_logo'] = f'images/club_logos/{(content["home_name"])}.png'
        content['away_logo'] = f'images/club_logos/{(content["away_name"])}.png'


def get_fixtures_data(date='', competition_id='244'):
    def correct_time():
        for content in all_data:
            fixture_date = list(map(int, content['date'].split('-')))
            fixture_time = list(map(int, content['time'].split(':')))
            content['date'] = datetime(
                year=fixture_date[0], month=fixture_date[1], day=fixture_date[2],
                hour=fixture_time[0], minute=fixture_time[1]
            ) + timedelta(hours=3)

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
    attach_club_logos(all_data)
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


def get_all_club_names(data):
    club_names = []
    for content in data:
        home_name = content['home_name']
        away_name = content['away_name']

        if home_name not in club_names:
            club_names.append(home_name)
        if away_name not in club_names:
            club_names.append(away_name)

    return club_names


def get_group_standings(group: str, competition_id='244'):
    def group_attach_club_logos():
        for content in group_data:
            content['logo'] = f'images/club_logos/{(content["name"])}.png'

    url = 'https://livescore-api.com/api-client/leagues/table.json'
    querystring['competition_id'] = competition_id
    querystring['group'] = group

    group_data = requests.request('GET', url, params=querystring).text
    group_data = json.loads(group_data)['data']['table']

    group_attach_club_logos()
    return group_data


def get_live_matches(competition_id='244'):

    url = 'https://livescore-api.com/api-client/scores/live.json'
    querystring['competition_id'] = competition_id

    all_data = requests.request('GET', url, params=querystring).text
    all_data = json.loads(all_data)['data']['match']

    attach_club_logos(all_data)
    return all_data


def get_match_events(match_id='129180'):
    def events_attach_club_logos(data):
        data['home_logo'] = f'images/club_logos/{(data["home_name"])}.png'
        data['away_logo'] = f'images/club_logos/{(data["away_name"])}.png'

    url = 'https://livescore-api.com/api-client/scores/events.json'
    querystring['id'] = match_id

    all_data = requests.request('GET', url, params=querystring).text
    all_data = json.loads(all_data)['data']

    events_attach_club_logos(all_data['match'])
    return all_data


querystring = {
    'key': os.getenv('API_KEY'),
    'secret': os.getenv('API_SECRET'),
}
