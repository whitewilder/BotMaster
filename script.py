import requests
import time
import schedule
from datetime import datetime

def time1():
    now = datetime.now()
    bot_token='1882490416:AAH9c4S-_ez4J9a-AKaIxj6nm2NA_qhtYLU'
    bot_chatID='715631635'
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    num = int(current_time[3:5])
    if (num % 2) == 0:
        price="This is Even number minute " + " is "+ str(num)
        price=str(price.encode('utf-8','ignore'),errors='ignore')
        send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + price
        response=requests.get(send_text)
        

    else:
        print("Minute {0} is Odd".format(num))
        
        


schedule.clear()
schedule.every(59).seconds.do(time1) 

    

while True:
    schedule.run_pending()
    time.sleep(1)
