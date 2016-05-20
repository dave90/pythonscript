import fileinput

import random

def printRule(rules):
    for r in rules:
        print(r)

r = 1
constraints =[]
simpleRules =[]
choiceRules = []
disjunctionRules =[]
weightRule = []
weaks = []

order = [0, 1 , 2 , 3, 4 , 5]

state = 0
table =""
for line in fileinput.input():
    line=line.rstrip()
    if line[0]=='0':
        state=1

    if state==1:
        table+=line+"\n"
    else:
        if line.startswith("1 1 "):
            constraints.append(line)
        elif line.startswith("1 "):
            simpleRules.append(line)
        elif line.startswith("3 "):
            choiceRules.append(line)
        elif line.startswith("8 "):
            disjunctionRules.append(line)
        elif line.startswith("5 "):
            weightRule.append(line)
        elif line.startswith("6 "):
            weaks.append(line)

print("CONSTRAIN:")
printRule(constraints)
print("SIMPLE")
printRule(simpleRules)
print("CHOICE")
printRule(choiceRules)
print("DISJUNCTIVE")
printRule(disjunctionRules)
print("WEIGHT")
printRule(weightRule)
print("WEAKS")
printRule(weaks)
print(table)


if r:
    merge = constraints +simpleRules +choiceRules +disjunctionRules + weightRule +weaks
    while len(merge)>0:
        i = random.randrange(len(merge))
        rule = merge[i]
        merge.pop(i)
        print(rule)
    print(table)
elif 1:
    for i in order:
        if i == 0:
            printRule(simpleRules)
        elif i == 1:
            printRule(constraints)
        elif i == 2:
            printRule(choiceRules)
        elif i == 3:
            printRule(disjunctionRules)
        elif i == 4:
            printRule(weightRule)
        elif i == 5:
            printRule(weaks)
    print(table)