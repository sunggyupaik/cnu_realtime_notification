#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import urllib.request
import sys
from bs4 import BeautifulSoup
import telegram
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers import interval
from datetime import datetime, timedelta

now = datetime.now()

#telegram_token = 'input your telegram_token' ex)123456789:skdfk1EISKpbCV72kaiskskWKDLD-ABAW
#telegram_chat_id = 'input your chat_id' ex) 216484946

bot = telegram.Bot(token = telegram_token )
noticeList=[]
bachelorList=[]
projectList=[]
jobList=[]

def tiny_url(url):
    apiurl = "http://tinyurl.com/api-create.php?url="
    tinyurl = urllib.request.urlopen(apiurl + url).read()
    return tinyurl.decode("utf-8")

#학사공지
def bachelor():
    
    url='https://computer.cnu.ac.kr/computer/notice/bachelor.do'
    html = requests.get(url)
    soup = BeautifulSoup(html.text,'html.parser')
    
    num = soup.select('span.b-date')
    checked=False
    
    if(len(bachelorList) > 30):
        for i in 5:
            bachelorList.pop();
    
    for i in num:
        checked=False
        notice_day = i.text.strip()
        i=i.find_parent('div', class_='b-title-box')
        title = i.select_one('a').attrs['title'][:-7]
        for one_title in bachelorList:
            if one_title == title:
                checked=True
                break
            
        if checked == False:
            address=i.select_one('a').attrs['href']
            address=url+address
            result = "학사공지[" +notice_day + "]\n" + title +"\n" + tiny_url(address)
            bachelorList.append(title)
            bot.sendMessage(chat_id = telegram_chat_id, text=result)

#일반소식
def notice():
    
    url='https://computer.cnu.ac.kr/computer/notice/notice.do'
    html = requests.get(url)
    soup = BeautifulSoup(html.text,'html.parser')
    
    num = soup.select('span.b-date')
    checked=False
    
    if(len(noticeList) > 20):
        for i in 5:
            noticeList.pop();
    
    for i in num:
        checked=False
        notice_day = i.text.strip()
        i=i.find_parent('div', class_='b-title-box')
        #title=i.select_one('a').text.strip()
        title = i.select_one('a').attrs['title'][:-7]
        for one_title in noticeList:
            if one_title == title:
                checked=True
                break
            
        if checked == False:
            address=i.select_one('a').attrs['href']
            address=url+address
            result = "일반소식[" +notice_day + "]\n" + title +"\n" + tiny_url(address)
            noticeList.append(title)
            bot.sendMessage(chat_id = telegram_chat_id, text=result)
        
#사업단소식           
def project():
    
    url='https://computer.cnu.ac.kr/computer/notice/project.do'
    html = requests.get(url)
    soup = BeautifulSoup(html.text,'html.parser')
    
    num = soup.select('span.b-date')
    checked=False
    
    if(len(projectList) > 15):
        for i in 5:
            projectList.pop();
    
    for i in num:
        checked=False
        notice_day = i.text.strip()
        i=i.find_parent('div', class_='b-title-box')
        title = i.select_one('a').attrs['title'][:-7]
        for one_title in projectList:
            if one_title == title:
                checked=True
                break
            
        if checked == False:
            address=i.select_one('a').attrs['href']
            address=url+address
            result = "사업단소식[" +notice_day + "]\n" + title +"\n" + tiny_url(address)
            projectList.append(title)
            bot.sendMessage(chat_id = telegram_chat_id, text=result)

#취업정보
def job():
    
    url='https://computer.cnu.ac.kr/computer/notice/job.do'
    html = requests.get(url)
    soup = BeautifulSoup(html.text,'html.parser')
    
    num = soup.select('span.b-date')
    checked=False
    
    if(len(jobList) > 15):
        for i in 5:
            jobList.pop();
    
    for i in num:
        checked=False
        notice_day = i.text.strip()
        i=i.find_parent('div', class_='b-title-box')
        title = i.select_one('a').attrs['title'][:-7]
        for one_title in jobList:
            if one_title == title:
                checked=True
                break
            
        if checked == False:
            address=i.select_one('a').attrs['href']
            address=url+address
            result = "취업정보[" +notice_day + "]\n" + title +"\n" + tiny_url(address)
            jobList.append(title)
            bot.sendMessage(chat_id = telegram_chat_id, text=result)      
            
sched = BackgroundScheduler()
sched.add_job(bachelor, 'interval',seconds=10)
sched.add_job(notice, 'interval',seconds=10)
sched.add_job(project, 'interval',seconds=10)
sched.add_job(job, 'interval',seconds=10)
sched.start()

