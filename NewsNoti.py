from news import NewsApiClient
from win10toast_click import ToastNotifier 
newsapi = NewsApiClient(api_key='c19e0447ec0d4eca9ea7c7e9e685f338')
news_sources = newsapi.get_sources()
for source in news_sources['sources']:
    #print(source['name'])
    top_headlines = newsapi.get_top_headlines(
    q='covid',
    language='en',
)
for article in top_headlines['articles']:
    print('Title : ',article['title'])
    print('Description : ',article['description'],'\n\n')
all_articles = newsapi.get_everything(
    q='World War',
    language='en',   
)

