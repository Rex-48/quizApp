import requests

url = "https://opentdb.com/api.php?amount=20&category=18"

respose = requests.get(url)

data = respose.json()

result = data['results'] 

print(result)