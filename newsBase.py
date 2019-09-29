# -*- coding: UTF-8 -*-

import spider
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
     """
      
     def  __init__(self):
          self.university = ""
          self.school = ""
          self.title = ""
          self.date = ""
     
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
   The abstract base class used to parse news from every university.
     """
      def __init__(self, url=""):
          self.url = url
          self.soup = Spider(url).soup() #convert html to BeautifulSoup object
          self.newsList = []
      
      @abstractmethod
      def parse_html(self): 
          raise RuntimeError,  ' "parse_html". method must be overwrite in subclass'
      
      def get_today_news(self):
         '''
        we will make a timed task used this function
         '''
          now_time = datetime.datetime.now()
          today_news = []
          for news in self.newsList:
               time_delta = now_time - today_news
               if time_delta.days < 1:
                  today_news.append(news)
          return today_news
          
          
