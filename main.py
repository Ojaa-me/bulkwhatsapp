import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
import json

usernames=[]
userphones=[]
with open('new.json') as json_file:
    data = json.load(json_file)
    for u in data:
        usernames.append(u['username'])
    for p in data:
        userphones.append(u['userphone'])

file = open("sample.txt")
combo = zip(usernames,userphones)
first = True
for username,userphone in combo:
    time.sleep(10)
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
    pg.hotkey('ctrl', 'w')
