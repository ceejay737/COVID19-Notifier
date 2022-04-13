import requests  #to access the webpage
from pygame import mixer 
from datetime import datetime, timedelta
import time
import sys
import os
from win10toast_click import ToastNotifier 
import webbrowser
from tkinter import *
from tkinter import messagebox

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Logo = resource_path("vax.png")

t = Tk()
t.title('Vaccine Notifier')
t.iconbitmap('Corona.ico')
t.geometry("500x300")

photo=PhotoImage(file="vax.png")
img_label=Label(image=photo)
img_label.pack()

t_label = Label(t, text="Enter age: ",font=("poppins", 10))
t_label.place(x=22, y=100)

# ENTRY - Title
title = Entry(t, width="25",font=("poppins", 13))
title.place(x=153, y=100)

def Save1():
    global age
    age=int(title.get())
    if age<15:
        messagebox.showwarning("Warning","You need to be over the age of 15 to be eligible for the vaccine.")


but1 = Button(t, text="SAVE", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=5,command=Save1)
but1.place(x=412, y=100)

# Label - Message
m_label = Label(t, text="Enter pincode: ", font=("poppins", 10))
m_label.place(x=22, y=150)

# ENTRY - Message
msg = Entry(t, width="25", font=("poppins", 13))
msg.place(x=153, y=150)

def Save2():
    global pcd
    pcd=int(msg.get())
    print(pcd)

but2 = Button(t, text="SAVE", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=5, command=Save2)
but2.place(x=412, y=150)


def vacc():
 pincodes=[]
 pincodes.append(pcd)
 num_days = 2  #checking slot availability for next two days

 print_flag = 'Y'

 print("Starting search for Covid vaccine slots!")

 actual = datetime.today()   #calculating today's date
 list_format = [actual + timedelta(days=i) for i in range(num_days)] #fetching dates from list
 actual_dates = [i.strftime("%d-%m-%Y") for i in list_format]

 

 while True:
    counter = 0   

    for pincode in pincodes:   #fetching details accroding to pincode
        for given_date in actual_dates:  #fetching details according to date

            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pincode, given_date)
            header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} 
            
            result = requests.get(URL, headers=header)

            if result.ok:
                response_json = result.json()  #using json to parse and structure the data
                if response_json["centers"]:
                    if(print_flag.lower() =='y'):
                        for center in response_json["centers"]:
                            for session in center["sessions"]:
                                if (session["min_age_limit"] <= age and session["available_capacity"] > 0 ) :
                                   

                                    pincd= str(pincode)
                                    vaxdate= str(given_date)
                                    centername= (center["name"])
                                    cname=str(centername)
                                    blockname= (center["block_name"])
                                    bname=str(blockname)
                                    price= str(center["fee_type"])
                                   

                                    # message="Pincode: "+pincd, "Date: "+vaxdate, "Center Name: " +cname, "Block Name: " +bname, "Price: " +price

                                    # messg=str(message)

                                    # toaster = ToastNotifier()
                                    # toaster.show_toast("Vaccine Slot Available! ", msg=messg , duration = 3, icon_path ="Vaccine.ico")
                                    

                                    if(session["vaccine"] != ''):
                                        vactype = str(session["vaccine"])

                                    message="Pincode: "+pincd, "Date: "+vaxdate, "Center Name: " +cname, "Block Name: " +bname, "Price: " +price, "Vaccine: " +vactype

                                    messg=str(message)

                                    toaster = ToastNotifier()
                                    toaster.show_toast("Vaccine Slot Available! ", msg=messg , duration = 3, callback_on_click=open_url,icon_path ="Vaccine.ico")
                                    print("\n")
                                    counter = counter + 1
            else:
                print("No Response!")
                
    if counter:
        print("Vaccination slot available!")
    
        mixer.init()
        mixer.music.load('dingdong.wav')
        mixer.music.play()
        print("Search Completed!")

    dt = datetime.now() + timedelta(minutes=3) #syncing data in realtime

    while datetime.now() < dt:
        time.sleep(1)

def open_url():
    
        webbrowser.open_new('https://www.cowin.gov.in/')
        print('Opening URL...')  

but = Button(t, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20, command=vacc)
but.place(x=80, y=230)

exit_button = Button(t, text="EXIT",font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20, command=t.destroy)
exit_button.place(x=290,y=230)

t.resizable(0,0)
t.mainloop()



   