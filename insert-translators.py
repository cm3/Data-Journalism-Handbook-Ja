import re

marker_str = "=== 本書はどういう本か（そして、どういう本ではないか） ==="
re_marker = re.compile(marker_str)
with open("contributors-jp.asc","r",encoding="utf8") as fr:
    translators = fr.read()+"\n"
with open("./translations/the-data-journalism-handbook.preface/ja_JP.txt","r",encoding="utf8") as fr:
    original = fr.read()
with open("./translations/the-data-journalism-handbook.preface/ja_JP.txt","w",encoding="utf8") as fw:
    inserted = re_marker.sub(translators+marker_str,original)
    fw.write(inserted)
