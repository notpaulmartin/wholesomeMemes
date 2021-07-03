"""
File:          main.py
Project:       htb2020-memebot
File Created:  Sunday, 1st March 2020 1:00:07 am
Author(s):     Paul Martin

Last Modified: Saturday, 3rd July 2021 12:54:47 pm
Modified By:   Paul Martin
"""
import os

import insta, reddit
import colour_utils as utils


def auto_post():
    # Wait another 1s - 20min until post to not get detected as bot
    # delay = random.randrange(65, 60*20)
    # time.sleep(delay)

    # Delete all previous memes
    [
        os.remove(f"{utils.IMG_DIR}/{f}")
        for f in os.listdir(utils.IMG_DIR)
        if f.endswith((".png", ".jpg"))
    ]
    [
        os.remove(f"{utils.IMG_DIR}/squared/{f}")
        for f in os.listdir(f"{utils.IMG_DIR}/squared")
    ]

    img_names = reddit.get_newest_memes(1)

    print("** Downloaded from Reddit:")
    print(img_names)

    for img_name in img_names:
        main_colour = utils.get_main_colour(img_name)
        squared_img = utils.square(img_name, main_colour)

        squared_img.save(f"{utils.IMG_DIR}/squared/{img_name}.jpg")
        insta.upload(f"squared/{img_name}.jpg", "")

    print("** Posted on Instagram")


if __name__ == "__main__":
    # schedule.every().day.at("11:30").do(auto_post)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(30)

    auto_post()
