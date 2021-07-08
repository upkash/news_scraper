import requests
from database import session
from bs4 import BeautifulSoup
import threading 
import queue
from models import Article, Image, Link
from textblob import TextBlob


def handle_story(story, s, q) -> None:
    h = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
        'Accept-Language': 'en-us',
        'Referer': 'https://money.usnews.com/',
        'Connection': 'keep-alive'
    }
    s.headers.update(h)
    r = s.get(story['permalink'])
    soup = BeautifulSoup(r.text, 'html.parser')
    text = soup.find_all('div', attrs={'class':'Raw-slyvem-0'})
    body = ''
    links = []
    for div in text:
        try:
            for a in div.find_all('a', href=True):
                # print(a.text, a['href'])
                links.append(Link(a['href'], a.text))
            body += div.find('p').text
        except:
            pass
    tb = TextBlob(body)
    article = Article(story['headline'], body, story['permalink'], tb.sentiment.subjectivity, tb.sentiment.polarity)
    article_links = []
    for key in story['image']:
        try:
            if 'https' in str(story['image'][key]):
                article_links.append(Image(story['image'][key], key))
        except Exception as e:
            print("ERROR")
            print(e)
            print(story['image'])
    article.images = article_links
    article.links = links
    q.put(article)
    list(map(q.put, links))
    list(map(q.put, article_links))



def main():
    s = requests.Session()


    headers = {
        # 'Cookie': '',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Host': 'www.usnews.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
        'Accept-Language': 'en-us',
        'Referer': 'https://www.usnews.com/topics/subjects/stock-market',
        'Connection': 'keep-alive',
    }

    s.headers.update(headers)

    cookie_res = s.get('https://www.usnews.com/topics/subjects/stock-market')

    stories = queue.Queue()
    for i in range(0, 40, 10):
        print('ground')
        
        r = s.get('https://www.usnews.com/topics/subjects/stock-market?offset='+str(i)+'&renderer=json')
        print(len(r.json()['stories']))
    

        threads = []

        for i in range(len(r.json()['stories'])):
            thread = threading.Thread(target=handle_story, args=(r.json()['stories'][i],requests.Session(),stories,))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()


    session.bulk_save_objects(list(stories.queue))
    session.commit()

if __name__ == '__main__':
    # handle_story('https://money.usnews.com/investing/stock-market-news/articles/should-you-buy-airbnb-stock', requests.Session())
    main()