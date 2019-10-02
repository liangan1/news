# -*- coding: UTF-8 -*-:

from phs import spider, newsBase

import re
import datetime
import bs4

class BeihangNews(newsBase.NewsParserBase):
     def __init__(self):
         super().__init__()
         
     def parse_html(self): 
         #one 
         self.set_target_url("http://yzb.buaa.edu.cn/zxsd/dtxx.htm")
         target_tags = self.get_tag_by_attr(tag="ul", attr="class", value="newslist")
         root_url = "http://yzb.buaa.edu.cn"
         self.parse_target_tags(target_tags, root_url, "北京航天航空大学", "研究生招生信息网", is_deeper = False) 

         #two 
         self.set_target_url("http://scse.buaa.edu.cn/")
         target_tags = self.get_tag_by_attr(tag="ul", attr="class", value="list_one")
         root_url = "http://http://scse.buaa.edu.cn/"
         #self.parse_target_tags(target_tags, root_url, "北京航天航空大学", "计算机学院", is_deeper = False)
         
         #three 
         self.set_target_url("http://soft.buaa.edu.cn")
         target_tags = self.get_tag_by_attr(tag="ul", attr="class", value="dynamic_list dynamic_listb dynamic_liste fr")
         print(target_tags)
         root_url = "http://soft.buaa.edu.cn"
         #self.parse_target_tags(target_tags, root_url, "北京航天航空大学", "软件学院", is_deeper = False)

         return self.news_list

if __name__ == '__main__':
    news_instance = BeihangNews()
    news_list = news_instance.parse_html()
    print("All news:")
    for news in news_list:
        print(news.get_university(), news.school, news.title, news.date, news.href)
    today_news = news_instance.get_today_news()
    print("today_news:")
    for news in today_news:
        print(news.get_university(), news.school, news.title, news.date, news.href)
