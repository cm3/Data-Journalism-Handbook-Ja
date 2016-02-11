# AsciiDoc で DocBook で出力し、その後 xsl を適用する方法

[Chapter 5. DocBook](http://www.methods.co.nz/asciidoc/chunked/ch05.html#_asciidoc_docbook_xsl_stylesheets_drivers "Chapter 5. DocBook") の `chunked.xsl` に書いてある方法。

```
asciidoc -b docbook index.adoc
```

で docbook 形式の `index.xml` が生成される。ここに

```
xsltproc --nonet /usr/share/xml/docbook/stylesheet/nwalsh/html/chunk.xsl index.xml
```

で xsl を適用すると、章ごとにページ分けされた html が出力される。ただし、chunk.xsl のパスは環境によって異なる。

参照:

- [DocBook XML文書からXHTML文書への変換 - 試験運用中なLinux備忘録](http://d.hatena.ne.jp/kakurasan/20070927/p1 "DocBook XML文書からXHTML文書への変換 - 試験運用中なLinux備忘録")