import requests
import json
import os
import sys
import time
import datetime
import dotenv
from PIL import Image
from io import BytesIO
##load env variables

dotenv.load_dotenv()


##get env variables
API_KEY = os.getenv("API_KEY")


class News:
    def __init__(self, news_id, title, content, url, pub_date, source, source_id, source_url, source_logo):
        self.news_id = news_id
        self.title = title
        self.content = content
        self.url = url
        self.pub_date = pub_date
        self.source = source
        self.source_id = source_id
        self.source_url = source_url
        self.source_logo = source_logo
        self.image_url = ""
        

    def __str__(self):
        return "News ID: " + str(self.news_id) + "\nTitle: " + self.title + "\nContent: " + self.content + "\nURL: " + self.url + "\nPub Date: " + self.pub_date + "\nSource: " + self.source + "\nSource ID: " + self.source_id + "\nSource URL: " + self.source_url + "\nSource Logo: " + self.source_logo






def get_news(source_id):
    """
    Function that gets the json response to our url request
    """
    get_news_url = "https://newsapi.org/v2/top-headlines?sources=" + source_id + "&apiKey=" + API_KEY
    #print(get_news_url)
    get_news_response = requests.get(get_news_url)
    get_news_json = get_news_response.json()
    return get_news_json


##print(get_news("cnn"))


#turn json into a list of dictionaries
def json_to_list(json_data):
    news_list = []
    for news in json_data["articles"]:
        news_list.append(news)
    return news_list



x = json_to_list(get_news("cnn"))



#print(x[0].keys())



## request image from url
def get_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content)).resize((300,200))
    return image



class Model:
    def __init__(self, news_dict):
        self.source = news_dict["source"]
        self.author = news_dict["author"]
        self.title = news_dict["title"]
        self.description = news_dict["description"]
        self.url = news_dict["url"]
        self.urlToImage = news_dict["urlToImage"]
        self.publishedAt = news_dict["publishedAt"]
        self.content = news_dict["content"]
        #self.image = display(Image(news_dict["urlToImage"]))

    def show_news(self):
        print(self.source)
        print(self.author)
        print(self.title)
        print(self.description)
        print(self.url)
        print(self.urlToImage)
        print(self.publishedAt)
        print(self.content)
        #display(Image(self.urlToImage))



def show_news(news):
    for i in range(0,5):
        print(news[i]["title"])
        print(news[i]["content"])
        print(news[i]["url"])
        print(news[i]["publishedAt"])
        print(news[i]["source"]["name"])
        #print(news[i]["urlToImage"])
        #display(Image(news[i]["urlToImage"]))
        get_image(news[i]["urlToImage"])

#show_news(json_to_list(get_news("cnn")))
#show_news(x)
def news_source(source_id):
    return json_to_list(get_news(source_id))