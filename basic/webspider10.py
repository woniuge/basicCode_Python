# -*- coding:UTF-8 -*-

from bs4 import BeautifulSoup
import requests
import random

pro = ['88.117.233.210:53281',
       '179.189.87.212:20183',
       '201.140.132.34:8080',
       '36.231.16.132:8080',
       '39.104.74.95:8080',
       '14.207.125.11:8080',
       '202.74.243.112:8080',
       '219.91.255.179:80',
       '95.47.4.54:8080',
       '185.173.15.2:8080',
       '103.59.212.93:8080',
       '186.215.198.179:20183',
       '122.114.31.177:808',
       '177.21.109.66:20183']
'''
def get_proxy():
	#proxy = str(requests.get("http://127.0.0.1:5010/get/").content).split(':')
    proxy = str(requests.get("http://47.90.127.102:5010/get/").content).split(':')
    ip = proxy[0]
    port = proxy[1]
    return ip, port
'''
# 类说明：下载《无问西东》的著名台词
class downloader(object):
    def __init__(self):
        #self.server = 'http://www.juzimi.com/'
        self.target = 'www.juzimi.com/article/无间道'
        #self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
        # self.headers = {'User-Agent':'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0'}
        self.urls = []  # 存放具体电影台词的页面链接
        self.nums = 0  # 页面数

    # 获取具体电影台词的页面链接
    def get_download_url(self,n):
        self.nums = n+1
        self.urls.append(self.target)
        for i in range(n):
            tail='?page='+str(i+1)
            self.urls.append(self.target + tail)
        print(self.urls)

    # 获取具体电影的经典台词,target--下载链接，texts--本页台词内容
    def get_contents(self, target):
        '''
        ip, port = get_proxy()
        proxie = {'http': 'http://' + str(ip).replace("b'", "") + ':' + str(port).replace("'", ""),
                  'https': 'https://' + str(ip).replace("b'", "") + ':' + str(port).replace("'", "")}
        print(proxie)
        '''
        try:
            '''
            ip, port = get_proxy()
            proxie = {'http': 'http://' + str(ip).replace("b'", "") + ':' + str(port).replace("'", ""),
                      'https': 'https://' + str(ip).replace("b'", "") + ':' + str(port).replace("'", "")}
            print(2)
            print(proxie)
            '''
            proxie = {'http': 'http://' + random.choice(pro),
                      'https': 'https://' + random.choice(pro)}
            #req = requests.get(url=target,proxies=proxie,headers=self.headers)
            req = requests.get(url=target, headers=self.headers,timeout=500)
            print(req.status_code)
            req.encoding='utf-8'

            html = req.text
            bf = BeautifulSoup(html, "html.parser")

            text = bf.find_all('a', class_='xlistju')
            timu = bf.find_all('a', class_='active')
            # print(text)

            texts = text[0].text + '\t' + '《' + timu[0].text + '》'
            # 不足十条
            # texts = ''

            for i in range(9):
                texts = texts + '\n\n' + text[i + 1].text + '\t' + '《' + timu[0].text + '》'
            # print(texts)
            return texts
        except requests.ConnectionError:
            print("connection error")

    # 将爬取的文章内容写入文件，path--当前路径下，台词保存名称，text--台词内容
    def write(self, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.writelines(text)
            f.write('\n\n')


if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url(5)
    # print(dl.nums)
    for i in range(dl.nums):
        # print(dl.urls[i])
        dl.write('台词2.txt', dl.get_contents(dl.urls[i]))

'''
#对于具体的某部电影获取页面链接
from bs4 import BeautifulSoup
import requests

server = 'http://www.juzimi.com/'
target = 'http://www.juzimi.com/article/664263'
htmlfile=open('juzimi.html','rb')
htmlpage=htmlfile.read()
#print(htmlpage)
bf = BeautifulSoup(htmlpage, "html.parser")
#print(bf.title.text)
li_first = bf.find_all('li',class_='pager-item') #前几页
li_last=bf.find_all('li',class_='pager-last') #最后一页
li= [*li_first,*li_last]
#print(li)
a_li = BeautifulSoup(str(li), "html.parser")
a= a_li.find_all('a')
urls= []
urls.append(target)
for each in a:
    urls.append(server + each.get('href'))
print(urls)
'''

'''
#读取本地html文件并抽取需要的台词
from bs4 import BeautifulSoup
from urllib import request
import requests

htmlfile=open('juzimi.html','rb')
htmlpage=htmlfile.read()
#print(htmlpage)
bf = BeautifulSoup(htmlpage, "html.parser")
#print(bf.title.text)
text = bf.find_all('a',class_='xlistju')
#print(text)
texts = text[0].text
for i in range(9):
    texts = texts + '\n\n' + text[i+1].text
print(texts)

#for i in range(10):
#    texts=texts.append(text[i].text)
#print(texts)
#print(i+1,texts[i].text)
'''
'''
with open('taici.txt','w') as f:
    f.writelines(bf.title.text)
    for i in range(10):
        print(i, texts[i].text)
        f.writelines('\n\n')
        f.writelines(texts[i].text)
'''

'''
from bs4 import BeautifulSoup
from urllib import request
import requests

px = request.ProxyHandler({'http':'117.127.0.209:8080'})
opener=request.build_opener(px)
requ=request.Request('http://www.juzimi.com/ju/4286465')
res=opener.open(requ)
request.install_opener(opener)
with open('juzimi.html','wb') as f:
    f.write(res.read())
'''

'''
if __name__ == "__main__":
    target = 'http://www.juzimi.com/article/664263'
    headers = {'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, sdch, br',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               }
    req = requests.get(url=target, headers=headers)
#    req = requests.get(url=target, headers={'User-Agent': "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt)"})
    html = req.text
    bf = BeautifulSoup(html, "html.parser")
    texts = bf.find_all('div', class_='views-field-phpcode-1')
    print(req)
'''

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
