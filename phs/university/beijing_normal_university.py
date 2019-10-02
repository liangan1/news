# -*- coding: UTF-8 -*-:

from phs import spider, newsBase

import re
import datetime
import bs4

class BeijingNormalNews(newsBase.NewsParserBase):
     def __init__(self):
         super().__init__()
         
     def parse_html(self): 
         #one 
         self.set_target_url("http://yz.bnu.edu.cn/list/master")
         target_tags = self.get_tag_by_attr(tag="ul", attr="style", value="min-height:200px;")
         root_url = "http://yz.bnu.edu.cn"
         self.parse_target_tags(target_tags, root_url, "北京师范大学", "研究生招生信息网-硕士", is_deeper = False) 

         #two 
         self.set_target_url("https://cist.bnu.edu.cn/xyxw/index.html")
         target_tags = self.get_tag_by_attr(tag="ul", attr="class", value="list01")
         root_url = "http://cist.bnu.edu.cn"
         self.parse_target_tags(target_tags, root_url, "北京师范大学", "人工智能学院-学院新闻", is_deeper = False)
         
         #three 
         self.set_target_url("https://cist.bnu.edu.cn/tzgg/index.html")
         target_tags = self.get_tag_by_attr(tag="ul", attr="class", value="list01")
         root_url = "http://cist.bnu.edu.cn"
         self.parse_target_tags(target_tags, root_url, "北京师范大学", "人工智能学院-通知公告", is_deeper = False)

         return self.news_list

if __name__ == '__main__':
    news_instance = BeijingNormalNews()
    news_list = news_instance.parse_html()
    print("All news:")
    for news in news_list:
        print(news.get_university(), news.school, news.title, news.date, news.href)
    today_news = news_instance.get_today_news()
    print("today_news:")
    for news in today_news:
        print(news.get_university(), news.school, news.title, news.date, news.href)
