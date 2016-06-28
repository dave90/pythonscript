import fileinput

i=0
for line in fileinput.input():
    if not i:
        i=1
        continue
    l = line.rstrip("\n")
    splitLine = l.split("\t")
    if len(splitLine) == 3:
    	splitInstance=splitLine[0].split("/")
    	inst=""
    	for s in splitInstance[6:]:
     		inst = inst + s +"/"
    	inst =  inst[:-1]
    	print(inst+"\t"+splitLine[1]+"\t"+splitLine[2])

    if len(splitLine) < 8:
        continue
    
    if splitLine[7]=="yes":
    	result="OK"
    elif splitLine[7]=="no":
    	result="NO"
    else:
    	continue
    instance=splitLine[1].strip("('")
    instance2=instance.strip("',)")
    splitInstance=instance2.split("/")
    inst=""
    for s in splitInstance[6:]:
     inst = inst + s +"/"
    inst =  inst[:-1]
    print(inst+"\t"+splitLine[2]+"\t"+result)



