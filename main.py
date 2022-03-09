import requests
import tweepy
from bs4 import BeautifulSoup
import time
import key


base_article = ""
sec_base_article = ""

base_temp_variable = ""
sec_base_temp_variable = ""

articles_variable = []
sec_articles_variable = []


auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_secret)
auth.set_access_token(key.access_token, key.access_token_secret)

api = tweepy.API(auth)

twitter_ids = [""] #set id/ids of profile to send message


def ats():
    global base_article, base_temp_variable, articles_variable

    urls = "https://atsmods.lt"

    source = requests.get(urls).text

    soup = BeautifulSoup(source, "html.parser")

    articles = soup.find_all("article")

    if articles != articles_variable:
        for i, article in enumerate(articles):
            if i == 0:
                base_article = article.find("h2", class_="entry-title").string
            article_title = article.find("a", {"rel": "category tag"}).string
            check_titles = ("AI traffic", "Maps", "Trucks")
            article_name = article.find("h2", class_="entry-title").string
            article_link = article.find(
                "h2", class_="entry-title").find(href=True)
            if (article_name == base_temp_variable):
                break
            else:
                if article_title in check_titles:
                    for twitter_id in twitter_ids:
                        api.send_direct_message(
                            recipient_id=twitter_id, text=f"⚠️ATS - {article_title}\n❗️ {article_name} ❗️\n\n🌝Link - {article_link['href']}")

        base_temp_variable = base_article

        articles_variable = articles


def ets():
    global sec_base_article, sec_base_temp_variable, sec_articles_variable

    urls = "https://ets2.lt/en/"

    source = requests.get(urls).text

    soup = BeautifulSoup(source, "html.parser")

    articles = soup.find_all("article")

    if articles != sec_articles_variable:
        for i, article in enumerate(articles):
            if i == 0:
                sec_base_article = article.find(
                    "h2", class_="entry-title").string

            article_title = article.find("a", {"rel": "category tag"}).string
            check_titles = ("AI traffic", "Maps", "Trucks")
            article_name = article.find("h2", class_="entry-title").string
            article_link = article.find(
                "h2", class_="entry-title").find(href=True)
            if (article_name == sec_base_temp_variable):
                break
            else:
                if article_title in check_titles:
                    for twitter_id in twitter_ids:
                        api.send_direct_message(
                            recipient_id=twitter_id, text=f"⚠️ETS2 - {article_title}\n❗️ {article_name} ❗️\n\n🌝Link - {article_link['href']}")

        sec_base_temp_variable = sec_base_article

        sec_articles_variable = articles


while True:
    ats()
    ets()
    time.sleep(10)
