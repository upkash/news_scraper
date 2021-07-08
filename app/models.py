from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
base = declarative_base()

class Article(base):
    __tablename__ = 'articles'
    id = Column(Integer(), primary_key=True)
    title = Column(String(100))
    body = Column(String(100000))
    permalink = Column(String(150))
    timestamp = Column(DateTime())
    subjectivity = Column(Float())
    polarity = Column(Float())
    images = relationship("Image", cascade='all, delete')
    links = relationship("Link", cascade='all, delete')


    @property
    def json(self) -> dict:
        return {
                    'title' : self.title,
                    'body' : self.body,
                    'permalink' : self.permalink,
                    'timestamp' : self.timestamp,
                    'subjectivity' : self.subjectivity,
                    'polarity' : self.polarity,
                }

    def __str__(self) -> str:
        return self.title


    def __init__(self, title, body, permalink, subjectivity, polarity) -> None:
        self.title = title
        self.body = body
        self.permalink = permalink
        self.timestamp = datetime.now()
        self.subjectivity = subjectivity
        self.polarity = polarity
        

class Image(base):
    __tablename__ = 'images' 
    id = Column(Integer(), primary_key=True)
    url = Column(String(150))
    tag = Column(String(100))
    article_id = Column(Integer(), ForeignKey('articles.id'))
    
    def __init__(self, url, tag ) -> None:
        self.url = url
        self.tag = tag
        

class Link(base):
    __tablename__ = 'links'
    id = Column(Integer(), primary_key=True)
    url = Column(String(1000))
    text = Column(String(300))
    article_id = Column(Integer(), ForeignKey('articles.id'))


    def __init__(self, url, text) -> None:
        self.url = url
        self.text = text
        


