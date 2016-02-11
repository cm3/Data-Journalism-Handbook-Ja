python3 prepare-asc.py > index.asc
asciidoctor -b html5 -d book *.asc

