from flask import Flask, jsonify
from database import session
from models import Article, Link, Image

app = Flask(__name__)


@app.route('/api/get_articles')
def get_articles():

    articles = session.query(Article).all()
    out = []
    for a in articles:
        out.append(a.json)
    return jsonify(out)

