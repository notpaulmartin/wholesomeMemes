'''
File:          sched.py
Project:       htb2020-memebot
File Created:  Sunday, 8th March 2020 10:36:05 pm
Author(s):     Paul Martin

Last Modified: Sunday, 8th March 2020 10:56:46 pm
Modified By:   Paul Martin
'''

import subprocess, schedule, time, random, math

def post():
    # Wait another 1s - 20min until post to not get detected as bot
    delay = random.randrange(65, 60*20)
    print(f"** Waiting for another {math.floor(delay/60)}min {delay%60}s")
    #time.sleep(delay)

    subprocess.call(["python", "main.py"])


if __name__ == "__main__":
    post_time = "22:57"
    schedule.every().day.at(post_time).do(post)
    print(f"** Waiting until {post_time}")

    while True:
        schedule.run_pending()
        time.sleep(30)