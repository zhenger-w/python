import requests
from lxml import etree
HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
     }
def get_url(url):
        response = requests.get(url, headers=HEADERS)
        text = response.text
        text = etree.HTML(text)
        title = text.xpath("//*[@id='readerFt']/div/div[2]/div[2]/text()")[0]
        contents = text.xpath("//div[@class='content']//p/text()")
        contents.insert(0, title)
        for i in contents:
                with open("剑仙在此.txt", "a+")as b:
                        b.write(str(i) + "\n")
def all_urls():
        url="http://book.zongheng.com/showchapter/907701.html"
        response=requests.get(url,headers=HEADERS)
        text=response.text
        html=etree.HTML(text)
        num=0
        zhengers=html.xpath("//ul[@class='chapter-list clearfix']//li")[0]
        for i in zhengers:
                wz=i.xpath("//li[@class=' col-4']//a//@href")
                for ze in wz:
                        num+=1
                        print("正在爬取第{}章".format(num))
                        get_url(ze)

if __name__ == '__main__':
        all_urls()

