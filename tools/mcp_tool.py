import requests

def get_health_news():

    url = "https://newsapi.org/v2/top-headlines?category=health"

    response = requests.get(url)

    return response.json()