import secret_api
import requests

api_key = secret_api.congress_gov_api

requests.get('https://api.congress.gov/v3/bill?api_key=' + api_key)

url = "https://api.congress.gov/v3/bill?format=xml&offset=0&limit=250&sort=updateDate%2Basc&api_key=" + api_key
headers = {"accept": "application/xml"}

response = requests.get(url,headers=headers)

response.raise_for_status()

print(response.text)
