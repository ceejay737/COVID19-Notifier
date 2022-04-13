from win10toast import ToastNotifier
from bs4 import BeautifulSoup  #pulling data out of HTML and XML files
import requests  #HTTP library for Python
import time
import os
import getpass
USER_NAME = getpass.getuser()


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\Christine\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

t = Tk()
t.title('Cases Notifier')
t.geometry("500x300")

photo=PhotoImage(file="covid.png")
img_label=Label(image=photo)
img_label.pack()

t_label = Label(t, text="Click to receive COVID-19 statistics",font=("poppins", 10))
t_label.place(x=130, y=40)


country = "India"
notification_duration = 10  #display time of the notification (in seconds)
refresh_time = 5 #time gap between two notifications ( in minutes)
data_check= []
worldmetersLink = "https://www.worldometers.info/coronavirus/"

def notif():
 def data_cleanup(array):
    L = []
    for i in array:
        i = i.replace("+","")
        i = i.replace("-","")
        i = i.replace(",",",")
        if i == "":
            i = "0"
        L.append(i.strip())
    return L

 while True:
    try:
        html_page = requests.get(worldmetersLink)
    except requests.exceptions.RequestException as e: 
        print (e)
        continue
    bs = BeautifulSoup(html_page.content, 'html.parser')

    search = bs.select("div tbody tr td")
    start = -1
    for i in range(len(search)):
        if search[i].get_text().find(country) !=-1:
            start = i
            break
    data = []
    for i in range(1,8):
        try:
            data = data + [search[start+i].get_text()]
        except:
            data = data + ["0"]
    
    data= data_cleanup(data)
    message = "Total infected = {}, New Case = {},  Total Deaths = {},  New Deaths = {}, Recovered = {},  New Recovered = {}".format(*data)



    if data_check != data:

        data_check = data
        toaster = ToastNotifier()
        toaster.show_toast("Coronavirus {}".format(country) , message, duration = notification_duration , icon_path ="Corona.ico" )
    else:
        time.sleep(refresh_time*60)
        continue



but = Button(t, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
             relief="raised", command=notif)
but.place(x=170, y=230)

t.resizable(0,0)
t.mainloop()