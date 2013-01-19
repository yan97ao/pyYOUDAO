#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sys
import urllib2
import re

def get_elements(xml, elem):
    p = re.compile("<" + elem + ">" + "(.*?)</" + elem + ">", re.DOTALL)
    it = p.findall(xml)
    return it

def main():
    if len(sys.argv) != 2 :
        usage()

    word = sys.argv[1]
    print "单词：\t",word
    url = 'http://dict.youdao.com/fsearch?q='+word
    content = (urllib2.urlopen(url).read())
    
    phonetic = get_elements(content,"phonetic-symbol")
    print "音标：\t",phonetic[0]
    
    trans = get_elements(content,"content")
    get_content = re.compile("\!\[CDATA\[(.*?)\]\]", re.DOTALL)
    print "释义："
    for t in trans:
        s=get_content.findall(t)
        print '\t',s[0]

def usage():
    print "usage:./pyYOUDAO word<cr>"
    exit()

if __name__ == '__main__':
    main()
