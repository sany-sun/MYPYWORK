import requests
import re
import time
import xlwt
from bs4 import BeautifulSoup
from lxml import etree

# 获取网页函数
def gethtml(url):
    try:
        heades = \
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
                "cookie": '_zap=a9d11532-aed4-4d1f-a3bb-0f7316be5c0c; ISSW=1; d_c0="AGCXdCoKohKPTk15hqxXEDz3Boa4DQtYg9Y=|1612891946"; captcha_session_v2="2|1:0|10:1612891964|18:captcha_session_v2|28:YzBoY2VmNnYzanZqa3VydTNrbzA=|968ec00227fff82af4a459e9c54b863aac9161c47e375904a8de9897bca7a0de"; captcha_ticket_v2="2|1:0|10:1612891972|17:captcha_ticket_v2|244:eyJhcHBpZCI6IjIwMTIwMzEzMTQiLCJyZXQiOjAsInRpY2tldCI6InQwM01wU3dlR1REUWVhVm8yN2ZoRHROT3ktMFFybkVoMmdqSXBqS0hDOG1rdUF6V0htdGVncE9UeFJ4dFRUY1NrV3dZdHM3VDRJcXVYN2JqUlRqZXdhQU9LZXlScjB6QTBfdlhRaTNFNFgtYmxIaXRrMjBwcldBV2cqKiIsInJhbmRzdHIiOiJAUElhIn0=|61269e2e07d830557f81040e4a7cbdb37f96d1b4e407cd51afdb2ae6d1128c7d"; z_c0="2|1:0|10:1612891985|4:z_c0|92:Mi4xUFpSN0VBQUFBQUFBWUpkMEtncWlFaVlBQUFCZ0FsVk5VUlVRWVFETm5UWnBhaTZ3N0JLRWdWMklyR3oyajlSSFlB|605e5342b12254e82673c107bf21893c82adc13edce1a5f7add0864134dd1a2c"; _xsrf=e059aad5-69b5-4a28-8ff3-4f594abd4b25; SESSIONID=jeem6E03i7ceXuTM2RXgK3gWQbnjKt8hBNnN6B7CNhR; JOID=UF4cC0sTkAswwTQwZRnWGE3jNJR8ffpvVfV1D1d4o2dUkUNgJwZ2MVrHPz5sBj_pUHaBOlcLJ7r3cw6ftqPIQsU=; osd=VF0WAUwXkwE6xjAzbxPRHE7pPpN4fvBlUvF2BV1_p2Rem0RkJAx8Nl7ENTRrAjzjWnGFOV0BIL70eQSYsqDCSMI=; tst=h; tshl=; q_c1=b21c4b297bd44e908817999f221665e3|1614014655000|1614014655000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1614014493,1614015751,1614016031,1614016208; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1614016264; KLBRSID=d6f775bb0765885473b0cba3a5fa9c12|1614016875|1614014491'}
        r = requests.get(url, headers=heades)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print(r.status_code)

def b_hot_list():
    index = input("请输入你想要查询的榜单类型：1.全站，2.国产，3.国创相关，4.纪录片，5.动画，6.音乐，7.舞蹈，8.游戏，9.知识，10.科技，11.体育，12.汽车，13.生活，14.动物圈，15.鬼畜，16.时尚，17.娱乐，18.影视，19.电影，20电视剧，21.原创，22.新人:\n")
    h_list = ["all", "bangumi", "guochan", "guochuang", "documentary", "douga", "music", "dance", "game", "knowledge", "tech", "life", "food", "animal", "kichiku", "fashion", "ent", "cinephile", "movie", "tv", "origin", "rookie"]
    html = gethtml('https://www.bilibili.com/v/popular/rank/'+h_list[int(index)-1])
    soup = BeautifulSoup(html, "html.parser")
    tit_item = soup.find_all(class_='title', target='_blank')
    j = 1
    result = etree.HTML(html, etree.HTMLParser())
    sco_item = result.xpath('//div[@class="pts"]/div//text()')
    link_item = result.xpath('//div[@class="info"]/a[@class="title"]//@href')
    # all_in = {
    #     'title': tit_item,
    #     'score': result
    # }
    print("序号     " + "     标题     " + "               评分     ")
    for i in tit_item:
        i = str(i)
        find_title = re.compile('>(.*?)</a>')
        h = re.findall(find_title, i)
        print(str(j)+"   "+str(h)+"   "+str(sco_item[j-1])+"   "+"https://"+str(link_item[j-1])[2:])
        j = j+1

#知乎

def z_hot_list():
    index = input("请输入你要查询了的榜单类型：1.全站,2.科学,3.数码,4.体育,5.时尚,6.电影,7.校园,8.车车,9.国际,10.时事")
    h_list = ["", "?list=science", "?list=digital", "?list=sport", "?list=fashion", "?list=film", "?list=school", "?list=car", "?list=focus", "?list=depth"]
    html = gethtml("https://www.zhihu.com/hot"+h_list[int(index)-1])
    result = etree.HTML(html, etree.HTMLParser())
    tit_item = result.xpath('//h2[@class="HotItem-title"]//text()')
    link_item = result.xpath('//div[@class="HotItem-content"]/a/@href')
    j = 1
    print("序号        名称       链接")
    for item in tit_item:
        print(str(j)+" "+item+" "+link_item[j-1])
        j = j+1

def up_fans():
    def interception(html):
            hk = re.compile('"follower":(.*?)}}')
            fans_num = re.findall(hk, str(html))
            return fans_num[0]
    def query():
        uid = input("请输入您想查询的up主的uid：")
        link = "https://api.bilibili.com/x/relation/stat?vmid="+uid+"&jsonp=jsonp"
        m = 0
        while 1:
            i = interception(gethtml(link))
            i = int(i)
            if(m==0):
                print("程序启动中........")
            elif(i==m):
                pass
            elif(i>m):
                print("实时涨粉:", i-m)
                print("当前粉丝数:", i)
            else:
                print("实时掉粉:", m-i)
                print("当前粉丝数：", i)
            time.sleep(5)
            m = i
    query()


def switcher(s_index):
        if s_index == 1:
            up_fans()
        elif s_index == 2:
            b_hot_list()
        elif s_index == 3:
            z_hot_list()


def main():
    options = input("功能：1.B站up主实时粉丝数变化 2.b站排行榜 3.知乎排行榜：")
    print("\n")
    switcher(int(options))

if __name__ == '__main__':
    main()
