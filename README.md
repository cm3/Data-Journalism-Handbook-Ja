# これは何？

[The Data Journalism Handbook の日本語訳プロジェクト](https://www.transifex.com/liliana.bounegru/the-data-journalism-handbook/language/ja_JP/)の現状を HTML 化するためのスクリプト。`update.sh` で、Transifex から翻訳ファイルを pull してきて、asciidoc でレンダリングできる。figs は [okfn/ddjbook in GitHub](https://github.com/okfn/ddjbook/tree/web/web/figs/)よりコピー。

# 必要な準備

```
virtualenv py2env
source ./py2env/bin/activate
pip install transifex-client
tx init
tx set --auto-remote http://www.transifex.net/projects/p/the-data-journalism-handbook/
sudo apt-get install asciidoc
```

# 毎回の更新

途中止まったように見えるが、辛抱強く待つと Done となる。1～2分程度。

```
source ./update.sh
```

# ライセンスについて

- コンテンツは本家を継承して [Creative Commons — Attribution-ShareAlike 3.0 Unported — CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/)
- プログラム部分は Public Domain。