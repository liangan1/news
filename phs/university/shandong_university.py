# -*- coding: UTF-8 -*-:

from phs import spider, newsBase

import re
import datetime
import bs4

class ShandongUniversityNews(newsBase.NewsParserBase):
     def __init__(self):
         super().__init__()
         
     def parse_html(self): 
         #one 
         urls = ["http://www.yz.sdu.edu.cn/bkzn/zsjz.htm",
                 "http://www.yz.sdu.edu.cn/bkzn/zyml.htm",
                 "http://www.yz.sdu.edu.cn/bkzn/xzxf.htm"]
         for url in urls:#日期难处理
             self.set_target_url(url)
             target_tags = self.get_tag_by_attr(tag="div", attr="id", value="div_more_news")
             self.parse_target_tags(target_tags, self.url, "山东大学", "研究生招生网-招生简章", is_deeper = False, date_format = 1) 

         #one
         urls = ["http://www.yz.sdu.edu.cn/bkzn/ssblb.htm",
                 "http://www.yz.sdu.edu.cn/bkzn/ssfsx.htm"]
         for url in urls:#日期难处理
             self.set_target_url(url)
             target_tags = self.get_tag_by_attr(tag="div", attr="id", value="div_more_news")
             self.parse_target_tags(target_tags, self.url, "山东大学", "研究生招生网-复试信息", is_deeper = False, date_format = 1)

         #two 
         self.set_target_url("http://www.yz.sdu.edu.cn/tzgg.htm")
         target_tags = self.get_tag_by_attr(tag="div", attr="class", value="newscontent")
         self.parse_target_tags(target_tags, self.url, "山东大学", "研究生招生网-通知公告", is_deeper = False)
         
         #three 
         self.set_target_url("http://www.cs.sdu.edu.cn/index/xygg.htm")
         target_tags = self.get_tag_by_attr(tag="div", attr="class", value="sub_text")
         self.parse_target_tags(target_tags, self.url, "山东大学", "计算机科学与技术学院", is_deeper = False)

         #four
         self.set_target_url("http://www.sc.sdu.edu.cn")
         target_tags = self.get_tag_by_attr(tag="div", attr="class", value="newslist")
         self.parse_target_tags(target_tags, self.url, "山东大学", "软件学院", is_deeper = True)

        
         return self.news_list

if __name__ == '__main__':
    news_instance = ShandongUniversityNews()
    news_list = news_instance.parse_html()
    print("All news:")
    for news in news_list:
        print(news.get_university(), news.school, news.title, news.date, news.href)
    today_news = news_instance.get_today_news()
    print("today_news:")
    for news in today_news:
        print(news.get_university(), news.school, news.title, news.date, news.href)
