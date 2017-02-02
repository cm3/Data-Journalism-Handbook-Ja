# see http://qiita.com/yudoufu/items/48cb6fb71e5b498b2532
cd $(dirname ${BASH_SOURCE:-$0})
source /home/kameda/.bashrc
source activate py35con
COLOR_1="\e[32m"
COLOR_OFF="\e[m"
# fetch (when you develop and debug jekyll templete, comment out this 3 lines.)
echo -e "${COLOR_1}pull from Transifex ... \n say 'no' to next question!${COLOR_OFF}"
yes "no" | /usr/local/bin/tx pull -f -l ja_JP
python3 insert-translators.py
# render
echo -e "${COLOR_1}render asciidoc ... ${COLOR_OFF}"
cd jekyll
/usr/local/bin/asciidoctor -b html5 -o "book.html" index.adoc
python3 jekyllify.py
/usr/local/bin/jekyll build --destination "../DataJournalismJP.github.io/handbook"
/usr/local/bin/asciidoctor -b html5 -o "../DataJournalismJP.github.io/handbook/all.html" -d book -a toc2 index.adoc
cd ../
echo Done.
echo `date`
source deactivate
