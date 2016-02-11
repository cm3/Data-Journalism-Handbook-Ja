# AsciiDoc で DocBook で出力し、Pandoc で html に変換

Pandoc は AsciiDoc を直接入力としてサポートしていないが、DocBook が完全に仲介してくれるので問題ない。

問題点として、Pandoc で直接変換し、toc を付けた場合は目次がリンクにならない。これは元の文書の各章に id が付されていないためで、Markdown 形式を介すことで、その `auto_identifiers` 拡張により、リンクがつく。Pandoc はヘッダーの付加などにも柔軟に対応するため、AsciiDoc のみで操作するよりは、DocBook から Pandoc で柔軟に変化させた方が良いかもしれない。また、Pandoc は開発が非常に活発である。