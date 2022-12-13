from lxml import etree
import os

import requests

fileName = r'D:\new_test\E10自动化\接口自动化测试\test_data\account.txt'
content_txt = """自动化团队管理员,147726153626476,a123456,管理员,Awbvgt内部自动化团队
普通成员,ni1668135531390@eteams.cn,796461,普通成员,1
普通成员,tc1668135537440@eteams.cn,560020,普通成员2,2
其他团队管理员,153849628969717,a123456,管理员,Rincla内部自动化团队
登录限制用户,ox1668135559306@eteams.cn,699774,普通成员1,2
切换团队用户,bk1668135565108@eteams.cn,579841,普通成员2,2
普通用户三,rp1668135570802@eteams.cn,991127,普通成员2,2
普通用户四,lg1668135576721@eteams.cn,811625,普通成员2,2
"""

with open(fileName, 'w', encoding='utf8')as file:
    file.write(content_txt)

fileName = r'D:\new_test\E10自动化\接口自动化测试\conf.ini'
content_txt = """[url]
baseurl = weapp.yunteams.cn
"""
with open(fileName, 'w', encoding='utf8')as file:
    file.write(content_txt)