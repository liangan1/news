# -*- coding: UTF-8 -*-:

from phs import spider, newsBase

import re
import datetime
import bs4

class TsingHuaCSNews(newsBase.NewsParserBase):
     def __init__(self):
         super().__init__()
         
     def parse_html(self): 
         #one 
         self.set_target_url("http://yz.tsinghua.edu.cn/publish/yjszs/8562/index.html")
         target_tags = self.get_tag_by_attr(tag="div", attr="class", value="bs_infor")
         root_url = "http://yz.tsinghua.edu.cn"
         self.parse_target_tags(target_tags, root_url, "清华大学", "研究生招生-最新通知", is_deeper = False) 

         #two 
         self.set_target_url("http://yz.tsinghua.edu.cn/publish/yjszs/8550/index.html")
         target_tags = self.get_tag_by_attr(tag="div", attr="class", value="bs_infor")
         root_url = "http://yz.tsinghua.edu.cn"
         self.parse_target_tags(target_tags, root_url, "清华大学", "研究生招生-硕士通知公告", is_deeper = False)
         
         #three 
         self.set_target_url("http://www.cs.tsinghua.edu.cn/publish/cs/4723/index.html")
         target_tags = self.get_tag_by_attr(tag="div", attr="class", value="box_list")
         root_url = "http://www.cs.tsinghua.edu.cn"
         self.parse_target_tags(target_tags, root_url, "清华大学", "计算机科学与技术系", is_deeper = True)

         return self.news_list

if __name__ == '__main__':
    news_instance = TsingHuaCSNews()
    news_list = news_instance.parse_html()
    print("All news:")
    for news in news_list:
        print(news.get_university(), news.school, news.title, news.date, news.href)
    today_news = news_instance.get_today_news()
    print("today_news:")
    for news in today_news:
        print(news.get_university(), news.school, news.title, news.date, news.href)
