## 记录了一些python 爬虫的代码
其中一部分的代码只是留下来做个记录, 可以真正起到爬虫作用的代码如下:

1. `Spider/maoYanBoxOffice`: 爬取猫眼票房的票房记录并存储到MySQL数据库
2. `Spider/zhihuAnalysis`: 爬取知乎中粉丝排名靠前（由看知乎中获取）的用户的粉丝的相关信息, 存储到数据库
3. `Spider/jiandan`: 获取煎蛋网中的图片并存储
以上三个项目都是刚学习爬虫的时候写的, 没有利用爬虫框架, 都是单线程爬虫. 代码写得不好, 暂时也没有重写的打算, 等将来需要的时候再重新写一遍.


1.`douban`: 利用scrapy框架写的豆瓣电影爬虫, 获取电影信息并保存到数据库中.
