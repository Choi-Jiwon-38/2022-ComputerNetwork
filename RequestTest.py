import requests

URL = 'http://www.naver.com'

params = {'param1': 'value1', 'param2': 'value'}
res = requests.get(URL, params=params)
print(res.url)