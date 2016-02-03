COLOR_1="\e[32m"
COLOR_OFF="\e[m"
echo -e "${COLOR_1}pull from Transifex ... ${COLOR_OFF}"
tx pull -f -l ja_JP
echo -e "${COLOR_1}render asciidoc ... ${COLOR_OFF}"
asciidoc -b html5 -d book -a toc2 ./rendered/index.adoc

