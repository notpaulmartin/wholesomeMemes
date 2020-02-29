'''
File:          reddit_scraper.py
Project:       htb2020-memebot
File Created:  Saturday, 29th February 2020 7:01:39 pm
Author(s):     Paul Martin

Last Modified: Saturday, 29th February 2020 8:46:59 pm
Modified By:   Paul Martin
'''

from typing import Dict, Any

import os, json
import praw, requests, schedule

from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("REDDIT_ID")
client_secret = os.getenv("REDDIT_SECRET")
user_agent = 'Wholesome Memepage'
target_subreddit = 'wholesomememes'
image_directory = './memes'
image_count = 1
order = 'top'
order = order.lower()
schedule_time = '09:00'

SUBREDDIT = 'wholesomememes'
IMG_DIR = './memes'

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret, user_agent=user_agent)

def get_subreddit(ranking):
    if ranking == 'hot':
        return reddit.subreddit(target_subreddit).hot(limit=None)
    elif ranking == 'top':
        return reddit.subreddit(target_subreddit).top(limit=None)
    elif ranking == 'new':
        return reddit.subreddit(target_subreddit).new(limit=None)

def get_img(what):
    img_name = "{}/{}".format(image_directory, what.split('/')[-1])
    img = requests.get(what).content
    with open(img_name, 'wb') as f:
        f.write(img)

if __name__ == "__main__":
    c = 1
    images = []
    
    for submission in get_subreddit(order):
        url = submission.url
        if url.endswith(('.jpg', '.png', '.gif', '.jpeg')):
            images.append(url)
            c += 1
            if c > int(image_count):
                break

    for img in images:
        get_img(img)

    print('Done')
