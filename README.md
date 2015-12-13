# neo4j_demo_SJTU
这是一个利用neo4j将交大打组织架构进行可视化展示的demo代码。

爬取的数据均来自交大官网：

http://www.sjtu.edu.cn/xbdh/yjdh/gk/jgsz/jgbc.htm

http://www.sjtu.edu.cn/xbdh/yjdh/yx/xy_x_.htm


##main.py

匹配抓取数据，并上传至neo4j数据库

##getData.py

用于网页内容获取与正则表达式的函数

##usingNeo4j.py

主要用于建立与neo4j数据库的链接，以及创建节点和关系等基本操作

