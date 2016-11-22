# see http://qiita.com/yudoufu/items/48cb6fb71e5b498b2532
cd $(dirname ${BASH_SOURCE:-$0})
source /home/kameda/.bashrc
source activate py35con
COLOR_1="\e[32m"
COLOR_OFF="\e[m"
echo -e "${COLOR_1}pull from Transifex ... \n say 'no' to next question!${COLOR_OFF}"
yes "no" | tx pull -f -l ja_JP
python3 insert-translators.py
echo -e "${COLOR_1}render asciidoc ... ${COLOR_OFF}"
cd jekyll
/usr/local/bin/asciidoctor -b html5 -o "book.html" index.adoc
/usr/local/bin/asciidoctor -b html5 -o "all.html" -d book -a toc2 index.adoc
python3 jekyllify.py
/usr/local/bin/jekyll build
cd ../
cp -r jekyll/_site/* githubio/DataJournalismJP.github.io/handbook
echo Done.
echo `date`
source deactivate
