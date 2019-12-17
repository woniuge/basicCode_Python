# encoding:utf-8
'''
import requests

def get_proxy():
    #proxy = str(requests.get("http://127.0.0.1:5010/get/").content).split(':')
    proxy = str(requests.get("http://47.90.127.102:5010/get/").content).split(':')
    print(proxy)
    ip = proxy[0]
    port = proxy[1]
    return ip, port

if __name__ == "__main__":
    ip,port=get_proxy()
    print(ip,port)
    proxie = {'http': 'http://' + str(ip).replace("b'", "") + ':' + str(port).replace("'", ""),
              'https': 'https://' + str(ip).replace("b'", "") + ':' + str(port).replace("'", "")}
    print(proxie)
'''

'''
import requests
import random


#pro = ['1.119.129.2:8080','115.174.66.148','113.200.214.164']

def get_proxy():
    #proxy = str(requests.get("http://127.0.0.1:5010/get/").content).split(':')
    proxy = str(requests.get("http://47.90.127.102:5010/get/").content).split(':')
    print(proxy)
    ip = proxy[0]
    port = proxy[1]
    return ip, port

#  你的网页请求头信息
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
url = 'http://www.whatismyip.com/'  # 你用于测试自己ip的网站

ip,port=get_proxy()
proxie = {'http': 'http://' + str(ip).replace("b'", "") + ':' + str(port).replace("'", ""),
          'https': 'https://' + str(ip).replace("b'", "") + ':' + str(port).replace("'", "")}
request = requests.get(url, proxies=proxie, headers=head)  # 让问这个网页  随机生成一个ip
request.encoding = request.apparent_encoding  # 设置编码 encoding 返回的是请求头编码  apparent_encoding 是从内容网页中分析出的响应内容编码方式
print(request.text)  # 输出返回的内容
'''
import requests
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
#proxies = { "http": "http://10.10.1.10:3128", "https": "http://10.10.1.10:1080"}
#requests.get("http://ip.china.com", proxies=proxies,headers = head)

proxies = { "http": "http://10.10.1.10:3128"}
res =requests.get('http://icanhazip.com/', proxies=proxies)
print(res.content)