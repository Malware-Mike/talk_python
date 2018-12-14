import requests
import datetime
import collections

url = 'http://consumer_services_api.talkpython.fm/api/blog'
resp = requests.get(url)
data = resp.json()
count = 0
for index, post in enumerate(data):
    print("Index: {}".format(index))
    print("Title: {}".format(data[index]['title']))
    print()

