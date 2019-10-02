# -*- coding: UTF-8 -*-:

from phs import spider, newsBase

import re
import datetime
import bs4

class NanjingUniversityNews(newsBase.NewsParserBase):
     def __init__(self):
         super().__init__()
         
     def parse_html(self): 
         #one 
         urls = ["https://grawww.nju.edu.cn/905/list.htm", "https://grawww.nju.edu.cn/910/list.htm",
                 "https://grawww.nju.edu.cn/911/list.htm", "https://grawww.nju.edu.cn/912/list.htm",
                 "https://grawww.nju.edu.cn/913/list.htm", "https://grawww.nju.edu.cn/916/list.htm"]
         for url in urls:
             self.set_target_url(url)
             target_tags = self.get_tag_by_attr(tag="ul", attr="class", value="wp_article_list")
             self.parse_target_tags(target_tags, self.url, "南京大学", "研究生院", is_deeper = False) 

         #two 
         self.set_target_url("https://cs.nju.edu.cn/1654/list.htm")
         target_tags = self.get_tag_by_attr(tag="ul", attr="class", value="wp_article_list")
         #root_url = "http://yz.tsinghua.edu.cn"
         self.parse_target_tags(target_tags, self.url, "南京大学", "计算机科学与技术系", is_deeper = False)
         
         #three 
         #self.set_target_url("http://software.nju.edu.cn")
         #target_tags = self.get_tag_by_attr(tag="ul", attr="class", value="wp_article_list")
         #root_url = "http://www.cs.tsinghua.edu.cn"
         #self.parse_target_tags(target_tags, root_url, "南京大学", "软件学院", is_deeper = True)

         return self.news_list

if __name__ == '__main__':
    news_instance = NanjingUniversityNews()
    news_list = news_instance.parse_html()
    print("All news:")
    for news in news_list:
        print(news.get_university(), news.school, news.title, news.date, news.href)
    today_news = news_instance.get_today_news()
    print("today_news:")
    for news in today_news:
        print(news.get_university(), news.school, news.title, news.date, news.href)
