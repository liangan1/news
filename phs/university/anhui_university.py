# -*- coding: UTF-8 -*-:

from phs import spider, newsBase

import re
import datetime

class AHUCSNews(newsBase.NewsParserBase):
     def __init__(self, url = "http://cs.ahu.edu.cn/11157/list.htm"):
         super().__init__(url)
         
     def parse_html(self): 
         a_tags = self.get_tag_by_name("ul", "nlist")
         root_url = "cs.ahu.edu.cn"
         for li_tag in a_tags.find_all("li"):
               a_tag = li_tag.find("a")
               attrs = a_tag.attrs
               href = root_url + attrs['href']
               title = a_tag.text
               date_str = re.search(r"(\d{4}-\d{1,2}-\d{1,2})",li_tag.text)[0]
               date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
               self.news_list.append(newsBase.News(university = "安徽大学",
                                     school = "计算机学院", title = title, 
                                     date = date, href = href))
               
         return self.news_list

if __name__ == '__main__':
    news_instance = AHUCSNews()
    news_list = news_instance.parse_html()
    for news in news_list:
        print(news.get_university(), news.school, news.title, news.date, news.href)
     
