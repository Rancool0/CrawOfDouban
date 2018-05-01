from bs4 import BeautifulSoup
import re

# div <strong class="ll rating_num" property="v:average">8.6</strong>
#<dd><a href="https://movie.douban.com/subject/1291843/?from=subject-page" class="">黑客帝国</a></dd>

class UrlParser():

    def get_moviename_and_score(self,page_url,download):
        #解析页面
        if page_url is None or download is None:
            print("can't parser")
            return
        data = {}
        new_urls=set()
        soup=BeautifulSoup(download,'html.parser',from_encoding='utf-8')
        moviename=soup.find('title')#得到电影名称
        score=soup.find('',class_="ll rating_num")#得到电影评分
        info= soup.find('div',id = 'info')#得到电影信息
        detail = soup.find('span', class_='all hidden')#得到电影简介
        if detail is None:
            detail = soup.find('span',property = "v:summary")
        links=soup.find_all('a',href=re.compile(r'https://movie.douban.com/subject/\d+/\?from=subject-page'))
        #得到新的url
        for link in links:
            new_link=link['href']
            new_urls.add(new_link)
        data['name']=moviename.get_text()
        data['score']=score.get_text()
        data['info']=info.get_text()
        data['detail']=detail.get_text().replace(' ','').replace('\n','').replace('　　','').replace('•',' ')
        return data,new_urls
