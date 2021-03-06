# これは何？

[The Data Journalism Handbook の日本語訳プロジェクト](https://www.transifex.com/liliana.bounegru/the-data-journalism-handbook/language/ja_JP/)の現状を HTML 化するためのスクリプト。`update.sh` で、Transifex から翻訳ファイルを pull してきて、asciidoctor でレンダリングできる。

[okfn/ddjbook in GitHub](https://github.com/okfn/ddjbook/)を元にしている。
figs は [/web/web/figs/](https://github.com/okfn/ddjbook/tree/web/web/figs/) よりコピー。

# 必要な準備

Python 3 を使う。例:

```
conda create -n py35con python=3.5.2
source activate py35con
pip install transifex-client
tx init
tx set --auto-remote http://www.transifex.net/projects/p/the-data-journalism-handbook/
sudo apt-get install asciidoctor
```

Jekyll のインストール:

```
conda install lxml
conda install jinja2
sudo apt-add-repository ppa:brightbox/ruby-ng
sudo apt-get update
sudo apt-get install ruby2.3 ruby2.3-dev make gcc nodejs
sudo gem install jekyll --no-rdoc --no-ri
```

（環境によっては他にも必要）

# 毎回の更新

所要時間 1～2分程度。

```
source ./update.sh
```

update.sh の冒頭には cron で環境変数を読み込むために作者の bashrc を読み込む設定が書かれている。適宜変更して使うこと。

# 仕組みなど

asciidoctor コマンドでまず book.html を生成し（`asciidoctor -b html5 -o "book.html" index.adoc`）、それを適宜分割しつつ yaml ヘッダーを付けて（`python jekyllify.py`）、`jekyll build`。そのため、book.htmlを見ることで全体を見渡すこともできる。目次付きの１ページレンダリングも all.html に用意している。

それらのアウトプット先を [DataJournalismJP/DataJournalismJP.github.io](https://github.com/DataJournalismJP/DataJournalismJP.github.io) を pull したディレクトリ内にしている。本スクリプトを動かしているサーバで内容を確認後、commit & push することで、[Data Journalism Handbook 日本語版プロジェクト](http://datajournalismjp.github.io/)のウェブサイトを更新できる。

# ライセンスについて

- コンテンツは本家を継承して [Creative Commons — Attribution-ShareAlike 3.0 Unported — CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/)
- プログラム部分は Public Domain。
