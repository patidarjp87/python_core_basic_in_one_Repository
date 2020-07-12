import requests
r=requests.get("https://covid19india.org")
print(r.text)
