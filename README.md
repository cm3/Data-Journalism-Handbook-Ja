# The Data Journalism Handbook tx2html

## これは何？

[The Data Journalism Handbook の日本語訳プロジェクト](https://www.transifex.com/liliana.bounegru/the-data-journalism-handbook/language/ja_JP/)の現状を HTML 化するためのスクリプト。`update.sh` で、Transifex から翻訳ファイルを pull してきて、asciidoc でレンダリングできる。figs は [okfn/ddjbook in GitHub](https://github.com/okfn/ddjbook/tree/web/web/figs/) よりコピー。

## 必要な準備

Python 2 を使う。

```
virtualenv py2env
source ./py2env/bin/activate
pip install transifex-client
tx init
tx set --auto-remote http://www.transifex.net/projects/p/the-data-journalism-handbook/
sudo apt-get install asciidoc
```

## 毎回の更新

所要時間 1～2分程度。

```
source ./update.sh
```

## Jekyll ブランチについて

[okfn/ddjbook](https://github.com/okfn/ddjbook) では、AsciiDoc で html を生成した後 [Jekyll](https://jekyllrb.com/)を用いて html を整えている。その部分をコピーしたブランチになっており、`update.sh` の後、`jekyllify.sh` を使うことで jekyll フォルダに html が生成されるようになっている。だが、元の AsciiDoc ファイルのシンタックスに不備がある場合に正常に吐き出せないなど、翻訳途中の確認には不向き。また、シンプルにするためにも、master ブランチでは AsciiDoc のファイルを整備することで、綺麗なレンダリングを実現しようと考えている。

### 必要な準備 for Jekyllify

```
pip install lxml
pip install jinja2
sudo apt-add-repository ppa:brightbox/ruby-ng
sudo apt-get update
sudo apt-get install ruby2.3 ruby2.3-dev make gcc nodejs
sudo gem install jekyll --no-rdoc --no-ri
```

## ライセンスについて

- コンテンツは本家を継承して [Creative Commons — Attribution-ShareAlike 3.0 Unported — CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/)
- プログラム部分は Public Domain。