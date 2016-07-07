#!/bin/bash

IP=$1
DIR="ALL-PROBLEMS"
OUTFILE="test.tar.gz"

if [ $2 == --list ]
then
    if [ $# == 2 ]
    then    
        ssh $IP "cd $DIR;python3 paco.py --list"
    fi
    if [ $# == 3 ]
    then
	 ssh $IP "cd $DIR;python3 paco.py --list $3"
    fi

fi
if [ $2 == --pac ]
then
    if [ $# == 2 ]
    then
	echo "NOT SUPPORTED"
    fi
    if [ $# == 3 ]
    then
	echo "NOT SUPPORTED"
    fi
    if [ $# == 4 ]
    then
	ssh $IP "cd $DIR;python3 paco.py --pac $3 $4"
	scp $IP:$DIR/$OUTFILE .
	ssh $IP "rm $DIR/$OUTFILE"
	tar -xvf $OUTFILE
    fi
    
fi
