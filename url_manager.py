

class UrlManager():
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self,url):
        #添加一个新url
        if url is not None and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        #添加一组新url
        for url in urls:
            if url is not None and url not in self.old_urls:
                self.new_urls.add(url)

    def get_url(self):
        #取出一个待抓取的url
        if self.new_urls is None:
            print('No urls')
            return
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
