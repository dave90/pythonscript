import fileinput

i=0
for line in fileinput.input():
    if not i:
        i=1
        continue
    l = line.rstrip("\n")
    splitLine = l.split("\t")
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
    print(instance2+"\t"+splitLine[2]+"\t"+result)



