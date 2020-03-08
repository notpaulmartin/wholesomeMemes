'''
File:          sched.py
Project:       htb2020-memebot
File Created:  Sunday, 8th March 2020 10:36:05 pm
Author(s):     Paul Martin

Last Modified: Sunday, 8th March 2020 10:39:57 pm
Modified By:   Paul Martin
'''

import subprocess, schedule

def post():
    # Wait another 1s - 20min until post to not get detected as bot
    delay = random.randrange(65, 60*20)
    print(f"** Waiting for {math.floor(delay/60)}min {delay%60}s")
    time.sleep(delay)

    subprocess.call("python main.py")


if __name__ == "__main__":
    schedule.every().day.at("11:30").do(post)

    while True:
        schedule.run_pending()
        time.sleep(30)