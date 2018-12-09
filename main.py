import praw
import datetime
import pytz
import json
from time import sleep
from sidebarCountdown import updateSidebar

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('TheGoodSandbox') # Test sub: TheGoodSandbox
print("Logged into r/{}".format(subreddit.title))

sleepTime = 5
while True:
	updateSidebar(subreddit,sleepTime)
	sleep(sleepTime)