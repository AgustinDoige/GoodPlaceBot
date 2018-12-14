import json
"""Rules should have the following information:

name = <string>              (very short string explaining what the rule is)
reply = <string>             (Automatic reply. "None" for no reply)
modnotice = <boolean>        (whether or not the bot should notify a mod something)
hardrule= <boolean>          (whether the text should be exact in that order or not)
termlist = <list>            (A list of terms to be looking for)
reward = <int>               (how many points it gives/takes away)


"""

def rewriteRules(newDict):
	with open("rules.json","w") as h:
		json.dump(newDict,h,indent=2)

def writeBasicFile():
	hardRuleExample = {'reward':0,'hardrule':True,'reply':None,'modnotice':False,'termlist':['shirt','fork','forking','shirtballs','forked']}
	softRuleExample = {'reward':0,'hardrule':False,'reply':None,'modnotice':False,'termlist':['>!','!<']}
	hardMixExample  = {'reward':0,'hardrule':True,'reply':None,'modnotice':False,'termlist':[['bad','terrible','awful','dumb','stupid'],[' accent',' accents']]}
	softMixExample  = {'reward':0,'hardrule':False,'reply':None,'modnotice':False,'termlist':[['this','that'],['example','examples']]}

	rulesDic = {}
	rulesDic['meta'] = {}
	rulesDic['meta']['format'] = "'reward':<int>,'hardrule':<bool>,'reply':<str/None>,'modnotice':<bool>,'termlist':<list/matrix>"
	rulesDic['meta']['Description'] = "Description in 'json rules' section of the README.md"
	rulesDic['rules'] = {"hardRuleExample":hardRuleExample,"softRuleExample":softRuleExample,"hardMixExample":hardMixExample,"softMixExample":softMixExample}
	rewriteRules(rulesDic)	


def addRule(dic):
	pass
	# return [newRule,repeatLoop]


writeBasicFile()

# with open("rules.json","r") as f:
# 	rulesDic = json.load(f)

# for rul in rulesDic['rules'].keys():
# 	print ("Key:",rul,"    ",rulesDic['rules'][rul])

# rulesDic['meta']['explanation'] = "name: a string that is used to call the key more easily"

# print(rulesDic)
