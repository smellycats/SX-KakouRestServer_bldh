# -*- coding: utf-8 -*-
import json

import requests


class DHKakou(object):

    def __init__(self, **kwargs):
        self.host = kwargs['host']
        self.port = kwargs['port']
        #self.city = kwargs['city']
        self.headers = {
            'authorization': 'HZSX',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.status = False

    def get_picrecord_by_id(self, this_id, timeout=5):
        url = '''http://{0}:{1}/dahuaIS/rest/picrecord/search?q={{"startId":{2},"endId":{3},"page":{{"pageNo":1,"pageSize":20}}}}'''.format(
            self.host, self.port, this_id, this_id)
        try:
            r = requests.get(url, headers=self.headers, timeout=timeout)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception('url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise
        
    def get_picrecord(self, **p):
        param = {
	    "page": {
	        "pageNo": p.get("page", 1),
	        "pageSize": p.get("per_page", 20)
	    }
        }
	if "st" in p.keys():
	    param["startDate"] = p["st"]
	if "et" in p.keys():
	    param["endDate"] = p["et"]
	if "startid" in p.keys():
	    param["startId"] = p["startid"]
	if "endid" in p.keys():
	    param["endId"] = p["endid"]
        url = '''http://{0}:{1}/dahuaIS/rest/picrecord/search?q={2}'''.format(
            self.host, self.port, json.dumps(param))
        try:
            r = requests.get(url, headers=self.headers, timeout=30)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception('url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise

    def get_device(self, timeout=30):
        url = '''http://{0}:{1}/dahuaIS/rest/devChn/search'''.format(
            self.host, self.port)
        try:
            r = requests.get(url, headers=self.headers, timeout=timeout)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception('url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise


if __name__ == '__main__':  # pragma nocover
    dhkk = DHKakou(**{'host': '10.44.245.247', 'port': 8082})
    #j = dhkk.get_picrecord(280128615, 280128615)
    #print j
    #for i in dhkk.get_picrecord(80128615, 80128615)['data']['rows']:
    #	print i
    p = {
	"st": '2017-08-17 12:00:00',
	"et": '2017-08-17 12:01:00'
    }
    print dhkk.get_picrecord(**p)
    #print json.loads(r.text)
    #print("test")
    #    if i['carType'] > 2:
    #        print i
    #    if i['carNum'][-1] == u'警':
    #        print i
    #l = dhkk.get_picrecord_by_time('2016-10-10 12:00:00','2016-10-10 12:00:30')['data']['rows']
    #print len(l)
    #for i in dhkk.get_picrecord_by_time('2016-10-10 12:00:00','2016-10-10 12:00:10')['data']['rows']:
	#print i
