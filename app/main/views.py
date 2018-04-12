from flask import render_template
from . import main
from ..requests import get_top_news

@main.route('/')
def index():
    top_news = get_top_news()
    return render_template('home.html', top_news = top_news)