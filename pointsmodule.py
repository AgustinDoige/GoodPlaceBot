import praw
import json
import datetime

class Message:
	def __init__(self,msgBody):
		self.rawMessage = msgBody
		self.sentences = self.getSentences()
		self.msgPoints = self.valueFunction1() + self.valueFunction2()

	def getSentences(self):
		"""A function that takes a string and does its best to return a list of separate sentences. 
			Used for some rules that need to look specifically inside a sentence"""
		splitTerms = ['.','!','?','\n',':']
		sentences = [self.rawMessage]
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

	def valueFunction1(self):
		"""
		ValueFunction1 gives the value of the json rules that don't need to be tested on a sentence-to-sentence basis
		"""
		return 0

	def valueFunction2(self):
		"""
		ValueFunction2 gives the value of the json rules that need to be tested on a sentence-to-sentence basis
		"""
		return 0

"""
WHOLE DIC:
{'meta': {'format': "'reward':<int>,'hardrule':<bool>,'reply':<str/None>,'modnotice':<bool>,'termlist':<list/matrix>", 'Description': "Description in 'json rules' section of the README.md"}, 'rules': {'hardRuleExample': {'reward': 0, 'hardrule': True, 'reply': None, 'modnotice': None, 'termlist': ['A', 'B']}, 'softRuleExample': {'reward': 0, 'hardrule': False, 'reply': None, 'modnotice': None, 'termlist': ['A', 'B']}, 'hardMixExample': {'reward': 0, 'hardrule': True, 'reply': None, 'modnotice': None, 'termlist': [['A', 'B'], ['C', 'D']]}, 'softMixExample': {'reward': 0, 'hardrule': False, 'reply': None, 'modnotice': None, 'termlist': [['A', 'B'], ['C', 'D']]}}}
RULES:
{'reward': 0, 'hardrule': True, 'reply': None, 'modnotice': None, 'termlist': ['A', 'B']}
{'reward': 0, 'hardrule': False, 'reply': None, 'modnotice': None, 'termlist': ['A', 'B']}
{'reward': 0, 'hardrule': True, 'reply': None, 'modnotice': None, 'termlist': [['A', 'B'], ['C', 'D']]}
{'reward': 0, 'hardrule': False, 'reply': None, 'modnotice': None, 'termlist': [['A', 'B'], ['C', 'D']]}
"""