# -*- coding: UTF-8 -*-:

from phs import spider, newsBase

import re
import datetime
import bs4

class PekingNews(newsBase.NewsParserBase):
     def __init__(self):
         super().__init__()
         
     def parse_html(self): 
         #one 
         self.set_target_url("https://admission.pku.edu.cn/tzgg/index.htm")
         target_tags = self.get_tag_by_attr(tag="ul", attr="class", value="zsxx_cont_list")
         root_url = "https://admission.pku.edu.cn"
         self.parse_target_tags(target_tags, root_url, "北京大学", "研究生招生-通知公告", is_deeper = False) 

         #two 
         self.set_target_url("https://admission.pku.edu.cn/zsxx/index.htm")
         target_tags = self.get_tag_by_attr(tag="ul", attr="class", value="zsxx_cont_list")
         root_url = "https://admission.pku.edu.cn"
         self.parse_target_tags(target_tags, root_url, "北京大学", "研究生招生-招生新闻", is_deeper = False)
         
         #three 
         self.set_target_url("http://eecs.pku.edu.cn/xygk1/xyxw.htm")
         target_tags = self.get_tag_by_attr(tag="ul", attr="class", value="xyxwM2")
         root_url = "http://www.cs.tsinghua.edu.cn"
         #self.parse_target_tags(target_tags, root_url, "北京大学", "信息科学技术学院", is_deeper = False)
         
         self.set_target_url("http://www.ss.pku.edu.cn/index.php/newscenter")
         target_tags = self.get_tag_by_attr(tag="ul", attr="id", value="info-list-ul")
         print("###", target_tags)
         root_url = "http://www.ss.pku.edu.cn"
         self.parse_target_tags(target_tags, root_url, "北京大学", "软件与微电子学院", is_deeper = False)

         return self.news_list


if __name__ == '__main__':
    news_instance = PekingNews()
    news_list = news_instance.parse_html()
    print("All news:")
    for news in news_list:
        print(news.get_university(), news.school, news.title, news.date, news.href)
    today_news = news_instance.get_today_news()
    print("today_news:")
    for news in today_news:
        print(news.get_university(), news.school, news.title, news.date, news.href)
