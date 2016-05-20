import fileinput

problemsResult = {}

for line in fileinput.input():
    l = line.rstrip("\n")
    splitLine = l.split("\t")
    if len(splitLine) < 3:
        continue
    if splitLine[0] not in problemsResult:
        problemsResult[splitLine[0]] = []
    sout = splitLine[1] + ";" + splitLine[2]
    problemsResult[splitLine[0]].append(sout)


def lessWeight(w1, w2):
    weightsLevels1 = w1.split(" ")
    weightsLevels2 = w2.split(" ")
    while len(weightsLevels1) > 0 and len(weightsLevels2) > 0:
        weightLevel1 = weightsLevels1.pop()
        weight1 = weightLevel1.split("@")[0]
        level1 = weightLevel1.split("@")[1]
        weightLevel2 = weightsLevels2.pop()
        weight2 = weightLevel2.split("@")[0]
        level2 = weightLevel2.split("@")[1]
        if level1 > level2:
            return 1
        if level1 < level2:
            return 0
        if weight1 < weight2:
            return 1
        if weight1 > weight2:
            return 0

    return len(weightsLevels1) > len(weightsLevels2)


def findLowWeight(okWeight):
    less = list(okWeight.keys())[0]
    for com in okWeight:
        if lessWeight(okWeight[com], okWeight[less]):
            less = com
    return less


def checkWeight(okWeight, instance):
    if len(okWeight) == 1:
        return
    first = list(okWeight.keys())[0]
    unequalWeight = 0
    for com in okWeight:
        if okWeight[com] != okWeight[first]:
            unequalWeight = 1
            break
    if unequalWeight:
        bestCom = findLowWeight(okWeight)
        print("WARNING command " + bestCom + " have lower weight with instance "+instance+":")
        for com in okWeight:
            print("\t" + com + " => " + okWeight[com])


for i in problemsResult:
    # create map for each command if yes or no ==> output
    # create map for each command the weights ==> weight
    output = {}
    weight = {}
    for commandRes in problemsResult[i]:
        command = commandRes.split(";")[0]
        res = commandRes.split(";")[1]
        if "@" in res:
            output[command] = res.split(" ", 1)[0]
            weight[command] = res.split(" ", 1)[1]
        else:
            output[command] = res
    # check if exist a command with no and another command with yes
    for com in output:
        if "OK" not in output[com]:
            for com1 in output:
                if "OK" in output[com1]:
                    print("WARNING command " + com + " have FAIL and " + com1 + " have OK in instance " + i)
                    break
    # compare weight of OK command
    if weight:
        okWeight = {}
        for com in output:
            if "OK" in output[com]:
                okWeight[com] = weight[com]
        if okWeight:
            checkWeight(okWeight, i)
