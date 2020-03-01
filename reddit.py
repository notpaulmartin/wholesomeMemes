'''
File:          reddit.py
Project:       htb2020-memebot
File Created:  Saturday, 29th February 2020 7:01:39 pm
Author(s):     Paul Martin

Last Modified: Sunday, 1st March 2020 2:40:45 am
Modified By:   Paul Martin
'''

from typing import List, Dict, Any

import os, json
import praw, requests

from dotenv import load_dotenv

import insta

load_dotenv()

client_id = os.getenv("REDDIT_ID")
client_secret = os.getenv("REDDIT_SECRET")
user_agent = 'Wholesome Memepage'
target_subreddit = 'wholesomememes'
image_directory = './memes'
image_count = 1
schedule_time = '09:00'

order = 'top'
time_filter = 'day' # month, hour, day, week, year, all

order = order.lower()

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret, user_agent=user_agent)

def get_subreddit(ranking):
    if ranking == 'hot':
        return reddit.subreddit(target_subreddit).hot(limit=None)
    elif ranking == 'top':
        return reddit.subreddit(target_subreddit).top(time_filter='day')
    elif ranking == 'new':
        return reddit.subreddit(target_subreddit).new(limit=None)

def get_img(url):
    img_name = "{}/{}".format(image_directory, url.split('/')[-1])
    img = requests.get(url).content
    with open(img_name, 'wb') as f:
        f.write(img)

def get_newest_memes(n:int = 1) -> List[str]:
    c = 1
    images = []
    
    for submission in get_subreddit(order):
        url = submission.url
        if url.endswith(('.jpg', '.png', '.gif', '.jpeg')):
            images.append(url)
            c += 1
            if c > int(image_count):
                break

    img_names:List[str] = []
    for img_url in images:
        get_img(img_url)
        img_name = img_url.split('/')[-1]
        img_names.append(img_name)

    return img_names
