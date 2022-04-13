from newsapi.newsapi_client import NewsApiClient  #library to fetch news from various sources
from win10toast import ToastNotifier
from tkinter import *
newsapi = NewsApiClient(api_key='c19e0447ec0d4eca9ea7c7e9e685f338')




t = Tk()
t.title('News Notifier')
t.geometry("500x300")

photo=PhotoImage(file="new-ew.png")
img_label=Label(image=photo)
img_label.pack()

t_label = Label(t, text="Click to receive COVID-19 news",font=("poppins", 10))
t_label.place(x=130, y=40)

def news():
 news_sources = newsapi.get_sources()   #returns source website of news
 for source in news_sources['sources']:
        print(source['name'])

 top_headlines = newsapi.get_top_headlines(  
    q='Covid' or 'Omicron',                  
    language='en',
   
 )
 for article in top_headlines['articles']:
    

    title=article['title']
    desc=article['description']
    message="Title: "+ title, "Description: "+desc,
    messg=str(message)
    toaster = ToastNotifier()
    toaster.show_toast("Latest Updates! ", msg=messg , duration = 6, icon_path ="news.ico")
                                   




but = Button(t, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
             relief="raised", command=news)
but.place(x=170, y=230)

t.resizable(0,0)
t.mainloop()