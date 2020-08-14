import requests
import re
def get_url(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }
    response = requests.get(url, headers)
    text = response.text
    content=re.findall(r'<div\sclass="content">.*?<span>(.*?)</span>',text,re.DOTALL)
    contents=[]
    for c in content:
        x=re.sub("<.*?>"," ",c)
        contents.append(x.strip())
    for i in contents:
        print(i)
        print("-"*40)
def main():
    urls=[]
    for i in range(1,14):
        url="https://www.qiushibaike.com/text/page/{}/".format(i)
        urls.append(url)
    num=0
    for url in urls:
        num+=1
        print("第{}页内容".format(num))
        get_url(url)
if __name__ == '__main__':
    main()
