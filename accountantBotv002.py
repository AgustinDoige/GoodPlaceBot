#!/usr/bin/python
import praw
import datetime
import json

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('TheGoodSandbox')

rDictionary = {}
# .rstrip()
with open("hardrules.txt","r") as f:
	f.readline() #This so it ignores the first 2 lines of the .txt file
	f.readline()
	rules = f.readlines()

	for rule in rules:
		split1 = rule.split(": ",1)
		rDictionary[split1[1].rstrip()] = int(split1[0])

try:
	with open("userStates.json","r") as g:
		uDictionary = json.load(f)
except FileNotFoundError:
	uDictionary = {'users':[]}

for submission in subreddit.new(limit=3):
	# print(submission.title)
	# print(submission.selftext)

	submission.comments.replace_more(limit=None)
	comment_queue = submission.comments[:]  # Seed with top-level

	while comment_queue:
		comment = comment_queue.pop(0)

		print("$Comment: "+comment.body+"\n")

		for phrase in rDictionary.keys():
			# print(phrase)
			if phrase in comment.body:
				author = comment.author

				try:
					pass
				except KeyError:
					ud = {
					'name'   : author.name,
					'id'     : author.id,
					'points' : rDictionary[phrase],
					'logs'   : []	}

					uDictionary['users'] = uDictionary['users']





				# try:
				# 	uDictionary[author.id] = uDictionary[author.id] + rDictionary[phrase]
				# except KeyError:
				# 	uDictionary[author.id] = rDictionary[phrase]

				with open("accountantLog.txt","a") as h:
					log = "{} awarded to {} (id:{}) for commenting '{}'. Comment url: {}\n".format(rDictionary[phrase],author.name,author.id,comment.body,comment.permalink)
					print(log)
					h.write(log)

				# comment.reply("You have been given {} points for that comment. Your total points are {}  \n\n ^^(I am a bot and this action was performed automatically)".format(rDictionary[phrase],uDictionary[author.id]))

		comment_queue.extend(comment.replies)

with open("userStates.json","w") as j:
	json.dump(uDictionary,j,indent=2)

# with open("userPoints.txt","w") as j:
# 	for userId in uDictionary.keys():
# 		j.write(str(uDictionary[userId])+": "+userId+"\n")


"""POSSIBLE PROBLEMS: 
If 1 comment has multiple hard rule phrases, the bot will account and reply to them separately."""