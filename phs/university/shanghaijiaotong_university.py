# -*- coding: UTF-8 -*-:

from phs import spider, newsBase

import re
import datetime
import bs4

class ShanghaiJiaoTongUniversityNews(newsBase.NewsParserBase):
     def __init__(self):
         super().__init__()
         
     def parse_html(self): 
         #one
         urls = ["https://yzb.sjtu.edu.cn/index/zkxx/bszs.htm",
                 "https://yzb.sjtu.edu.cn/index/zkxx/sszs.htm"] 
         for url in urls:
             self.set_target_url(url)
             target_tags = self.get_tag_by_attr(tag="div", attr="class", value="Newslist")
             target_tags = target_tags[0].find_all("ul")
             self.parse_target_tags(target_tags, self.url, "上海交通大学", "研究生院招生网-硕博招生", is_deeper = False) 

         #two 
         self.set_target_url("https://yzb.sjtu.edu.cn/zsjz/ssszs.htm")
         target_tags = self.get_tag_by_attr(tag="div", attr="class", value="Newslist")
         for tag in target_tags:
             tag = tag.find_all("ul")
             self.parse_target_tags(tag, self.url, "上海交通大学", "研究生招生网-招生简章", is_deeper = False)
         
         #three 
         #self.set_target_url("http://www.se.sjtu.edu.cn") ##待处理
         #target_tags = self.get_tag_by_attr(tag="ul", attr="class", value="wp_article_list")
         #root_url = "http://www.cs.tsinghua.edu.cn"
         #self.parse_target_tags(target_tags, self.url, "南京大学", "软件学院", is_deeper = True)
         
         #four
         #self.set_target_url("http://www.cs.sjtu.edu.cn")##待处理
         #target_tags = self.get_tag_by_attr(tag="ul", attr="class", value="wp_article_list")
         #root_url = "http://yz.tsinghua.edu.cn"
         #self.parse_target_tags(target_tags, self.url, "复旦大学", "研究生院-通知公告", is_deeper = False)

         return self.news_list

if __name__ == '__main__':
    news_instance = ShanghaiJiaoTongUniversityNews()
    news_list = news_instance.parse_html()
    print("All news:")
    for news in news_list:
        print(news.get_university(), news.school, news.title, news.date, news.href)
    today_news = news_instance.get_today_news()
    print("today_news:")
    for news in today_news:
        print(news.get_university(), news.school, news.title, news.date, news.href)
