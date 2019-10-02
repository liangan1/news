# -*- coding: UTF-8 -*-:

from phs import spider, newsBase

import re
import datetime
import bs4

class ChinineseAcademyOfScienceNews(newsBase.NewsParserBase):
     def __init__(self):
         super().__init__()
         
     def parse_html(self): 
         #one 
         self.set_target_url("http://admission.ucas.ac.cn/")
         target_tags = self.get_tag_by_attr(tag="ul", attr="class", value="mp-list")
         root_url = "http://admission.ucas.ac.cn/"
         self.parse_target_tags(target_tags, root_url, "中国科学院大学", "官网", is_deeper = False) 

         #two 
         self.set_target_url("http://www.ict.cas.cn/yjsjy/zs/jsszs/")
         target_tags = self.get_tag_by_attr(tag="table", attr="width", value="692")
         root_url = "http://www.ict.cas.cn"
         self.parse_target_tags(target_tags, root_url, "中国科学院大学", "硕士招生", is_deeper = False)
        
         #three 
         self.set_target_url("http://www.iscas.ac.cn/xwdt2016/rdxw2016/")#热点新闻
         target_tags = self.get_tag_by_attr(tag="div", attr="class", value="list-news")
         self.parse_target_tags(target_tags, self.url, "中国科学院大学", "软件研究所", is_deeper = True)
         self.set_target_url("http://www.iscas.ac.cn/xwdt2016/kyjz2016/")#科技进展
         target_tags += self.get_tag_by_attr(tag="div", attr="class", value="list-news")
         self.parse_target_tags(target_tags, self.url, "中国科学院大学", "软件研究所", is_deeper = True)
         self.set_target_url("http://www.iscas.ac.cn/xwdt2016/kjdt2016/")#科技动态
         target_tags += self.get_tag_by_attr(tag="div", attr="class", value="list-news")
         self.parse_target_tags(target_tags, self.url, "中国科学院大学", "软件研究所", is_deeper = True)
         self.set_target_url("http://www.iscas.ac.cn/xwdt2016/kjdt2016/")#通知公告
         target_tags += self.get_tag_by_attr(tag="div", attr="class", value="list-news")
         self.parse_target_tags(target_tags, self.url, "中国科学院大学", "软件研究所", is_deeper = True)
         self.set_target_url("http://www.is.cas.cn/yjsjy2016/zsxx2016/")#招生信息
         target_tags += self.get_tag_by_attr(tag="div", attr="class", value="list-news")        
         self.parse_target_tags(target_tags, root_url, "中国科学院大学", "软件研究所", is_deeper = True)
         
         return self.news_list

if __name__ == '__main__':
    news_instance = ChinineseAcademyOfScienceNews()
    news_list = news_instance.parse_html()
    print("All news:")
    for news in news_list:
        print(news.get_university(), news.school, news.title, news.date, news.href)
    today_news = news_instance.get_today_news()
    print("today_news:")
    for news in today_news:
        print(news.get_university(), news.school, news.title, news.date, news.href)
