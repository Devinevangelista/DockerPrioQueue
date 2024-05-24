import requests

BASE = "http://127.0.0.1:5000/"

#send a get request to the url that is BASE + helloworld
response = requests.get(BASE + "helloworld")
print(response.json())