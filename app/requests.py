import urllib, json
# from . models import news
# Getting api key
api_key = None
# Getting the movie base url
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']

# get top_highlights
def get_top_news():
    '''gets top news from news api'''
    get_news_url = base_url.format(api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None
        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results

# precess the result into objects
def process_results(news_list):
    news_result = []
    for news_item in news_list:
        id = news_item.get('id')
        source = news_item.get('source')
        title = news_item.get('title')
        description = news_item.get('description')
        author = news_item.get('author')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')

        # set creteria to get object
        if id and author and urlToImage:
            news_result.append(description)

    print(news_result)
    return news_result
