# -*- coding: UTF-8 -*-

from spider import Spider
import datetime
from abc import abstractmethod

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
     def __init__(self, url=""):
          self.url = url
          self.soup = Spider(url).soup() #convert html to BeautifulSoup object
          self.news_list = []
      
     def get_tag_by_name(self, tag = "ul", class_name = ""):
          '''
          The news list are generally 'ul/table' tag with specific 'class' name in html.
          Every news is generally a 'ref' tag.
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
              tags = body.find(tag, attrs={"class":class_name})
              if tags is not None:
                 break 
          return tags

     @abstractmethod
     def parse_html(self): 
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
          
          
