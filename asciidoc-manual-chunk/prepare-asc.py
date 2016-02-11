#Transifex のファイルを整理する DJH プロジェクト専用のスクリプト

import re

re_head2 = re.compile("^== (.*?)(?: ==)?$")
re_head3 = re.compile("^=== (.*?)(?: ===)?$")

top_header = """:docinfo1:
:nofooter:
"""
eachpage_header = """:docinfo1:
:noheader:
:nofooter:

++++
<div id="header">
<a href="./">&laquo; Data Jounalism Handbook: 目次へ</a> 
</div>
<style>
#header {margin: 1em 0em;}
</style>
++++
"""

id_list_chap0 = ["preface"]
id_list_chap1 = ["011-what-is-data-journalism",
    "012-why-journalists-should-use-data",
    "013-why-is-data-journalism-important",
    "014-some-favourite-examples",
    "015-data-journalism-in-perspective"]
id_list_chap2 = ["021-the-abcs-data-journalism-play",
    "022-data-journalism-at-the-bbc",
    "how-the-news-apps-team-at-the-chicago-tribune-works",
    "024-behind-the-scenes-at-the-guardian-datablog",
    "025-data-journalism-at-the-zeit-online",
    "026-how-to-hire-a-hacker",
    "027-harnessing-external-expertise-through-hackathons",
    "028-following-the-money",
    "029-our-stories-come-as-code",
    "0210-kaas-mulvad-semi-finished-content-for-stakeholder-groups",
    "0211-business-models-for-data-journalism"]
id_list_chap3 = ["031-the-opportunity-gap",
    "032-a-nine-month-investigation-into-european-structural-funds",
    "033-the-eurozone-meltdown",
    "034-covering-the-public-purse-with-openspendingorg",
    "035-finnish-parliamentary-elections-and-campaign-funding",
    "036-electoral-hack-in-realtime-hackshackers-buenos-aires",
    "037-data-in-the-news-wikileaks",
    "038-mapa76-hackathon",
    "039-the-guardian-datablogs-coverage-of-the-uk-riots",
    "0310-illinois-school-report-cards",
    "0311-hospital-billing",
    "0312-care-home-crisis",
    "0313-the-tell-all-telephone",
    "0314-which-car-model-mot-failure-rates",
    "0315-bus-subsidies-in-argentina",
    "0316-citizen-data-reporters",
    "0317-the-big-board-for-election-results",
    "0318-crowdsourcing-the-price-of-water"]
id_list_chap4 = ["041-a-five-minute-field-guide",
    "042-your-right-to-data",
    "043-wobbing-works-use-it",
    "044-getting-data-from-the-web",
    "045-the-web-as-a-data-source",
    "046-crowdsourcing-data-at-the-guardian-datablog",
    "047-how-the-datablog-used-crowdsourcing-to-cover-olympic-ticketing",
    "048-using-and-sharing-data-the-black-letter-the-fine-print-and-reality"]
id_list_chap5 = ["051-become-data-literate-in-three-simple-steps",
    "052-tips-for-working-with-numbers-in-the-news",
    "053-basic-steps-in-working-with-data",
    "054-the-32-loaf-of-bread",
    "055-start-with-the-data-finish-with-a-story",
    "056-data-stories",
    "057-data-journalists-discuss-their-tools-of-choice",
    "058-using-data-visualization-to-find-insights-in-data"]
id_list_chap6 = ["061-presenting-data-to-the-public",
    "062-how-to-build-a-news-app",
    "063-news-apps-at-propublica",
    "064-visualization-as-the-workhorse-of-data-journalism",
    "065-using-visualizations-to-tell-stories",
    "066-different-charts-tell-different-tales",
    "067-data-visualization-diy-our-top-tools",
    "068-how-we-serve-data-at-verdens-gang",
    "069-public-data-goes-social",
    "0610-engaging-people-around-your-data"]

def id2path(_id):
    return "../translations/the-data-journalism-handbook."+_id+"/ja_JP.txt"

def get_chap(_path, _chapnum, _secnum):
    _toc_string = ""
    write_to = ""
    with open(_path, "r", encoding="utf8") as fr:
        line = fr.readline()
        while line:
            if(re_head2.match(line)):
                write_to = "toc"
                line = fr.readline()
            elif(re_head3.match(line)):
                write_to = "fw"
                try:
                    fw.close()
                except:
                    pass
                _secnum += 1
                fileid = str(_chapnum)+"-"+str(_secnum)
                sectitle = re_head3.match(line).group(1)
                _toc_string += "- "+str(_chapnum)+"."+str(_secnum)+". link:./"+fileid+".html["+sectitle+"]\n"
                fw = open(fileid+".asc", "w", encoding="utf8")
                fw.write(eachpage_header)
                fw.write("=== "+str(_chapnum)+"."+str(_secnum)+". "+sectitle)
                line = fr.readline()
            elif write_to is "fw":
                fw.write(line)
                line = fr.readline()
            elif write_to is "toc":
                _toc_string += line
                line = fr.readline()
            else:
                line = fr.readline()
    return [_toc_string, _secnum]

def get_chap_all(_id_list,_chapnum):
    _secnum = 0
    _toc_string = ""
    for _id in _id_list:
        _toc_temp, _secnum = get_chap(id2path(_id),_chapnum,_secnum)
        _toc_string += _toc_temp
    return _toc_string

if __name__ == '__main__':
    print(top_header)
    print("= データ・ジャーナリズム・ハンドブック =")
    print("")
    print("== 0. 前書き")
    print(get_chap_all(id_list_chap0,0))
    print("== 1. はじめに")
    print(get_chap_all(id_list_chap1,1))
    print("== 2. ニュースルームにて")
    print(get_chap_all(id_list_chap2,2))
    print("== 3. ケーススタディ")
    print(get_chap_all(id_list_chap3,3))
    print("== 4. データを取得する")
    print(get_chap_all(id_list_chap4,4))
    print("== 5. データを理解する")
    print(get_chap_all(id_list_chap5,5))
    print("== 6. データを提供する")
    print(get_chap_all(id_list_chap6,6))
