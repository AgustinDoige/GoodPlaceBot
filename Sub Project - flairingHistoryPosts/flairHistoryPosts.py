
import praw
# import datetime
# import pytz
# import json
from time import sleep
# from sidebarCountdown import updateSidebar

print("Logging In...")
reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('TheGoodPlace') # Test sub: TheGoodSandbox
print("Logged into r/{}".format(subreddit.title))

counter = 0

print("Parsing Flairs...")
query1 = "NOT flair:'no_spoilers' NOT flair:'season_one' NOT flair:'season_two' "
query2 = "NOT flair:'season_three' NOT flair:'season_four' NOT flair:'shirtpost' NOT flair:'meta'"
query = query1+query2
for submission in subreddit.search(query,limit=1):
	flairList = submission.flair.choices() #List of dictionaries of flairs
	
	""" EXAMPLE OF FLAIR TEMPLATE:
	{'flair_css_class': 'meta', 
	'flair_template_id': 'e2eda490-4cef-11e9-a49a-0e1d6d9f8604', 
	'flair_text_editable': True, 
	'flair_position': 'left', 
	'flair_text': 'Meta'}
	"""
	templates = {}
	for template in flairList:
		if "no spoiler" in template['flair_text'].lower():
			templates['no_spoilers'] = template

		if "meta" in template['flair_text'].lower():
			templates['meta'] = template

		if "shirtpost" in template['flair_text'].lower():
			templates['shirtpost'] = template

		if "season one" in template['flair_text'].lower():
			templates['s1'] = template

		if "season two" in template['flair_text'].lower():
			templates['s2'] = template

		if "season three" in template['flair_text'].lower():
			templates['s3'] = template

		if "season four" in template['flair_text'].lower():
			templates['s4'] = template

print("Parsing Flairs done")

nonSpoilers = ["no spoiler", "s1e1 ", "s1 e1 "]
s1List = ["s1", "s01", "season 1", "first season"]
s2List = ["s2", "s02", "season 2", "second season"]
s3List = ["s3", "s03", "season 3", "third season"]
s4List = ["s4", "s04", "season 4", "fourth season"]

print("Reading id cache...")
posts_processed = set()
try:
	with open("flairHistoryPostsLog3.txt",'r') as h:
		line = h.readline()
		while line != '':
			posts_processed.add(line.strip())
			line = h.readline()
except FileNotFoundError:
	pass

# print(posts_processed)

print("Reading id cache done")
print("Flairing Posts...")
while True:
	temp_counter =  (counter+1)-1
	with open("flairHistoryPostsLog1.txt",'a') as f:
		with open("flairHistoryPostsLog2.txt",'a') as g:
			for submission in subreddit.search(query,sort='new',limit=1000):

				if submission.id in posts_processed:
					continue
				else:
					posts_processed.add(submission.id)

				titl = submission.title.lower()
				counter += 1

				try:
					if any((x in titl) for x in nonSpoilers):
						templ_id = templates['no_spoilers']["flair_template_id"]
						print("Selecting Flair No-Spoilers to submission: {} Link: {}\n".format(submission.title,submission.permalink))
						f.write("Selecting Flair No-Spoilers to submission: {} Link: {}\n".format(submission.title,submission.permalink))
						submission.flair.select(templ_id, 'No Spoilers')

					elif any((x in titl) for x in s1List):
						templ_id = templates['s1']["flair_template_id"]
						print("Selecting Flair [Season One] to submission: {} Link: {}\n".format(submission.title,submission.permalink))
						f.write("Selecting Flair [Season One] to submission: {} Link: {}\n".format(submission.title,submission.permalink))
						submission.flair.select(templ_id, 'Season One')

					elif any((x in titl) for x in s2List):
						templ_id = templates['s2']["flair_template_id"]
						print("Selecting Flair [Season Two] to submission: {} Link: {}\n".format(submission.title,submission.permalink))
						f.write("Selecting Flair [Season Two] to submission: {} Link: {}\n".format(submission.title,submission.permalink))
						submission.flair.select(templ_id, 'Season Two')

					elif any((x in titl) for x in s3List):
						templ_id = templates['s3']["flair_template_id"]
						print("Selecting Flair [Season Three] to submission: {} Link: {}\n".format(submission.title,submission.permalink))
						f.write("Selecting Flair [Season Three] to submission: {} Link: {}\n".format(submission.title,submission.permalink))
						submission.flair.select(templ_id, 'Season Three')

					elif any((x in titl) for x in s4List):
						templ_id = templates['s4']["flair_template_id"]
						print("Selecting Flair [Season Four] to submission: {} Link: {}\n".format(submission.title,submission.permalink))
						f.write("Selecting Flair [Season Four] to submission: {} Link: {}\n".format(submission.title,submission.permalink))
						submission.flair.select(templ_id, 'Season Four')

					elif "shirtpost" in titl:
						templ_id = templates['shirtpost']["flair_template_id"]
						print("Selecting Flair [Shirtpost] to submission: {} Link: {}\n".format(submission.title,submission.permalink))
						f.write("Selecting Flair [Shirtpost] to submission: {} Link: {}\n".format(submission.title,submission.permalink))
						submission.flair.select(templ_id, 'Shirtpost')

					elif "meta" in titl:
						templ_id = templates['meta']["flair_template_id"]
						print("Selecting Flair [Meta] to submission: {} Link: {}\n".format(submission.title,submission.permalink))
						f.write("Selecting Flair [Meta] to submission: {} Link: {}\n".format(submission.title,submission.permalink))
						submission.flair.select(templ_id, 'Meta')

					else:
						counter -= 1
						g.write("https://www.reddit.com{}    - Title: {}\n".format(submission.permalink,submission.title))

				except Exception:
					g.write("An Exception ocurred with submission {}. Could not flair.\n".format(submission.permalink))
	print("Cycle finished. {} posts flaired".format(counter))
	if temp_counter <= counter:
		break
	else:
		print("Starting new cycle...")

print("Flairing Posts done")
print("Updating cache...")
with open("flairHistoryPostsLog3.txt",'w') as h:
	pass
with open("flairHistoryPostsLog3.txt",'w') as h:
	for i in posts_processed:
		h.write(i+"\n")
print("Updating cache done")
print("Program Completed. {} posts flaired".format(counter))