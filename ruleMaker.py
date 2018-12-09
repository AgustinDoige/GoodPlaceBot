import json
"""Rules should have the following information:

name = <string>              (very short string explaining what the rule is)
shadow = <boolean>           (whether or not it triggers a response)
repply = <string>            (if reaction is NonShadow this stores the repply)
hardrule= <boolean>          (whether the text should be exact in that order or not)
termlist = <list>            (A list of terms to be looking for)
reward = <int>               (how many points it gives/takes away)


"""

dummyrule = {'name': "dummyRule",'shadow':False,'repply':None,'hardrule':True,'termlist':["shirt","fork","forking","shirtballs","ashole"],'reward':10}




def addRule(dic):

	return [newRule,repeatLoop]



with open("rules.json","r") as f:
	rulesDic = json.load(f)

while True:
	addRule(rulesDic)
	
