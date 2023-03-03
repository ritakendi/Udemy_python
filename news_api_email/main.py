import requests

api_key = "10a2b95b8fef49f7bc42c3fe80e731a5"
url = "https://newsapi.org/v2/everything?q=tesla&"\
    "from=2023-02-01&sortBy=publishedAt&apiKey="\
    "10a2b95b8fef49f7bc42c3fe80e731a5"

my_request = requests.get(url)
content = my_request.json()
for article in content["articles"]:
    print(article["title"])
