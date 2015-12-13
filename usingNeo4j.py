#!/usr/bin/python
# -*- coding: utf-8 -*-

from getData import *
from py2neo import Graph,node,Relationship
from neo4j import Node

class usingNeo4j:
    
    def __init__(self):
        self.url="http://user:password@ip:7474/db/data/"
        self.graph = Graph(self.url)
        self.graph.cypher.execute("CREATE (SJTU:University {name:'上海交通大学',url:'www.sjtu.edu.cn'})",)
        
    def createNode(self,id,what,name,url):
    #    cmd="No extension found at path %r on graph <%s>" % (name, url)
        cmd="CREATE (%s:`%s` {name:'%s',url:'%s'})" % (id,what,name,url)
        print cmd
        self.graph.cypher.execute(cmd)
    
    def createRelation(self,node1,relation,node2):
        cmd="MATCH (a:`%s`),(b:`%s`) CREATE (b)-[:`%s`]->(a) RETURN a,b" % (node1,node2,relation)
        print cmd
        self.graph.cypher.execute(cmd)
    #    cmd2="CREATE (%s)-[r:`%s`]->(%s)" % (node1,relation,node2)
    #    Relationship(node1,relation,node2)
    
    def cmd(self,cmd):
        print cmd
        self.graph.cypher.execute(cmd)
        
    def showAll(self):
        self.graph.cypher.execute("MATCH (n) RETURN n")  
    
    def deleteAll(self): 
        self.graph.cypher.execute("MATCH (n) DETACH DELETE n")   
    #def relationShip(self,node1,node2,relation):
    


