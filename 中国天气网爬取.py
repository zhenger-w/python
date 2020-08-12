import requests
from bs4 import BeautifulSoup

def parse_page(url):
    headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }
    response=requests.get(url,headers=headers)
    text = response.content.decode("utf-8")
    soup=BeautifulSoup(text,'lxml')
    conMidtab=soup.find("div",class_="conMidtab")
    tables=conMidtab.find_all("table")
    for table in tables:
        trs=table.find_all("tr")[2:]
        for index,tr in enumerate(trs):
            tds=tr.find_all("td")
            city_td=tds[0]
            if index==0:
                city_td=tds[1]
            city=list(city_td.stripped_strings)[0]


            wea=tds[1]
            if index == 0:
                wea = tds[2]
            w2 = list(wea.stripped_strings)[0]

            max_temp= tds[3]
            if index==0:
                max_temp=tds[4]
            max_temp= list(max_temp.stripped_strings)[0]



            weather=tds[-4]
            w=list(weather.stripped_strings)[0]

            winds=tds[-3]
            wind=list(winds.stripped_strings)[0]


            temp_td=tds[-2]
            min_temp=list(temp_td.stripped_strings)[0]
            message={"城市":city,
                     "天气现象(白天)":w2,
                     "白天最高气温":max_temp+"度",
                     "天气现象(晚上)":w,
                     "风向风力":wind,
                     "晚上最低温度":min_temp+"度"}

            print(message)
def main():
    url = "http://www.weather.com.cn/textFC/xn.shtml"
    parse_page(url)
if __name__ == '__main__':
    main()
