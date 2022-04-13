import requests  #to access the webpage
from pygame import mixer 
from datetime import datetime, timedelta
import time
from win10toast import ToastNotifier



age = int(input("ENTER YOUR AGE: "))

if age<15:

    print("You need to be over the age of 15 to be eligible for the vaccine.")

else:

#pincodes = ["421301"]

 pincodes=[]

 for i in range(0,1):
    print("ENTER YOUR PINCODE: ")
    pcd=(input())
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
                                   

                                    pincd= pincode
                                    vaxdate= str(given_date)
                                    centername= (center["name"])
                                    cname=str(centername)
                                    blockname= (center["block_name"])
                                    bname=str(blockname)
                                    price= center["fee_type"]
                                   

                                    # message="Pincode: "+pincd, "Date: "+vaxdate, "Center Name: " +cname, "Block Name: " +bname, "Price: " +price

                                    # messg=str(message)

                                    # toaster = ToastNotifier()
                                    # toaster.show_toast("Vaccine Slot Available! ", msg=messg , duration = 3, icon_path ="Vaccine.ico")
                                    

                                    if(session["vaccine"] != ''):
                                        vactype = session["vaccine"]

                                    message="Pincode: "+pincd, "Date: "+vaxdate, "Center Name: " +cname, "Block Name: " +bname, "Price: " +price, "Vaccine: " +vactype

                                    messg=str(message)

                                    toaster = ToastNotifier()
                                    toaster.show_toast("Vaccine Slot Available! ", msg=messg , duration = 3, icon_path ="Vaccine.ico")
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