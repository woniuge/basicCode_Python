import requests

def get_proxy():
    #proxy = str(requests.get("http://127.0.0.1:5010/get/").content).split(':')
    proxy = str(requests.get("http://47.90.127.102:5010/get/").content).split(':')
    ip = proxy[0]
    port = proxy[1]
    return ip, port

if __name__ == "__main__":
    ip,port=get_proxy()
    print(ip,port)
