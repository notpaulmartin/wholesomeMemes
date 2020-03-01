'''
File:          insta.py
Project:       htb2020-memebot
File Created:  Sunday, 1st March 2020 12:02:18 am
Author(s):     Paul Martin

Last Modified: Sunday, 1st March 2020 4:10:08 am
Modified By:   Paul Martin
'''

import os
from dotenv import load_dotenv
from instabot import Bot

load_dotenv()

IMG_DIR = './memes'

HASHTAGS = "#memes #memesdaily #memesfordays #memes4ever #memesbelike #memes4life #memesarelife #memesdank #wholesome #wholesomememes #wholesomebfmemes #wholesomegfmemes #wholesomenemes #happy #funny #funnymemes #funnypicture #funnymoments #cute"

insta_uname = os.getenv("INSTA_USERNAME")
insta_pw = os.getenv("INSTA_PW")

bot = Bot()
bot.login(username=insta_uname, password=insta_pw)


def upload(filename:str, caption:str=""):
    filepath = f"{IMG_DIR}/{filename}"
    description = caption + "\n\n\n" + HASHTAGS
    
    bot.upload_photo(
        filepath,  
        caption=description
    )

if __name__ == "__main__":
    upload('0mdbycr1bel21.jpg', "")