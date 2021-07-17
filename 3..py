import requests
from datetime import datetime, timedelta
from pprint import pprint

date = datetime.now() - timedelta(days=2)
params = {'tagged': 'python',
          'fromdate': int(date.timestamp()),
          'sort': 'activity',
          'order': 'desc',
          'site': 'stackoverflow'
          }
link = r'https://api.stackexchange.com/2.3/questions'
response = requests.get(link, params=params).json()
for question in response['items']:
    pprint(question['title'])
