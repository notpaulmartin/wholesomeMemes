'''
File:          main.py
Project:       htb2020-memebot
File Created:  Sunday, 1st March 2020 1:00:07 am
Author(s):     Paul Martin

Last Modified: Sunday, 8th March 2020 10:40:39 pm
Modified By:   Paul Martin
'''
import schedule, time, random

import insta, reddit
import colour_utils as utils

def auto_post():
    # Wait another 1s - 20min until post to not get detected as bot
    # delay = random.randrange(65, 60*20)
    # time.sleep(delay)

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
    # schedule.every().day.at("11:30").do(auto_post)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(30)

    auto_post()