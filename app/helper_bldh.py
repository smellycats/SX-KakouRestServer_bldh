# -*- coding: utf-8 -*-
from urlparse import urlparse

KKDD = {
    '1000037': '441322101',
    '1000053': '441322102',
    '1000039': '441322103',
    '1000067': '441322104',
    '1000065': '441322105',
    '1000070': '441322106',
    '1000042': '441322107',
    '1000043': '441322108',
    '1000066': '441322109',
    '1000012': '441322110',
    '1000069': '441322111',
    '1000046': '441322112',
    '1000068': '441322113',
    '1000048': '441322114',
    '1000072': '441322115',
    '1000071': '441322116'
}

def hpzl2hpys(hpzl):
    if hpzl == 1:
        return (2, 'BU', u'蓝牌')
    if hpzl in set([2, 10]):
        return (1, 'YL', u'黄牌')
    if hpzl in set([3,4,5,6]):
        return (3, 'BK', u'黑牌')
    if hpzl in set([12,13]):
        return (0, 'WT', u'白牌')
    return (9, 'QT', u'其他')

def fxbh2code(fxbh):
    if fxbh in set([0,4]):
        return ('EW', u'由东往西')
    if fxbh in set([1,5]):
        return ('WE', u'由西往东')
    if fxbh in set([2,6]):
        return ('SN', u'由南往北')
    if fxbh in set([3,7]):
        return ('NS', u'由北往南')
    return ('QT', u'其他')


def create_kkddid(url_str):
    url = urlparse(url_str)
    return KKDD.get(url.path.split('/')[2][:7], '441322110')
    
if __name__ == '__main__':
    print hpzl2hpys(12)
    url_str = u'http://10.44.245.247:8081/d/1000043$1$0$3/20160521/15/4003-2717404-0.jpg?streamID:25372@capTime:1463816067'
    print create_kkddid(url_str)
