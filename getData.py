#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import re


class getData:
    
    def __init__(self,url):
        self.url=url
        #self.url="http://www.sjtu.edu.cn/xbdh/yjdh/gk/jgsz/jgbc.htm"
        
    def getPages(self):
        print self.url
        
    def getContext(self):
        self.response=urllib2.urlopen(self.url)
        self.read=self.response.read()
        #print self.read
    
    def re(self,pattern):
        self.result=re.findall(pattern,self.read)
        print self.result
        return self.result
        
    
    

        
        
