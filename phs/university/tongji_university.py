# -*- coding: UTF-8 -*-:

from phs import spider, newsBase

import re
import datetime
import bs4

class TongjiUniversityNews(newsBase.NewsParserBase):
     def __init__(self):
         super().__init__()
         
     def parse_html(self): 
         #one 
         urls = ["https://see.tongji.edu.cn/index/gg.htm",
                 "https://see.tongji.edu.cn/index/tz.htm",
                 "https://see.tongji.edu.cn/index/xyxw.htm"]
         for url in urls:
             self.set_target_url(url)
             target_tags = self.get_tag_by_attr(tag="ul", attr="class", value="ss")
             self.parse_target_tags(target_tags, self.url, "同济大学", "电子与信息工程学院", is_deeper = False) 

         #two 
         self.set_target_url("https://yz.tongji.edu.cn/")
         target_tags = self.get_tag_by_attr(tag="ul", attr="class", value="listul")
         #root_url = "http://yz.tsinghua.edu.cn"
         self.parse_target_tags(target_tags, self.url, "同济大学", "研究生招生网", is_deeper = False)
         
         #three 
         self.set_target_url("https://yz.tongji.edu.cn/zsjz.htm")
         target_tags = self.get_tag_by_attr(tag="div", attr="class", value="list_main_content")
         #root_url = "http://www.cs.tsinghua.edu.cn"
         self.parse_target_tags(target_tags, self.url, "同济大学", "研究生招生网-招生简章", is_deeper = True)

         #four
         self.set_target_url("https://yz.tongji.edu.cn/zsxw.htm")
         target_tags = self.get_tag_by_attr(tag="div", attr="class", value="list_main_content")
         #root_url = "http://www.cs.tsinghua.edu.cn"
         self.parse_target_tags(target_tags, self.url, "同济大学", "研究生招生网-招生新闻", is_deeper = True)

         #five
         self.set_target_url("https://yz.tongji.edu.cn/lssj.htm")
         target_tags = self.get_tag_by_attr(tag="div", attr="class", value="list_main_content")
         #root_url = "http://www.cs.tsinghua.edu.cn"
         self.parse_target_tags(target_tags, self.url, "同济大学", "研究生招生网-历史数据", is_deeper = True)

         #six
         #self.set_target_url("https://me.tongji.edu.cn/") # 维护 待处理
         #target_tags = self.get_tag_by_attr(tag="div", attr="class", value="list_main_content")
         #root_url = "http://www.cs.tsinghua.edu.cn"
         #self.parse_target_tags(target_tags, self.url, "同济大学", "研究生招生网-历史数据", is_deeper = True)
  

         return self.news_list

if __name__ == '__main__':
    news_instance = TongjiUniversityNews()
    news_list = news_instance.parse_html()
    print("All news:")
    for news in news_list:
        print(news.get_university(), news.school, news.title, news.date, news.href)
    today_news = news_instance.get_today_news()
    print("today_news:")
    for news in today_news:
        print(news.get_university(), news.school, news.title, news.date, news.href)
