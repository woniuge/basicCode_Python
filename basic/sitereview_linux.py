from argparse import ArgumentParser
from bs4 import BeautifulSoup
import json
import requests
import sys
import time

def get_proxy():
	#proxy = str(requests.get("http://127.0.0.1:5010/get/").content).split(':')
        proxy = str(requests.get("http://47.90.127.102:5010/get/").content).split(':')
	ip = proxy[0]
	port = proxy[1]
	return ip, port

class SiteReview(object):
	def __init__(self):
		self.baseurl = "https://sitereview.bluecoat.com/resource/lookup"
		self.headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}

	def sitereview(self, url, ip, port):
		payload = {"url": url, "captcha":""}
		proxie = {'http' : 'http://' + str(ip).replace("b'","") + ':' + str(port).replace("'",""),
					'https' : 'https://' + str(ip).replace("b'","") + ':' + str(port).replace("'","")} 
		print(proxie)
		try:
			self.req = requests.post(
				self.baseurl,
				headers=self.headers,
				data=json.dumps(payload),
				# data=payload,
				proxies = proxie,
				timeout = 20,
			)
			return json.loads(self.req.content.decode("UTF-8"))
		except requests.ConnectionError:
			# sys.exit("[-] ConnectionError: " \
			#		  "A connection error occurred")
			print("connection error")
			return False
		except requests.exceptions.Timeout:
			print("time out")
			return False

		

	def check_response(self, response):
		if self.req.status_code != 200:
			# sys.exit("[-] HTTP {} returned".format(req.status_code))
			print(self.req.status_code)
			return False
		else:
			self.category = response["categorization"][0]["name"]
			self.date = response["translatedRateDates"][0]["text"][0:35]
			self.url = response["url"]



def main(url,outpath,ip,port):
	s = SiteReview()
	uurl = 'www.' + url
	response = s.sitereview(uurl,ip,port)
	if (response == False):
		return False
	status = ' '.join(response.keys())
	# print(status)
	
	if ("error" in status or "CAPTCHA" in status):
		print("proxy ip banned")
		return False
	else:
		s.check_response(response)
	border = "=" * (len("Symantec Site Review") + 2)

	print("\n{0}\n{1}\n{0}\n".format(border, "Symantec Site Review"))
	print("URL: {}\n{}\nCategory: {}\n".format(
		s.url,
		s.date,
		s.category
		)
	)
	data = url.replace("http://","").replace("/","") + "\001" + s.category + '\n'
	o = open(outpath,"a",encoding='UTF-8')
	o.write(data)
	o.close()
	return True

if __name__ == "__main__":
	url_path = sys.argv[1]
	# url_path = "/home/ruc/siteview/input/xaa"
	out_path = "/root/spider/sitereview/SiteReview_data.txt"
	while True:
		f = open(url_path,'r',encoding = 'UTF-8')
		urls = f.readlines()
		f.close()
		url_dict = {}
		i = 0
		for each in urls:
			url_dict[each.strip()] = i
			i += 1
		print("raw url number...  " + str(len(url_dict)))
		g = open(out_path,'r',encoding = 'UTF-8')
		done_list = g.readlines()
		for every in done_list:
			ym = every.split("\001")[0]
			# print(ym)
			if ym in url_dict:
				url_dict.pop(ym)
		print("need to claw...  " + str(len(url_dict)))
		urls = sorted(url_dict.items(),key = lambda x:x[1],reverse = False)
		submitUrls = []
		for each in urls:
			submitUrls.append(each[0])
		# print(submitUrls)
		for each in submitUrls:
			ip, port = get_proxy()
			# print(ip,port)
			# time.sleep(3)
			# url = 'www.' + each
			check = main(each,out_path, ip, port)
			if(check == False):
				break
