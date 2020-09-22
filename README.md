# realtime telegram push alarm
![image](https://user-images.githubusercontent.com/45138206/93852677-6d55a700-fced-11ea-985a-d31a56cdbf2a.png)

# How it works
crwals bachelor, notice, project, job 4 boards every 10 seconds. when title is changed or there are new writings, give push alarm to telegram. It contains board name, date, title, tinyurl. if users click a tinyurl, redirect to a original url.

# Installation
1. download telegram application. Users need telegram token , chat_id and revise code.
![설정방법](https://user-images.githubusercontent.com/45138206/93852868-c7ef0300-fced-11ea-9220-6a2b9f97d1ce.png)

```python
<cnu_realtime_notification_.py>
telegram_token = 'input your telegram_token'
telegram_chat_id = 'input your chat_id'
```

### telegram token  
1. enters in BotFather  
2. input /newbot, yourname, *bot  
3. get telegram token  

### telegram chat_id  
1. enters in get_id_bot  
2. input /my_id  
3. get telegram chat_id  

2. install libraries in EC2
```
$sudo apt-get update
$sudo apt-get install python3-pip
$pip3 install requests bs4 python-telegram-bot apscheduler
```
