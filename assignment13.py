import requests
resp=requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en")
print(resp.status_code)
import json
datata=resp.json()
print(type(datata))
print(datata["quoteText"])
