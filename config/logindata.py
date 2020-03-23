'''
Created on 2020年3月5日

@author: yanzi
'''

pwd={'txtUserName': 'ryjy',
            'txtUserPassword': '8458037dyq',
            'isLoginAnyway': '1'
    }
   
url='http://gc.buildnet.cn/project/index'#首页搜索
url2='http://gc.buildnet.cn/CheckSession'#检查cookie是否过期
url3='http://gc.buildnet.cn/Exp/PreviewExcel' # excel导出
url4='http://gc.buildnet.cn/Notice/SearchBIDList/' #项目搜索

'''
exceldata={'Ref_Id': '270244635|1|2020/3/5 17:10:06|964378262',
           'WordStyle': '',
           'DownFiled': '',
           'UserId': '387083',
           'miuecolor': 'p1'}
'''


zcookie='UM_distinctid=170a97740b59d-016968ea979523-3c604504-100200-170a97740b6225; ASP.NET_SessionId=rhkefumfozv3tsx05fabxl1k; Hm_lvt_cf1b280f712422bacef6f4e10a5da5e8=1583488514,1583489743,1583489750,1583493104; Hm_lpvt_cf1b280f712422bacef6f4e10a5da5e8=1583493397'







header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
            'Connection': 'keep-alive',
            'Content-Type': 'text/html; charset=gb2312', #传递参数方式
            "Cookie": zcookie}

#proxies
proxies={'https':'//117.88.5.140:3000',
         'https':'//218.249.45.162:35586',
         'https':'//113.12.202.50:40498'}
