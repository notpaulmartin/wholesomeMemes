'''
File:          main.py
Project:       htb2020-memebot
File Created:  Sunday, 1st March 2020 1:00:07 am
Author(s):     Paul Martin

Last Modified: Sunday, 1st March 2020 2:15:54 pm
Modified By:   Paul Martin
'''
import schedule, time

import insta, reddit
import colour_utils as utils

def auto_post():
    img_names = reddit.get_newest_memes(1)
    # img_names = ["e1cnz3bhu7g31.jpg", "ghbyqn3xhs531.jpg"]

    print('** Downloaded from Reddit:')
    print(img_names)

    for img_name in img_names:
        main_colour = utils.get_main_colour(img_name)
        squared_img = utils.square(img_name, main_colour)

        squared_img.save(f"{utils.IMG_DIR}/squared/{img_name}.jpg")
        insta.upload(f"squared/{img_name}.jpg", "")
    
    print('** Posted on Instagram')

if __name__ == "__main__":
    schedule.every().day.at("11:30").do(auto_post)

    while True:
        schedule.run_pending()
        time.sleep(30)

    # auto_post()