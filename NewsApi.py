import requests

api_key = 'b7ed2b2dc2b5442ebb7abeb9f4eaa4d6'
url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
json_data = requests.get(url).json()
arr = []

def news():
    for i, article in enumerate(json_data.get('articles', [])[:3]):
        arr.append(f'Number {i + 1}, {article["title"]}.')
    return arr