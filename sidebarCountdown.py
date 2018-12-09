#!/usr/bin/python
import praw
import datetime
import pytz
from time import sleep

reddit = praw.Reddit('bot1')
# subreddit = reddit.subreddit('TheGoodSandbox')
subreddit = reddit.subreddit('TheGoodPlace')

print("Logged into r/{}".format(subreddit.title))

timeZone = 'US/Eastern' # Google "pytz timezones" for other options
dummydate = datetime.datetime.now(tz=pytz.timezone(timeZone)) # This is needed for the .replace(tzinfo=dummydate.tzinfo) method

try:
	with open("episodeSchedule.txt","r") as f:
		# YYYY - MM - DD - TT:TT AM
		f.readline() # This is so it ignores the first line of the file which talks about the format
		temp = f.readlines()
		scheduleDates = []
		for st in temp:
			parsed_date = datetime.datetime.strptime(st.rstrip(),'%Y - %m - %d - %I:%M %p') # This creates a naive date with the parsed info
			scheduleDates.append(parsed_date.replace(tzinfo=dummydate.tzinfo)) # This turns that naive date into an aware one 
		del temp #This deletes the temporal list to free a small amount of memory	
except FileNotFoundError:
	print("Error. File 'episodeSchedule.txt' not found.")
	raise FileNotFoundError

while True:
	oldSidebar = subreddit.mod.settings()["description"] # Requests the current sidebar
	sidebarSectionB = oldSidebar.split("___",1)[1] # Splits the sidebar into the part that will be changed and the other, and saves the other
	# print(sidebarSectionB)

	currentDate = datetime.datetime.now(tz=pytz.timezone(timeZone)) #Gets current time
	# print("Current time in timezone", timeZone,":",currentDate)
	print("Updating Sidebar - Current time:",currentDate.strftime('%H:%M:%S'), " Local time:",datetime.datetime.now().strftime('%H:%M:%S'))

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
			pastEpisodes.append(abs(totalSec))

	if (remainingTime == []):
		newSidebar = "Next episode air date: To be announced  \n___"+sidebarSectionB
		subreddit.mod.update(description=newSidebar)
		break

	elif(min(pastEpisodes) < 86400): # If an episode has aired in the las 42h it will show this message
		newSidebar = "The new episode is out now!  \n___"+sidebarSectionB
		subreddit.mod.update(description=newSidebar)
		print("Last episode aired in the last {} seconds ({} hours).".format(min(pastEpisodes),int((min(pastEpisodes) - min(pastEpisodes)%3600)/3600)))
		print("Sleeping for 500 seconds")
		sleep(500)

	else:
		delta = min(remainingTime)
		days = delta.days
		hours = int((delta.seconds - delta.seconds%3600)/3600)
		minutes = int((delta.seconds%3600)/60)
		# countdown = "**{0}** day{1}, **{2}** hour{3} and **{4}** minute{5}".format(delta.days, "s"*(delta.days != 1), hours, "s"*(hours != 1),  minutes, "s"*(minutes != 1))

		######## This replaces the last line ############
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
		######################

		# print(countdown)
		newSidebar = "Next episode airs in:  \n"+countdown+"\n___"+sidebarSectionB
		# print(newSidebar)
		subreddit.mod.update(description=newSidebar)
		sleep(120)