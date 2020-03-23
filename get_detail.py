'''
Created on 2020年3月5日

@author: yanzi
'''
import get_buildnet
from config.logindata import header
from config import logindata
from config import seachdata
from bs4 import BeautifulSoup
import re
def getDetail(url):
    zproid=url[45:]
    rsponse=get_buildnet.session.get(url,headers=logindata.header,proxies=logindata.proxies,timeout=20)
    html=rsponse.text
    soup=BeautifulSoup(html,'html.parser') #解析器Python标准库
    
    ztitle=soup.title.string.strip()
    zdate=soup.find_all(name='td', attrs={'id': 'Td6'})[0].string.strip()[0:10]
    znotice=soup.find_all(name='td', attrs={'id': 'param_10004_2'})[0].string.strip()
    if soup.find_all(name='td', attrs={'id': 'param_10005_2'}):
         zproject=soup.find_all(name='td', attrs={'id': 'param_10005_2'})[0].string.strip()
    else:
        zproject=''
    zbarea=soup.find_all(name='td', attrs={'id': 'param_10002_2'})[0].string.strip()
    
    if len(soup.find_all(name='td', attrs={'id': 'param_10005_2'}))<=1:
        zsarea=''
    else:
        zsarea=soup.find_all(name='td', attrs={'id': 'param_10005_2'})[1].string.strip()
    #预算
    plist=['\d+\.?\d*万元','\d+\.?\d*元']
    if re.findall(plist[0], str(soup)):
        zmoney=re.findall(plist[0], str(soup))[0]
    elif re.findall(plist[1], str(soup)):
        zmoney=re.findall(plist[1], str(soup))[0]
    else:
        zmoney=''
    #招标单位；代理单位
    table=soup.find_all(name='div', attrs={'class': 'line_b'}) #页面分为三部分table
    if len(soup.find_all(name='div', attrs={'class': 'line_b'}))>2:
        table=soup.find_all(name='div', attrs={'class': 'line_b'})
        zborgTable=table[1] #第二个table是招标单位信息
        dlorgTable=table[2] #第三个table是代理单位信息
        if zborgTable.find_all(name='table'):
            zb_org=zborgTable.find_all(name='table')[1].find_all(name='td')[1].string.strip()
        else:
            zb_org=''
        if dlorgTable.find_all(name='table'):
            dl_org=dlorgTable.find_all(name='table')[1].find_all(name='td')[1].string.strip()
        else:
            dl_org=''
    else:
        zb_org=''
        dl_org=''
    
    zzzbman=''
    zzbphone=''
    zdlman=''
    adlphone=''
    ztext=''
    zkeyword=';'.join(seachdata.params['key'])
    zpro_list=zproid+','+url+' '+','+ztitle+','+zdate+','+znotice+','+\
              zproject+','+zbarea+','+zsarea+','+zmoney+','+zb_org+','+\
              dl_org+','+zzzbman+','+zzbphone+','+zdlman+','+adlphone+','+ztext+','+zkeyword
    return zpro_list
    '''
    content2=soup.find(name='div ', attrs={'class': 'content'})
    text=content2.text
    begin=text.find('==========以下为招标信息正文开始==========')+1
    end=text.find('==========以下为招标信息正文结束==========')+31
    realtext=text[begin:end]
    print(text)
    print(text[begin:end])
    '''




