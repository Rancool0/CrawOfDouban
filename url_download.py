from urllib import request



class UrlDownload():
    def download(self,page_url,ip):
        #下载url页面
        if page_url is None:
            print('page_url is None')
            return
        proxy = {'https':ip}#这是代理IP
        proxy_support = request.ProxyHandler(proxy)#创建ProxyHandler
        opener = request.build_opener(proxy_support)#创建opener
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6', }
        req = request.Request(page_url, headers=headers)#装载url和header
        request.install_opener(opener)#安装opener
        response = request.urlopen(req,timeout=10)#抓取url,响应时间上限为10
        return response

# def func():
#     url = 'http://www.whatismyip.com.tw/'
#     # 这是代理IP
#     proxy = {'http': '60.177.227.34:18118'}
#     # 创建ProxyHandler
#     proxy_support = request.ProxyHandler(proxy)
#     # 创建Opener
#     opener = request.build_opener(proxy_support)
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',}
#     req = request.Request(url, headers=headers)
#     # 安装Opener
#     request.install_opener(opener)
#     # 使用自己安装好的Opener
#     response = request.urlopen(req)
#     # 读取相应信息并解码
#     html = response.read().decode("utf-8")
#     # 打印信息
#     print(html)
