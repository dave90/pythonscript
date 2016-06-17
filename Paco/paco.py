import sys
import os
import tarfile

DIR = "problems"

def diplayFile():
    if len(sys.argv)==2:
      for file in os.listdir(DIR):
          print(file)
    else:
        for file in os.listdir(os.path.join(DIR,sys.argv[2])):
            print(file)

def compact():
    tar = tarfile.open("test.tar.gz","w:gz")
    if len(sys.argv)==2:
      for file in os.listdir(DIR):
          tar.add(os.path.join(DIR, file))
    elif len(sys.argv)==3:
        for file in os.listdir(os.path.join(DIR,sys.argv[2])):
            print("ADD "+os.path.join(DIR, sys.argv[2],file))
            tar.add(os.path.join(DIR, sys.argv[2],file))
    else:
         for file in os.listdir(os.path.join(DIR,sys.argv[2],sys.argv[3])):
            print("ADD "+os.path.join(DIR, sys.argv[2],sys.argv[3],file))
            tar.add(os.path.join(DIR, sys.argv[2],sys.argv[3],file))
    tar.close()





status=0
if len(sys.argv)<1:
    exit(0)

if sys.argv[1]=="--list":
    status=1
elif sys.argv[1]=="--pac":
    status=2

if status==1:
    diplayFile()
elif status==2:
    compact()
