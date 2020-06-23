from gnewsclient import gnewsclient
from engine import *
def news(topic):
    client = gnewsclient.NewsClient(language='english', location='india', topic=topic, max_results=3)
    n=[i['title'] for i in client.get_news()]
    for i in n:
        speak(i)