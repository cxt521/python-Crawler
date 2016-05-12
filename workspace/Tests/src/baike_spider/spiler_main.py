# coding=gbk

from baike_spider import html_downloader, url_manager, html_outputer,\
    html_parser

class Spliermain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.parser=html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    def craw(self, root_url):
        count = 1
        self.urls.add_new_urls(root_url)
        
        while self.urls.have_urls():
            try:
                new_urls=self.urls.get_new_urls()
                print'craw %d:%s'%(count,new_urls)
                html_count = self.downloader.downloader(new_urls)
                new_url , new_data = self.parser.parse(new_urls,html_count)
                self.urls.add_new_url(new_url)
                self.outputer.collect_data(new_data)
                
                if  count==100 :
                    
                    break
                    
                count = count+1
            except:
                print 'craw failed'
        self.outputer.output_html()
    
if __name__=="__main__":
    root_url ="http://baike.baidu.com/view/1219.htm"
    obj_splier = Spliermain()
    obj_splier.craw(root_url)
    