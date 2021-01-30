import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
import json

broadcast=""
# data = pd.read_csv("contacts.csv")
# data_dict = data.to_dict('list')
# leads = data_dict['LeadNumber']
# messages = data_dict['Message']
usernames=[]
userphones=[]
with open('new.json') as json_file:
    data = json.load(json_file)
    for u in data:
        usernames.append(u['username'])
    for p in data:
        userphones.append(u['userphone'])


combo = zip(usernames,userphones)
first = True
for username,userphone in combo:
    time.sleep(10)
    web.open("https://web.whatsapp.com/send?phone="+str(userphone.replace('0', "+234", 1))+"&text="+"""
Hello.
Good evening {}
 I'm Theophilus from ojaa.me.
I got your number from olist.
 I run an online market place known as ojaa.me.
And we need you to place your items on this online market place.
It comes with a lot of features actually
 ojaa.me.
It's and online growing market place where you can sell your products for free. 

Benefits are
1. You get a free web page (website) for your business.
2. More customers.
3. People don't need to call or message you before you get orders. You only get orders from people who have paid for your products.
It only charges a stipend of 5'%' from every customer purchase.
It offers a prepaid service to customers thus purchasing customers pay for the item they purchase but this doesn't include delivery. The company selling the items would need to  sort out the item delivery themselves.
 Note: To avoid fraudulent activities ojaa.me doesn't make payment to the selling company until the customer has indicated that the product is received.
 Due to our nice referral system the web application has the tendency to attract many customers to ur online store thus increasing your revenue.
 Does it fits your business model?



 To get started. Simply visit ojaa.me

Click create store
 How it works is simply.
Create an account.
Click https://ojaa.me/create/form 
Fill all the required information and come back to tell me thanks.
Because it will really help your business.
 And don't hesitate to share your new website link with others
""".format(username))
    if first:
        time.sleep(6)
        first=False
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(8)
    pg.press('enter')
    time.sleep(8)
    pg.hotkey('ctrl', 'w')
