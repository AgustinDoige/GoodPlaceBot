#!/usr/bin/python
import praw
import datetime
import pytz
import json
from time import sleep

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('TheGoodPlace') # Test sub: TheGoodSandbox

print("Logged into r/{}".format(subreddit.title))

timeZone = 'US/Eastern' # Google "pytz timezones" for other options
dummydate = datetime.datetime.now(tz=pytz.timezone(timeZone)) # This is needed for the .replace(tzinfo=dummydate.tzinfo) method
sleepTime = 120   #Time (in seconds) the program will wait to loop again

try:
	with open("episodeSchedule.txt","r") as f:
		# Schedule format in file:        YYYY - MM - DD - TT:TT AM  
		""" NOTE: The variable 'timeZone' is the timezone of the dates in this file.
		        Change variable if needed and keep dates in the file on the same timezone."""
		f.readline() # This is so it ignores the first line of the file which reminds about the format
		temp = f.readlines()
		scheduleDates = [] # List that will store all dates from file
		for st in temp:
			# (1) : Creates a naive date with the parsed info from episodeSchedule.txt
			# (2) : Turns naive date into an aware (with timezone) one 
			parsed_date = datetime.datetime.strptime(st.rstrip(),'%Y - %m - %d - %I:%M %p') # (1)
			scheduleDates.append(parsed_date.replace(tzinfo=dummydate.tzinfo)) # (2)
		del temp #This deletes the temporal list to free a small amount of memory	
except FileNotFoundError:
	print("Error. File 'episodeSchedule.txt' not found.")
	raise FileNotFoundError

while True:
	oldSidebar = subreddit.mod.settings()["description"] # Requests the current sidebar
	sidebarSectionB = oldSidebar.split("___",1)[1] # Saves the sidebar part that doesn't change as a string

	currentDate = datetime.datetime.now(tz=pytz.timezone(timeZone)) # Gets current time on chosen timezone

	# Crafts a message log for the console
	m1 = "Updating Sidebar - {} time: ".format(timeZone)
	m2 = currentDate.strftime('%H:%M:%S')
	m3 = " Local time: {}".format(datetime.datetime.now().strftime('%H:%M:%S'))
	m4 = " - Next update programed in {} sec.".format(sleepTime)
	print(m1+m2+m3+m4)

	remainingTime = []
	pastEpisodes = []
	for date in scheduleDates:
		# print("Dates;",date)
		dlt = date - currentDate
		totalSec = dlt.total_seconds()
		if (totalSec >= 0): #This makes sure that it only takes into account future dates
			remainingTime.append(dlt)
			# print("Remaining Dates:",date - currentDate)
		else:
			pastEpisodes.append(abs(totalSec)) #This adds already past dates to a list. This is for the grace period

	if (remainingTime == []): # This is where there're no future dates
		newSidebar = "Next episode air date: To be announced  \n___"+sidebarSectionB
		subreddit.mod.update(description=newSidebar)
		break

	elif(min(pastEpisodes) < 86400): # Grace Period: If an episode has aired in the las 42h it will show this message. 
		newSidebar = "The new episode is out now!  \n___"+sidebarSectionB
		subreddit.mod.update(description=newSidebar)
		print("Last episode aired in the last {} seconds ({} hours).".format(min(pastEpisodes),int((min(pastEpisodes) - min(pastEpisodes)%3600)/3600)))
		print("Sleeping for 20000 seconds")
		sleep(20000)

	else: # General most common case. A schedule past date is beyond the grace period and there are still dates in the schedule
		delta = min(remainingTime)  # This takes the date closest to the current time
		days = delta.days
		hours = int((delta.seconds - delta.seconds%3600)/3600)
		minutes = int((delta.seconds%3600)/60)

		"""What follows is a rule to display the countdown in a simple way. 
			It is equivalent, but displays a better message that this 1 line of code:
		countdown = "**{0}** day{1}, **{2}** hour{3} and **{4}** minute{5}".format(delta.days, "s"*(delta.days != 1), hours, "s"*(hours != 1),  minutes, "s"*(minutes != 1))
			"""
		if (days > 1):
			dayString = "**{}** days".format(delta.days)
		elif (days == 0):
			dayString = ""
		elif (days == 1):
			dayString = "**1** day"
		else:
			print("Error with delta days. Negative or fraction number")
			raise TypeError

		if (hours > 1):
			hourString = " **{}** hours".format(hours)
		elif (hours == 0):
			hourString = ""
		elif (hours == 1):
			hourString = " **1** hour"
		else:
			print("Error with delta hours. Negative or fraction number")
			raise TypeError

		if (minutes > 0):
			if (hours > 0 or delta.days > 0):
				minuteString = " and **{0}** minute{1}".format(minutes,"s"*(minutes != 1))
			else:
				minuteString = "**{0}** minute{1}".format(minutes,"s"*(minutes != 1))

		elif (minutes == 0):
			minuteString = ""
		else:
			print("Error with delta minutes. Negative or fraction number")
			raise TypeError

		countdown = dayString+hourString+minuteString
		"""###"""

		# print(countdown)
		newSidebar = "Next episode airs in:  \n"+countdown+"\n___"+sidebarSectionB
		# print(newSidebar)
		subreddit.mod.update(description=newSidebar)
		sleep(sleepTime)