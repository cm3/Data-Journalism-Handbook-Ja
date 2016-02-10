#!/bin/bash

asciidoc -b html5 -o "book.html" ./rendered/index.adoc
python jekyllify.py
cd web
jekyll build
cd ..
