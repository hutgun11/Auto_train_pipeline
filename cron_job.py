
import time
# import atexit
# from apscheduler.schedulers.background import BackgroundScheduler
import requests
from datetime import datetime
import schedule

def send_chart():
    date=str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    url ='https://notify-api.line.me/api/notify'
    token='WdvCQWsmZyV6dZGvSctOtuiyawh2OQxleHLpeTtSrwh'
    img={'imageFile':open('chart.png','rb')}
    data = {'message':date}
    headers= {'Authorization':'Bearer '+token}
    session = requests.Session()
    session_port = session.post(url,headers=headers,files=img,data=data)
    
#schedule.every(10).seconds.do(send_chart)
schedule.every(6).hours.do(send_chart)

i = 0
while True:
    schedule.run_pending()
    #print(i)
    time.sleep(1)
    #i = i+1
