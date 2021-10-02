import json

import requests


api_key = 'AqwYEHLfTdMhQMWv'
api_secret = '70ezFej6TdHbhIQS9mQN3C2XPPeGCbbK'

url = 'https://livescore-api.com/api-client/fixtures/matches.json'

# url = 'https://livescore-api.com/api-client/scores'
# url = 'http://livescore-api.com/api-client/leagues/list.json'

querystring = {

    # 'date': 'today',
    'key': 'AqwYEHLfTdMhQMWv',
    'secret': '70ezFej6TdHbhIQS9mQN3C2XPPeGCbbK',

    # 'competition_id': 566,
    # 'league_id': 174,
    'league': 174,
    # 'country_name': 'Champions League',
}

# 'country_name': 'Champions League',
# 'fixures': 'https://livescore-api.com/api-client/fixtures/matches.json?key=AqwYEHLfTdMhQMWv&amp;secret=70ezFej6TdHbhIQS9mQN3C2XPPeGCbbK&amp;league=174',
# 'league_id': '174',
# 'league_name': 'Group A',
# 'scores': 'https://livescore-api.com/api-client/scores/live.json?key=AqwYEHLfTdMhQMWv&amp;secret=70ezFej6TdHbhIQS9mQN3C2XPPeGCbbK&amp;league=174'}

data = requests.request('GET', url, params=querystring).text
# data = json.loads(data)['data']['fixtures']
data = json.loads(data)

__import__('pprint').pprint(data)
