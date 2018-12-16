import praw
import json
import datetime

def getSentences():
	pass

def giveValue(string,ruleDic):
	#dummyrule = {'name': "dummyRule",'shadow':False,'repply':None,'hardrule':True,'termlist':["shirt","fork","forking","shirtballs","ashole"],'reward':10}

	pass
	






def readSubreddit(subreddit,readtype):

	#/r/subredditname/new and /r/subredditname/comments
	pass



with open("rules.json","r") as f:
	rulesDic = json.load(f)

rulesDic['rules'] = [{'name': 'dummyRule', 'reply': None, 'hardrule': True, 'termlist': ['shirt', 'fork', 'forking', 'shirtballs'], 'reward': 10}]


with open("rules.json","w") as f:
	json.dump(rulesDic,f,indent=2)

print(rulesDic['rules'])