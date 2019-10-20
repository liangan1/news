# -*- coding: UTF-8 -*-:

from phs import spider, newsBase

import re
import datetime
import bs4

class TianjinUniversityNews(newsBase.NewsParserBase):
     def __init__(self):
         super().__init__()
         
     def parse_html(self): 
         #one 
         urls = ["http://yzb.tju.edu.cn/xwzx/zxxx/",
                 "http://yzb.tju.edu.cn/xwzx/tztg/",
                 "http://yzb.tju.edu.cn/xwzx/tkss_xw/",
                 "http://yzb.tju.edu.cn/xwzx/zzxw/"]
         for url in urls:
             self.set_target_url(url)
             target_tags = self.get_tag_by_attr(tag="table", attr="width", value="97%")
             root_url = url
             self.parse_target_tags(target_tags, root_url, "天津大学", "研究生院-新闻中心", is_deeper = False) 

         #two 
         urls = ["http://cs.tju.edu.cn/csweb/tzgg"]
         for url in urls:
             self.set_target_url(url)
             root_url ="http://cs.tju.edu.cn/"
             print(self.soup)
             target_tags = self.get_tag_by_attr(tag="div", attr="id", value="textframe")
             print(target_tags)
             self.parse_target_tags(target_tags, root_url, "天津大学", "计算机科学与技术学院", is_deeper = False)
         
         #three 
         #self.set_target_url("http://software.nju.edu.cn")
         #target_tags = self.get_tag_by_attr(tag="ul", attr="class", value="wp_article_list")
         #root_url = "http://www.cs.tsinghua.edu.cn"
         #self.parse_target_tags(target_tags, root_url, "南京大学", "软件学院", is_deeper = True)

         return self.news_list

if __name__ == '__main__':
    news_instance = TianjinUniversityNews()
    news_list = news_instance.parse_html()
    print("All news:")
    for news in news_list:
        print(news.get_university(), news.school, news.title, news.date, news.href)
    today_news = news_instance.get_today_news()
    print("today_news:")
    for news in today_news:
        print(news.get_university(), news.school, news.title, news.date, news.href)
