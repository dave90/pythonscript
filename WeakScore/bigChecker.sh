if [ "$(ls -A weak)" ]; then
    python3 RewForWeak.py *.txt > restemp
    python3 RewForWeak.py weak/* | grep @ >> restemp
else
    python3 RewForWeak.py *.txt > restemp 
fi

python3 WeakScore.py weakGringo/* restemp > weak_message
cat message >> weak_message
DATE=`date +%d-%m-%Y:%H:%M`
mv restemp old_result/restemp.$DATE
rm weak/*
mutt -s "Test Finiti - Checker" fusca@mat.unical.it zangari@mat.unical.it < weak_message
rm weak_message
