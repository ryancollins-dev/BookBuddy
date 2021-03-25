# Book Buddy
# Author: R.
# Reading timer for a random selection of books. 
# 12-1-2020
# Requirments
# https://gitea.com/chopin42/countdown > pip install countdown-timer
# https://github.com/jithurjacob/Windows-10-Toast-Notifications > pip install win10toast

import random
from countdown import countdown
from sys import platform
from win10toast import ToastNotifier

toaster = ToastNotifier()

a = []
with open("topics.txt", "r") as f:
  a = f.readlines()
print("Let's read a good book, how about?:",random.choice(a)),
input("Press Enter to Start timer")
countdown(30),
if platform == "win32":
    toaster.show_toast("Finished!", "Well done, have a Good Day!", threaded=True,
                   icon_path=None, duration=3) # 4 seconds
#else:
#    print("Finished!, Well done, have a Good Day!")