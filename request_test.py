# -*- coding: utf-8 -*-
import time
import datetime
import json

import arrow
import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

from kakou import Kakou
from union_kakou import UnionKakou

class UnionKakouTest(object):
    def __init__(self):
        self.ini = {
            'host': '127.0.0.1',
            'port': 5000
        }
        self.uk = UnionKakou(**self.ini)
    
    def test_kakou_post(self):
        """上传卡口数据"""
        data = [
            {
                'jgsj': arrow.now().format('YYYY-MM-DD HH:mm:ss'),
                'hphm': '粤L70939',
                'kkdd_id': '441302004',
                'hpys_id': '0',
                'fxbh': 'IN',
                'cdbh':4,
                'img_path': 'http:///img/123.jpg'
            },
            {
                'jgsj': arrow.now().format('YYYY-MM-DD HH:mm:ss'),
                'hphm': '粤L12345',
                'kkdd_id': '441302004',
                'hpys_id': '0',
                'fxbh': 'IN',
                'cdbh': 4,
                'img_path': 'http:///img/123.jpg',
                'cllx': 'K41'
            }
        ]

        r = self.uk.post_kakou(data)
        assert isinstance(r, dict) == True
        #assert r['headers'] == 201


class KakouTest(object):
    def __init__(self):
        self.ini = {
            'host': '127.0.0.1',
            'port': 80,
            'city': 'hcq'
        }
        self.kk = Kakou(**self.ini)

    def __del__(self):
        pass

    def test_get_cltxs(self):
        """根据ID范围获取卡口信息"""
        r = self.kk.get_cltxs(123, 125)

        assert 'total_count' in r
        
    def test_get_maxid(self):
        """获取最大ID"""
        r = self.kk.get_maxid()

        assert 'maxid' in r

if __name__ == '__main__':  # pragma nocover
    kt = UnionKakouTest()
    kt.test_kakou_post()

