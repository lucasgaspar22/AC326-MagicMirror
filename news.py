import requests
import json

NEWS_URL = "https://newsapi.org/v1/articles?source=google-news&sortBy=top&apiKey=1735e90f53c040d193e4cd76a6df0515"
news_data = None

def get_news_data():
	global news_data
	result = requests.get(NEWS_URL)
	content = result.text
	news_data = json.loads(content)
	
def get_news():
	news_list = []
	for news in news_data["articles"]:
		news_list.append(news["title"])
	return news_list
