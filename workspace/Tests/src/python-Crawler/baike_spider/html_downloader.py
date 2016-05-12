# coding=gbk

import urllib2

class HtmlDownLoader(object):
    
    
    def downloader(self,urls):
        if urls is None:
            return None
        
        response = urllib2.urlopen(urls)
        if response.getcode() != 200:
            return None
        
        return response.read()
        
    
    



