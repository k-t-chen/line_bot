from __future__ import unicode_literals

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextSendMessage

import configparser

from apscheduler.schedulers.blocking import BlockingScheduler
import urllib
import datetime

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('key_from_line')

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', minute='*/2')
def scheduled_job():
    print('========== APScheduler CRON =========')
    print('This job runs every weekday */2 min.')
    print(f'{datetime.datetime.now().ctime()}')
    print('========== APScheduler CRON =========')

    url = "https://robotappline.herokuapp.com/"
    conn = urllib.request.urlopen(url)

    for key, value in conn.getheaders():
        print(key, value)
        

@sched.scheduled_job('cron', day_of_week='mon-sun', minute='*/2')
def scheduled_job():
    print('========== APScheduler CRON =========')
    print('This job is run every weekday at 6:30')
    print('========== APScheduler CRON =========')

    line_bot_api.push_message('', TextSendMessage(text='Good Morning!'))
    line_bot_api.push_message('', TextSendMessage(text='Good Morning!'))



sched.start()