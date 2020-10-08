import requests

url = "https://www.googleapis.com/youtube/v3/search?part=snippet&q=rick%20roll&key=APIKEY"

payload = {}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
