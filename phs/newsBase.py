# -*- coding: UTF-8 -*-

import phs.spider
import datetime
from abc import abstractmethod
import re
import bs4
import time

class News:
     """
   This class is used to describe a news. 
   
   Args:
     university: 
     school:
     title:
     date: 
     href:  
     """
      
     def  __init__(self, university ="", school ="", 
                   title ="", date ="", href=""):
          self.university = university
          self.school = school
          self.title = title
          self.date = date
          self.href = href
     
     def get_university(self):
         return self.university

     def get_school(self):
         return self.school

     def get_title(self):
         return self.title
     
     def get_date(self):
         return self.date

class NewsParserBase:

     """
   The abstract base class is used to parse news from every university.
     """
     def __init__(self):
         self.news_list = []

     def set_target_url(self, url = ""):
         '''
           You can change the website url to support multi website for one collegue
           eg: for Tsinghua university you may get news from 3 website:
               http://yz.tsinghua.edu.cn/publish/yjszs/8562/index.html
               http://yz.tsinghua.edu.cn/publish/yjszs/8550/index.html
               http://www.cs.tsinghua.edu.cn
         '''
         self.url = url
         self.soup = phs.spider.Spider(url).soup() #convert html to BeautifulSoup object
      
     def get_tag_by_attr(self, tag = "ul", attr = "", value = ""):
          '''
          The news list are generally 'ul/table' tag with specific 'class' name in html.
          Every news is generally a 'href' tag (hyperlink).
          For example:
              <ul class="nlist">
                 <div> 
                  <li class="zhiti"><span style="float: right;">[2019-09-27]</span><a href="/2019/0927/c11157a209885/page.htm" title=""></a></li>
                                        
                  <li class="zhiti"><span style="float: right;">[2019-09-27]</span><a href="/2019/0927/c11157a209884/page.htm" title=""></a></li>
                 </div>
              </ul>
          '''
          tags = None
          for body in self.soup:
              if attr == "":
                 body.find_all(tag)
              else:
                 tags = body.find_all(tag, attrs={attr:value})
              if tags is not None and len(tags):
                 break 
          return tags

     def validate(self, date_text):
          try:
              if date_text != datetime.datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d'):
                  raise ValueError
              return True
          except ValueError:
              return False
 
     def get_news_date(self, tag = None):
         '''
         DFS(Depth First Search) is used to find the news date
         '''
         date_str = re.search(r"(\d{4}-\d{1,2}-\d{1,2})",str(tag))
         if date_str is not None and self.validate(date_str[0]):
            return datetime.datetime.strptime(date_str[0], "%Y-%m-%d")
         
         #date_str = re.search(r"(\d{1,2}-\d{1,2})",str(tag))
         #if date_str is not None:
         #   now_year = datetime.datetime.now().strftime("%Y")
         #   if self.validate(now_year + "-" + date_str[0]):
         #      return datetime.datetime.strptime(now_year + "-" + date_str[0], "%Y-%m-%d")
 
         if isinstance(tag, bs4.element.Tag):
            for child in tag.children:
                self.get_news_date(child)
   
     def get_current_url_directory(self):
         if self.url.find("htm") != -1:
            last_sep_index = self.url.rfind("/") 
            return self.url[0:last_sep_index + 1]        
         else:
            return self.url + "/" 
   
     def get_date_by_href_html_date_format_1(self, href = ""):
         href = href if href.find("http") == 0 else self.get_current_url_directory() + href 
         href_soup = str(phs.spider(href).soup())
         date_str = re.search(r"(\d{4}-\d{1,2}-\d{1,2})",str(href_soup))
         if date_str is not None and self.validate(date_str[0]):
            return datetime.datetime.strptime(date_str[0], "%Y-%m-%d")

     def get_date_by_href_html_date_format_2(self, href = ""):
         href = href if href.find("http") == 0 else self.get_current_url_directory() + href
         href_soup = str(phs.spider(href).soup())
         date_str = re.search(r"(\d{4}年\d{1,2}月\d{1,2}日)",str(href_soup))
         if date_str is not None and self.validate(date_str[0]):
            return datetime.datetime.strptime(date_str[0], "%Y年%m月%d日")

     def parse_target_tags(self, tags = None, root_url = "", 
                           university = "", school = "", is_deeper = False, date_format = 0):
         '''
         Generally, every news is hyperlink.
         '''
         if tags is None:
            return
         for tag in tags:
             for child in tag.children:
                 if is_deeper:
                     for child_child in child:
                          date = self.get_news_date(child_child)
                          a_tag = child_child.find("a")
                          if a_tag is not None \
                             and isinstance(a_tag, bs4.element.Tag):
                              attrs = a_tag.attrs
                              href = attrs['href'] if attrs['href'].find("http") == 0 \
                                      else self.get_current_url_directory() + attrs['href']
                              title = a_tag.text
                              if date_format == 1:
                                  date = self.get_date_by_href_html_date_format_1(attrs['href'])
                              elif date_format == 2:
                                  date = self.get_date_by_href_html_date_format_2(attrs['href'])


                              if date is not None:
                                 self.news_list.append(News(university = university,
                                                    school = school, title = title,
                                                    date = date, href = href))                  
                 else:
                     date = self.get_news_date(child)
                     a_tag = child.find("a")
                     if a_tag is not None \
                        and isinstance(a_tag, bs4.element.Tag):
                         attrs = a_tag.attrs
                         href = attrs['href']  if attrs['href'].find("http") == 0 \
                                else self.get_current_url_directory() + attrs['href']
                         title = a_tag.text
                         if date_format == 1:
                             date = self.get_date_by_href_html_date_format_1(attrs['href'])
                         elif date_format == 2:
                             date = self.get_date_by_href_html_date_format_2(attrs['href'])

                         if date is not None:
                            self.news_list.append(News(university = university,
                                               school = school, title = title,
                                               date = date, href = href))
               

     @abstractmethod
     def parse_html(self):
         '''
         This is abstractmethod and must be overwrite in subclass.         
         The steps are as follows:
            1. set_target_url 
               Set the source url where you want to get news
            2. get_tag_by_attr
               Get target tags block  by specific tag name with attr.
               such "<div class="bs_infor>"" 
            3. get_news_date and parse_target_tags will be used
               to get news.  
         '''  
         raise RuntimeError(' "parse_html". method must be overwrite in subclass')
      
     def get_today_news(self):
         '''
        we will make a timed task used this function
         '''
         now_time = datetime.datetime.now()
         today_news = []
         for news in self.news_list:
              time_delta = now_time - news.date
              if time_delta.days < 1:
                 today_news.append(news)
         return today_news
          
          
