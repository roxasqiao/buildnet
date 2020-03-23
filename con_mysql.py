'''
Created on 2020年3月6日

@author: yanzi
'''
import pymysql
from datetime import datetime
def mysql_connection(zpro_group):
    conn=pymysql.connect("49.235.46.34","root","yanzi.3718406","spider_water")
    #使用cursor()方法创建一个游标对象cursor
    cursor=conn.cursor()
    sql='insert into spider_water.buildnet_prolist\
        (ZPROID,ZURL, ZPROJECT,ZDATE,ZNOTICE,ZPROTYPE,ZPROVINCE,\
        ZCITY,ZMONEY,ZZBORG,ZDLORG,ZZBMAN,ZZBPHONE,ZDLMAN,ZDLPHONE,ZTEXT,ZKEYWORD,ZGETTIME)\
        values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,CURRENT_TIMESTAMP())'
    #sql2='insert into spider.job_logs values (%s,%s,%s);'
    sql3='delete from spider_water.buildnet_prolist where ZPROID=%s'
    try:
        
        i=len(zpro_group)
        for num in range(i):
            co1=zpro_group[num].split(',')[0]
            co2=zpro_group[num].split(',')[1]
            co3=zpro_group[num].split(',')[2]
            co4=zpro_group[num].split(',')[3]
            co5=zpro_group[num].split(',')[4]
            co6=zpro_group[num].split(',')[5]
            co7=zpro_group[num].split(',')[6]
            co8=zpro_group[num].split(',')[7]
            co9=zpro_group[num].split(',')[8]
            co10=zpro_group[num].split(',')[9]
            co11=zpro_group[num].split(',')[10]
            co12=zpro_group[num].split(',')[11]
            co13=zpro_group[num].split(',')[12]
            co14=zpro_group[num].split(',')[13]
            co15=zpro_group[num].split(',')[14]
            co16=zpro_group[num].split(',')[15]
            co17=zpro_group[num].split(',')[16]
            par=co1,co2,co3,co4,co5,co6,co7,co8,co9,co10,co11,co12,co13,co14,co15,co16,co17
            par_d=co1
            cursor.execute(sql3,par_d)
            cursor.execute(sql,par)
            conn.commit()
        print( '----sql执行成功存贮数据量:'+str(i))
    except Exception as e:
        print("----sql异常-->"+str(e))
        conn.rollback()
        '''
        #错误日志
        par2=str(datetime.now()),'get_weather',str(e)
#         print(par2)
        cursor.execute(sql2,par2)
        conn.commit()
        '''
    finally:
            conn.close()   
