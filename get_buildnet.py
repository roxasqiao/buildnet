'''
Created on 2020年3月5日

@author: yanzi
'''
#使用requests方法
import requests
from bs4 import BeautifulSoup  
from config import logindata
from config import seachdata
import re 
import get_detail
import con_mysql

session = requests.Session()
def checkToken():
    #判断token是否过期
    status=session.get(logindata.url2, headers=logindata.header) # 检查会话
   # print(status.text)
    status_code=status.text[21:25]
    return status_code

#获取数据列表
def zroList(url):
    code=checkToken()
    if (code=='true'):
        #print('--->登录成功')
        pro_list=get_detail.getDetail(url)
        return pro_list
    else:
        print('--->token已过期')
        
#存贮数据
def saveData(pro_group):
    con_mysql.mysql_connection(pro_group)
    
def getDetalUrl():
    #查询总列表
    response = session.get(logindata.url4, headers=logindata.header,params=seachdata.params) # get传递参数
    response.encoding='utf-8'
    html=response.text
    soup=BeautifulSoup(html,'html.parser') #解析器Python标准库
    count=soup.find(name='label', attrs={'class': 'ml8 f-fr'})
    
    #1、查询总数据量
    num=int(count.string.replace('合计',''))
    pagenum=(num//25)+1
    print('--->总共查询到数据量：'+str(num)+'-->页数：'+str(pagenum))

    #2、获取详情页url
    for page in range(19,pagenum+1):
        print('抓取第'+str(page)+'页url')
        response2 = session.get(logindata.url4+str(page), headers=logindata.header,params=seachdata.params,timeout=20)# get传递参数
        html2=response2.text
        soup=BeautifulSoup(html2,'html.parser') #解析器Python标准库
        content=soup.find_all(name='td', attrs={'class': 'td-line'})
        url_group=[]
        for i in range(len(content)):
            pattern1='<a href=.*?target="_blank">'
            finaldata=re.findall(pattern1, str(content[i]))[0].split('<a href="')[1].split('" target="_blank">')[0]
            urllist='http://gc.buildnet.cn'+finaldata
            url_group.append(urllist)
    
        #3、解析数据
        print('解析第'+str(page)+'页url')
        pro_group=[]
        for url in url_group:
            pro_list=zroList(url)
            print(pro_list)
            pro_group.append(pro_list)
        
        #4、存贮数据
        print('存贮'+str(page)+'页数据')
        saveData(pro_group)
        
if __name__ == '__main__':
    code=checkToken()
    if (code=='true'):
        print('--->登录成功')
        getDetalUrl()
    else:
        print('--->token已过期')
    print('--->导入完成--- ') 
      

    



