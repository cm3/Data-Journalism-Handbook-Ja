#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from lxml import html
from pprint import pprint
from jinja2 import Template, Markup

SEGMENT = """---
layout: default
title: {{title.replace(':', '&59;')}}
short_title: {{short_title.replace(':', ' -')}}
---

<div class='row'>
    <div class="btn-group book-nav-top span6">
        <a class='btn' href="index.html">Home</a>
        {% if parent_name %}
            <a href="{{parent_name}}.html" class="btn">章: {{parent_title}}</a>
        {% endif %}
        {% if next_name %}
            <a href="{{next_name}}.html" class="btn">次: {{next_title.rsplit('(',1)[0]}}</a>
        {% endif %}
    </div>
    <div class="span6 right-align">
        <span class='st_facebook_hcount' displayText='Facebook'></span>
        <span class='st_twitter_hcount' st_title="{{ short_title }} #ddjbook" displayText='Tweet'></span>
        <span class='hatebu_hcount'><a href="http://b.hatena.ne.jp/entry/datajournalismjp.github.io/handbook/{{name}}.html" class="hatena-bookmark-button" data-hatena-bookmark-title="{{title}}" data-hatena-bookmark-layout="simple-balloon" title="このエントリーをはてなブックマークに追加"><img src="https://b.st-hatena.com/images/entry-button/button-only@2x.png" alt="このエントリーをはてなブックマークに追加" width="20" height="20" style="border: none;" /></a></span>
        <span class='line_sp'><div class="line-it-button" style="display: none;" data-type="share-b" data-lang="ja" ></div></span>
    </div>
</div>


<div id='content'>
    {{body}}
</div>

{% if children %}
    <h3>本章の内容</h3>
    <ul class='toc'>
        {% for c in children %}
            <li><a href="{{c.name}}.html">{{c.short_title}}</a></li>
        {% endfor %}
    </ul>
{% endif %}

<div class="btn-group book-nav-bottom">
    <a class='btn' href="index.html">Home</a>
    {% if parent_name %}
        <a href="{{parent_name}}.html" class="btn">章: {{parent_title}}</a>
    {% endif %}
    {% if next_name %}
        <a href="{{next_name}}.html" class="btn">次: {{next_title.rsplit('(',1)[0]}}</a>
    {% endif %}
</div>
"""

INDEX = """---
layout: default
title: ようこそ
short_title: ようこそ
---

<div class='row'>
    <div class="span12 right-align">
        <span class='st_facebook_hcount' displayText='Facebook'></span>
        <span class='st_twitter_hcount' st_title="データ・ジャーナリズム・ハンドブック日本語版 #ddjbook" displayText='Tweet'></span>
        <span class='hatebu_hcount'><a href="http://b.hatena.ne.jp/entry/datajournalismjp.github.io/handbook/" class="hatena-bookmark-button" data-hatena-bookmark-title="{{title}}" data-hatena-bookmark-layout="simple-balloon" title="このエントリーをはてなブックマークに追加"><img src="https://b.st-hatena.com/images/entry-button/button-only@2x.png" alt="このエントリーをはてなブックマークに追加" width="20" height="20" style="border: none;" /></a></span>
        <span class='line_sp'><div class="line-it-button" style="display: none;" data-type="share-b" data-lang="ja" ></div></span>
    </div>
</div>

<div class="row">
    <div class='span6'>
        {% for chapter in segments %}
        {% if not chapter.parent_name %}
            <h2><a href='{{chapter.name}}.html'>{{chapter.title}}</a></h2>
            <ul class='toc'>
                {% for segment in chapter.children %}
                    <li><a href="{{segment.name}}.html">{{segment.short_title}}</a></li>
                {% endfor %}
            </ul>
        {% endif %}
        {% endfor %}
    </div>
    <div class='span6'>
        <img src='img/cover_print.png' align='right'>
    </div>
</div>

"""


def clean_html(elem):
    for img in elem.findall('.//img'):
        if img.get('src').startswith('data:'):
            img.attrib['src'] = img.get('alt')
            del img.attrib['alt']
            print(img.get('alt'))
        if 'width' in img.attrib:
            del img.attrib['width']
    for a in elem.findall('.//a'):
        if a.get('href', '').startswith('#'):
            id_ = a.get('href').strip('#')
            #print id_
            caption = elem.find('.//div[@id="' + id_ + '"]/div[@class="title"]')
            #print caption
            if caption is not None:
                a.text = caption.text.split('.')[0]
            else:
                print(a.attrib)
    return html.tostring(elem, encoding='utf8')


def write_segment(data, out_dir):
    content = Template(SEGMENT).render(data)
    write_file(content, out_dir, data.get('name'))

def write_index(segments, out_dir):
    content = Template(INDEX).render(segments=segments)
    write_file(content, out_dir, 'index')


def write_file(content, out_dir, name):
    print(name)
    file_name = os.path.join(out_dir, name + '.html')
    fh = open(file_name, 'w')
    fh.write(content)
    fh.close()


def split_up(in_file, out_dir):
    segments = []
    doc = html.parse(in_file)
    for sect1 in doc.findall('//div[@class="sect1"]'):
        sect1_title = sect1.find('h2')
        print([sect1_title.text])
        name = sect1_title.get('id').strip('_')
        sect1_title_text = sect1_title.text
        for i, sect2 in enumerate(sect1.findall('.//div[@class="sect2"]')):
            sect2_title = sect2.find('h3')
            print([sect2_title.text])
            segments.append({
                'name': name + '_' + str(i),
                'title': sect2_title.text,
                'body': clean_html(sect2).decode('utf-8'),
                'el': sect2,
                'parent_name': name,
                'parent_title': sect1_title_text
                })
            sect2.getparent().remove(sect2)
        segments.append({
            'name': name,
            'title': sect1_title_text,
            'body': clean_html(sect1).decode('utf-8'),
            'el': sect1,
            'parent_name': None,
            'parent_title': None
            })

    for segment in segments:
        segment['short_title'] = segment['title'] #.rsplit('(')[0]
        segment['children'] = [s for s in segments if s['parent_name'] == segment['name']]
    sorted_segments = []
    for segment in segments:
        if segment['parent_name']:
            continue
        sorted_segments.append(segment)
        for s in segment.get('children', []):
            s['parent'] = segment
            sorted_segments.append(s)

    for i, segment in enumerate(sorted_segments):
        if i < len(sorted_segments) - 1:
            if len(segment['children']):
                for s in sorted_segments[i + 1:]:
                    if len(s['children']):
                        segment['next_title'] = s['title']
                        segment['next_name'] = s['name']
                        break
            else:
                segment['next_title'] = sorted_segments[i + 1]['title']
                segment['next_name'] = sorted_segments[i + 1]['name']
        #pprint(segment)
        write_segment(segment, out_dir)
    write_index(sorted_segments, out_dir)

if __name__ == '__main__':
    split_up('book.html', '')
