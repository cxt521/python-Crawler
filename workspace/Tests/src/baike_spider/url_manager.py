# coding=gbk 

class UrlManager(object):
    def __init__(self):
        self.new_urls =set()
        self.old_urls = set()        
                   
    def add_new_urls(self,urls):
        if urls is None:
            return
        if urls not in self.new_urls and urls not in self.old_urls:
            self.new_urls.add(urls)
    
    def have_urls(self):
        return len(self.new_urls) !=0

    
    def get_new_urls(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url 

    
    def add_new_url(self,url):
        if url is None and len(url)==0:
            return
        for urls in url:
            self.add_new_urls(urls)