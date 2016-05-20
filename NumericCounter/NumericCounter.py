import sys
import os

#arg
# 1: benchmark filename
# 2: name of the grounder
# 3: file to append the result

def takeNumber(line , num):
    l=line.split(" ")
    number=l[num]
    return int(number)

r = 0
state = 0
body = 0
fact = 0
fileBench = sys.argv[1]
outfile = sys.argv[3]
binary = sys.argv[2]

for line in sys.stdin:
    line=line.rstrip()
    if len(line) == 0:
        continue
    if line[0]=='0':
        state=1

    if state!=1:
        r+=1

        if line.startswith("1 1 "):
            body+=takeNumber(line,2)
        elif line.startswith("1 "):
             num=takeNumber(line,2)
             if num==0:
                 fact += 1
             body += num
        elif line.startswith("2 "):
            body+=takeNumber(line,2)
        elif line.startswith("3 ") or line.startswith("8 "):
            head=takeNumber(line,1);
            body+=takeNumber(line,head+2)
        elif line.startswith("5 "):
            body+=takeNumber(line,3)
        elif line.startswith("6 "):
            body+=takeNumber(line,2)

nameBench = fileBench.split("/")
bench=""
if len(nameBench)>8:
    bench=nameBench[7]+"\t";

header=""
if not os.path.isfile(outfile):
    header="Bench\tProblem\tExe\tN.Rule\tN. Atom In Boby\tN. Fact\n"
with open(outfile, "a") as myfile:
    myfile.write(header+bench+fileBench+"\t"+binary+"\t"+str(r)+"\t"+str(body)+"\t"+str(fact)+"\n")

#print(str(r)+"\t"+str(body)+"\t"+str(fact))
