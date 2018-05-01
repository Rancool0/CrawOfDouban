#coding=utf-8

import url_manager,url_data,url_download,url_parser,time,url_ip

class UrlMain():
    def __init__(self):
        #初始化对象
        self.urlmanager = url_manager.UrlManager()
        self.urldownload = url_download.UrlDownload()
        self.urlparser = url_parser.UrlParser()
        self.urldata = url_data.UrlData()

    def craw(self,root_url):
        count=0#计数器
        ip=url_ip.test_new_ips()
        #获取一个可用的代理IP
        self.urlmanager.add_new_url(root_url)
        #添加第一个要抓取的页面
        while True:
            try:
                page_url=self.urlmanager.get_url()#拿到一个新的待抓取的url
                if page_url is None:
                    break
                download=self.urldownload.download(page_url,ip)#下载页面
                data,new_urls=self.urlparser.get_moviename_and_score(page_url,download)#解析，并拿到返回值
                self.urlmanager.add_new_urls(new_urls)#添加新的url去待抓取的url集合中去
                file_obj = open('douban_spider.json', 'a+')
                self.urldata.wiret_data(file_obj,data,page_url)#写文件
                file_obj.close()
                count += 1
                time.sleep(0.1)
                if count > 60000:
                    break
                if count % 10 == 1:
                    start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    print(count, start_time)#打印已抓取的数量和时间
            except Exception as e:
                print(e)
                del ip
                ip = url_ip.test_new_ips()#Ip被封后，换一个新IP
                print(ip)

if __name__=='__main__':
    root_url='https://movie.douban.com/subject/1652587/?from=subject-page'
    url_obj=UrlMain()
    url_obj.craw(root_url)
