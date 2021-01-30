import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
import json


#initialized  lists to store usernames and numbers inother to zip them and loop through them simultaneausly and respectively
usernames=[]
userphones=[]

# opened json file consisting of names and contact of potential vendors
with open('unique_olist.json') as json_file:
    data = json.load(json_file)
    # in other for there to be a break filterd the first 50 contacts should only be sent invitation messages 
    for u in data[:50]:
        usernames.append(u['username'])
    for p in data:
        userphones.append(p['userphone'])

combo = zip(usernames,userphones)
first = True
no=0
for username,userphone in combo:
    time.sleep(10)
    file = open("sample.txt")
    web.open("https://web.whatsapp.com/send?phone="+str(userphone.replace('0', "+234", 1))+"&text="+file.read().replace("name", username)
)
    if first:
        time.sleep(6)
        first=False
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(8)
    pg.press('enter')
    time.sleep(8)
    pg.press('enter')
    no+=1
    print(no)
    pg.hotkey('ctrl', 'w')