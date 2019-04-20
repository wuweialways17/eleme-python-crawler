    # coding=utf-8 
    import re  
    from bs4 import BeautifulSoup  
    import json  
    import threading  
    from requests import Session  
    class dazp_bj:  
        def __init__(self,category):  
            self.baseUrl='https://www.ele.me/place/wtsw0tdny0wh?latitude=32.023562&longitude=118.85311'  
            self.bgurl=category[0]  
            self.typename=category[1]  
            self.page=1  
            self.pagenum=10 #设置最大页面数目
            self.headers={  
                "Host":"https://www.ele.me/place/wtsw0tdny0wh?latitude=32.023562&longitude=118.85311",  
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/59.0",  
                "Referer":"https://www.ele.me/place/wtsw0tdny0wh?latitude=32.023562&longitude=118.85311",  
            }  
        def start(self):        
            self.s=Session()    #定义一个Session()对象  
            print self.bgurl,self.typename  
            print "please wait for 15"  
            dazp_bj.__parseHtml(self,self.bgurl) #调用__parseHtml函数  
            print 'getdata down'  
        def __parseHtml(self,preurl):  
            _json=dict()    #定义一个字典用以存储数  
            html=self.s.post(preurl,headers=self.headers).text  #发送请求，获取html  
            soup=BeautifulSoup(html,'lxml') #进行解析  
                    name=['商家名称','配送费'，'配送时间']  
            for li in soup.find('div',class_="place-rstbox clearfix").find('div',id="shop-all-list").ul.find_all('li'):  
                info=li.find('div',class_='txt')  
                _json[name[0]]=info.find(into.find('div',class_='<div class="rstblock-content">').find('a',class_="rstblock-title")a.h4.get_text().encode('utf-8')                      
                _json[name[1]]=int(info.find('div',class_='rstblock-content').find('a',class_="rstblock-cost").b.get_text().encode('utf-8'))  
                _json[name[2]]=int(re.sub('￥','',info.find('div',class_='rstblock-logo').find('a',class_="span").b.get_text().encode('utf-8')))  
                with open(self.typename+'.json','a') as outfile:  
                    json.dump(_json,outfile,ensure_ascii=False)  
                with open(self.typename+'.json','a') as outfile:  
                    outfile.write(',\n')
                #针对某些网站的反爬虫措施，可以通过人为降低访问频率的方式避免
               import time  
               import random  
               time.sleep(random.uniform(1,4))#表示设置一个随机数作为停顿时间，为１～４之间的一个数
                          
            self.page+=1  
            if self.page<=self.pagenum:  
                self.nexturl=self.baseUrl+soup.find('div',class_='page').find('a',class_='next')['href']  #获得下一页的链接  
                dazp_bj.__parseHtml(self,self.nexturl)        
