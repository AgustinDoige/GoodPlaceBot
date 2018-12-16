import praw
import json
import datetime

def getSentences(commentBody):
	"""A function that takes a string and does its best to return a list of separate sentences. 
		Used for some rules that need to look specifically inside a sentence"""
	splitTerms = ['.','!','?','\n',':']
	sentences = [commentBody]
	rejectedList = ['www','com/','//']
	for term in splitTerms:
		for ind in range(0,len(sentences)):
			tempStr = sentences.pop(0)
			# sentences.extend(tempStr.split(term))
			sencand = tempStr.split(term)
			for it in sencand:
				if (it != '' and it != ' '):
					sentences.append(it)

	curated = []
	for sent in sentences:
		add = True
		for trm in rejectedList:
			if trm in sent:
				add = False
		if add:
			curated.append(sent)
	return curated


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