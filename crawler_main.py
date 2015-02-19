"""
crawler study code 

Author: smilexie1113@gmail.com

"""

import urllib.request
import os
import re
from collections import deque
from asyncio.queues import Queue

if __name__ == "__main__":
    start_url = "http://news.dbanotes.net/"
    
    to_be_visited = deque()
    visited = set()
    
    cnt = 0
    to_be_visited.append(start_url)
    
    while to_be_visited:
        url = to_be_visited.popleft()        
        
        print(str(cnt) + "page(s) has been grabbed." + "URL " + "\"" + url + "\"" + " is being grabbed.")
        
        try:
            urlfd =  urllib.request.urlopen(url)
        except Exception as ex:
            print( "URL " + "\"" + url + "\"" + "crawling failed. " + str(ex))
            continue
            
        if "html" not in urlfd.getheader("Content-Type"):
            continue
        
        try:
            html_str = urlfd.read().decode("utf-8")
        except:
            continue
        
        cnt += 1
        visited |= {url}
        
        #todo: parse the html_str
        
        link_pattern = re.compile('href=\"(.+?)\"') #links' regular expression       
        for tmp_url in link_pattern.findall(html_str):
            if "http" in tmp_url and tmp_url not in visited:
                to_be_visited.append(tmp_url)
        

