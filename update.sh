# see http://qiita.com/yudoufu/items/48cb6fb71e5b498b2532
cd $(dirname ${BASH_SOURCE:-$0})
source /home/kameda/.bashrc
source ./py2env/bin/activate
COLOR_1="\e[32m"
COLOR_OFF="\e[m"
echo -e "${COLOR_1}pull from Transifex ... \n say 'no' to next question!${COLOR_OFF}"
#yes "no" | tx pull -f -l ja_JP
#python3 insert-translators.py
echo -e "${COLOR_1}render asciidoc ... ${COLOR_OFF}"
cd jekyll
# . render.sh
/usr/bin/asciidoc -b html5 -o "book.html" index.adoc
python3 jekyllify.py
/usr/local/bin/jekyll build
cd ../
cd asciidoctor
# . render.sh
/usr/local/bin/asciidoctor -b html5 -d book -a toc2 index.adoc
cd ../
cp -r jekyll/_site/* githubio/DataJournalismJP.github.io/handbook
cp asciidoctor/index.html githubio/DataJournalismJP.github.io/handbook/all.html
echo Done.
echo `date`
deactivate
