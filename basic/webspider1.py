# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
     target = 'http://www.juzimi.com/article/664263'
     req = requests.get(url = target,headers={'User-Agent':"your agent string"})
     html = req.text
     bf = BeautifulSoup(html,"html.parser")
     texts = bf.find_all('div', class_ = 'views-field-phpcode-1')
     print(texts[0])











'''
# _*_ coding:UTF-8 _*_
import requests

if __name__ == '__main__':
    target = 'http://www.juzimi.com/article/664263'
    req = requests.get(url=target,headers={'User-Agent':"your agent string"})
    print(req.text)
'''






















'''
# _*_ coding:UTF-8 _*_

import requests,sys
from bs4 import BeautifulSoup

class downloader(object):
    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/1_1094/'
        self.names = []     #存放章节名
        self.urls = []      #存放章节链接
        self.nums = 0       #章节数

    def get_download_url(self):
        req = requests.get(url = self.target)
        html = req.text
        div_bf = BeautifulSoup(html,"html.parser")
        div = div_bf.find_all('div',class_ = 'listmain')
        a_bf = BeautifulSoup(str(div[0]))
        a = a_bf.find_all('a')
        self.nums = len(a[15:])     #剔除不必要的章节，并统计章节数
        for each in a[15:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    def get_contents(self,target):
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html,"html.parser")
        texts = bf.find_all('div',class_ = 'showtxt')
        texts = texts[0].text.replace('\xa0'*8,'\n\n')
        return texts

    def writer(self,name,path,text):
        write_flag = True
        with open(path,'a',encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')
            
if __name__ == "__main__":               
    d1 = downloader()
    d1.get_download_url()
    print('经典台词开始下载:')
    for i in range(d1.nums):
        d1.writer(d1.names[i],'一念永恒.txt',d1.get_contents(d1.urls[i]))
        sys.stdout.write("  已下载：%.3f%%" % float(i/d1.nums) + '\r')
        sys.stdout.flush()
    print('《一年永恒》下载完成')
'''
        
'''    
    if __name__ == '__main__':
        server = 'http://www.biqukan.com/'
        target = 'http://www.biqukan.com/1_1094/'
        req = requests.get(url=target)
        html = req.text
        div_bf = BeautifulSoup(html,"html.parser")
        div = div_bf.find_all('div',class_ ='listmain')
        a_bf = BeautifulSoup(str(div[0]),"html.parser")
        a = a_bf.find_all('a')
        for each in a:
            print(each.string,server + each.get('href'))
'''
