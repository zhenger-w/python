import requests
from lxml import etree
def newest():
    douban_url = "https://movie.douban.com/cinema/nowplaying/deyang/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
        "Referer": "https://movie.douban.com/cinema/nowplaying/deyang/"
    }
    response = requests.get(url=douban_url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    ul = html.xpath("//ul[@class='lists']")[0]
    # print(etree.tostring(ul,encoding="utf-8").decode("utf-8"))
    lis = ul.xpath("./li")
    movies = []
    for li in lis:
        title = li.xpath("@data-title")[0]
        score = li.xpath("@data-score")[0]
        star  = li.xpath("@data-star")[0]
        release=li.xpath("@data-release")[0]
        duration=li.xpath("@data-duration")[0]
        region=li.xpath("@data-region")[0]
        director=li.xpath("@data-director")[0]
        actors = li.xpath("@data-actors")[0]
        hb = li.xpath(".//img/@src")[0]
        movie = {
            "title": title,
            "score": score,
            "hb": hb,
            "star":star,
            "release":release,
            "duration":duration,
            "region":region,
            "director":director,
            "actors":actors





        }
        movies.append(movie)
    for i in movies:
        print(i)
def Coming_soon():
    douban_url = "https://movie.douban.com/cinema/nowplaying/deyang/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
        "Referer": "https://movie.douban.com/cinema/nowplaying/deyang/"
    }
    response = requests.get(url=douban_url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    ul = html.xpath("//ul[@class='lists']")[1]
    # print(etree.tostring(ul,encoding="utf-8").decode("utf-8"))
    lis = ul.xpath("./li")
    movies = []
    for li in lis:
        title = li.xpath("@data-title")[0]
        duration = li.xpath("@data-duration")[0]
        region = li.xpath("@data-region")[0]
        director = li.xpath("@data-director")[0]
        actors = li.xpath("@data-actors")[0]
        hb = li.xpath(".//img/@src")[0]
        movie = {
            "title": title,
            "hb": hb,

            "duration": duration,
            "region": region,
            "director": director,
            "actors": actors

        }
        movies.append(movie)
    for i in movies:
        print(i)

if __name__ == '__main__':
    newest()#正在上映 的电影
    print("------------------------------------------------------------------")
    Coming_soon()#即将上映的电影




