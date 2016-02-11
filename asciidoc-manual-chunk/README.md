# Python スクリプトで目次と各ページに分割する

本は構造によってどのように html 化したらよいかが異なる。一章の長さ、図の多さや配置、節や小節の深さ、参考文献の多さなどがその条件になる。そこで、コンテンツおよびメディアごとの対応を行うのは免れ得ない。

[okfn/ddjbook: Data Driven Journalism Handbook](https://github.com/okfn/ddjbook)で Jekyll 対応している `jekyllify.py` はまさにそうだし、本コンテンツも AsciiDoc のみでなるべくレンダリングを目指すものの、目次の生成や各ページへの分割のスクリプトを用意した。`prepare-asc.py` がそれである。

ヘッダーとフッターに関しては、各ファイルの初めに設定値を挿入し、共通のフッターは `docinfo-footer.html` に書いて読み込んでいる。詳しくは [Asciidoctor User Manual](http://asciidoctor.org/docs/user-manual/#docinfo-file)や[Chapter 31. Intrinsic Attributes](http://www.methods.co.nz/asciidoc/chunked/ch31.html)を参照のこと。
