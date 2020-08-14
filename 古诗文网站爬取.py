import requests
import re
def parse_url(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }
    response = requests.get(url,headers)
    text= response.text
    titles=re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,re.DOTALL)
    dynasty=re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    authors=re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    content_tage=re.findall(r'<div class="contson".*?>(.*?)</div>',text,re.DOTALL)
    contents=[]
    poems=[]
    for content in content_tage:
        x=re.sub("<.*?>"," ",content)
        contents.append(x.strip())

    for value in zip(titles,dynasty,authors,contents):
        title,dynasty,author,content=value
        poem={
            "title":title,
            "dynasty":dynasty,
            "author":author,
            "content":content
        }
        poems.append(poem)
    for p in poems:
        print(p)
        print("-"*40)
def main():
    urls=[]
    num=0
    for i in range(1,11):
        url="https://www.gushiwen.cn/default_{}.aspx".format(i)
        urls.append(url)
    for url in urls:
        num+=1
        print("第{}页资料".format(num))
        parse_url(url)
if __name__ == '__main__':
    main()
