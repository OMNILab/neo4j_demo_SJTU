#!/usr/bin/python
# -*- coding: utf-8 -*-

#
#Author: Pengfei Shi <shipengfei92@gmail.com>
#

from getData import *
from usingNeo4j import *
from _ast import List
#import getData 

if __name__=="__main__":
    
    url1="http://www.sjtu.edu.cn/xbdh/yjdh/gk/jgsz/jgbc.htm"
    s=getData(url1)
    s.getPages()
    s.getContext()
    
    department=["党务部门","行政部门","直属单位","附属医院","附属学校","学院（系）","研究院"]
    
#    list=s.re(r'(?<=#8a9046">).*(?=</font>)')
    
 
    list0=s.re(r'(?<="c51084">).*(?=</a>)')
    list1=s.re(r'(?<="c51085">).*(?=</a>)')
    list2=s.re(r'(?<="c51273">).*(?=</a>)')
    list3=s.re(r'(?<="c51244">).*(?=</a>)')
    list4=s.re(r'(?<="c51245">).*(?=</a>)')
    

#   listname=s.re(r'(?<="_blank" title=").*(?=" class=")')
    
    connection=usingNeo4j()
    
    for i in range(0,len(department)):
        connection.createNode("department1_"+str(i),"Department"+str(i),department[i],"")
        connection.createRelation("University", "机关部处", "Department"+str(i))
    
    
    
#        for j in range(0,len(list2[i])):
#            print list2[i][j]
#            connection.createNode("department2_"+str(j),department[i],list[i][j],"")  
    
    for i in range(0,len(list0)):
        print list0[i]
        connection.createNode("department2_"+str(i),department[0],list0[i],"")    
        
    connection.createRelation("Department0", "下属机构", department[0])
    
    for i in range(0,len(list1)):
        print list1[i]
        connection.createNode("department2_"+str(i),department[1],list1[i],"")    
        
    connection.createRelation("Department1", "下属机构", department[1])
        
    for i in range(0,len(list2)):
        print list2[i]
        connection.createNode("department2_"+str(i),department[2],list2[i],"")    
        
    connection.createRelation("Department2", "下属机构", department[2])
        
    for i in range(0,len(list3)):
        print list3[i]
        connection.createNode("department2_"+str(i),department[3],list3[i],"")    
    
    connection.createRelation("Department3", "下属机构", department[3])
        
    for i in range(0,len(list4)):
        print list4[i]
        connection.createNode("department2_"+str(i),department[4],list4[i],"")    
        
    connection.createRelation("Department4", "下属机构", department[4])
    
    
    url2="http://www.sjtu.edu.cn/xbdh/yjdh/yx/xy_x_.htm"
    s2=getData(url2)
    s2.getPages()
    s2.getContext()
    
    list5=s2.re(r'(?<="c51280">).*(?=</a>)')
    
    for i in range(0,len(list5)):
        print list5[i]
        connection.createNode("department2_"+str(i),department[5],list5[i],"")    
        
    connection.createRelation("Department5", "下属机构", department[5])    
 
 
    url3="http://www.sjtu.edu.cn/xbdh/yjdh/yx/yjy.htm"
    s3=getData(url3)
    s3.getPages()
    s3.getContext()
    
    list6=s3.re(r'(?<="c51280">).*(?=</a>)')
    
    for i in range(0,len(list6)):
        print list6[i]
        connection.createNode("department2_"+str(i),department[6],list6[i],"")    
        
    connection.createRelation("Department6", "下属机构", department[6])  
        
    #connection.cmd("")
    #for i in range(0,len(list2url)):
    #    print list2url[i]
    #connection.deleteAll()
    
    
    
       