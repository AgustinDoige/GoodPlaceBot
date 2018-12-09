import praw
import datetime
import pytz
import json
from time import sleep
from sidebarCountdown import updateSidebar
"""

Main.py should:
- Update the sidebar every 1-5minutes [DONE]
- Read the latest comments for calls for the Bot to tell them their points as often as possible
- Read the latests comments and give them points based on the Rules every every 5-10 minutes
- Read the latests submissions and give them points based on the Rules every 3-8 minutes
- Log every action
- Change the user logs to reflect their history and total points
- At the end of each week it should update the flairs and the ranking on the sidebar

Files that main.py will require:
 - rules.txt  a json file that stores hard/soft rules with their respective points and how often they should award points
 - bookOfUsers.txt a json file that stores every user, their point logs and their current points

External files that help the running: 
 - ruleMaker.py : helps update the rules.txt file
 - logReader.py : helps read the userbook.txt and dump their logs


"""

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('TheGoodSandbox') # Test sub: TheGoodSandbox
print("Logged into r/{}".format(subreddit.title))

sleepTime = 5
while True:
	updateSidebar(subreddit,sleepTime)
	sleep(sleepTime)