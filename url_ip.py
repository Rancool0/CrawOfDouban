from bs4 import BeautifulSoup
import re
from urllib import request

url = 'http://www.xicidaili.com/wn/'
#从这个网站去获取IP


# def download(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6', }
#     req = request.Request(url, headers=headers)
#     response = request.urlopen(req)
#     return response
#
# def get_new_ips():
#         new_ips=set()
#         soup=BeautifulSoup(download(url),'html.parser',from_encoding='utf-8')
#         ips=soup.find_all('td',text=re.compile(r'\d+\.\d+\.\d+\.\d+'))
#         ports=soup.find_all('td',text=re.compile(r'^\d{2,5}$'))
#         for i in range(0,len(ips)-1):
#             ip = str(ips[i].get_text())+':'+str(ports[i].get_text())
#             new_ips.add(ip)
#         return new_ips

def test_new_ips():
    #抓取一个新的可用的代理IP
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6', }
    req = request.Request(url, headers=headers)#抓取代理IP网站网页
    response_getip = request.urlopen(req)
    new_ips = set()
    soup = BeautifulSoup(response_getip, 'html.parser', from_encoding='utf-8')
    ips = soup.find_all('td', text=re.compile(r'\d+\.\d+\.\d+\.\d+'))#获取一页代理IP
    ports = soup.find_all('td', text=re.compile(r'^\d{2,5}$'))#获取端口
    for i in range(0, len(ips) - 1):
        ip = str(ips[i].get_text()) + ':' + str(ports[i].get_text())
        new_ips.add(ip)#拼装成一个完整的IP，加入集合中去
    root_url='https://movie.douban.com/subject/1652587/?from=subject-page'
    verified_ip = ''
    while new_ips:
        #验证拼装IP是否可用
        ip = new_ips.pop()
        try:
            proxy = {'https': ip}
            proxy_support = request.ProxyHandler(proxy)
            opener = request.build_opener(proxy_support)
            req = request.Request(root_url, headers=headers)
            request.install_opener(opener)
            response = request.urlopen(req,timeout=10)
            print(ip +'successful')
            verified_ip=ip#已证明这个IP可用，跳出循环
            break
        except:
            print(ip+'failed')
    del new_ips,ips,ports
    print(verified_ip)
    return verified_ip


