# see http://qiita.com/yudoufu/items/48cb6fb71e5b498b2532
cd $(dirname ${BASH_SOURCE:-$0})
source /home/kameda/.bashrc
source ./py2env/bin/activate
COLOR_1="\e[32m"
COLOR_OFF="\e[m"
echo -e "${COLOR_1}pull from Transifex ... \n say 'no' to next question!${COLOR_OFF}"
yes "no" | tx pull -f -l ja_JP
python3 insert-translators.py
echo -e "${COLOR_1}render asciidoc ... ${COLOR_OFF}"
#cd asciidoc
#source render.sh
#cd ../
cd jekyll
source render.sh
cd ../
#cd asciidoc-manual-chunk
#source render.sh
#cd ../
echo Done.
echo `date`
deactivate
