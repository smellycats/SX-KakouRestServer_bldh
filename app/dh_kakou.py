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
        
    def get_picrecord(self, _id, last_id):
        url = '''http://{0}:{1}/dahuaIS/rest/picrecord/search?q={{"startId":{2},"endId":{3},"page":{{"pageNo":1,"pageSize":100}}}}'''.format(
            self.host, self.port, _id, last_id)
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception('url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise

    def get_picrecord_by_time(self, st, et):
        url = '''http://{0}:{1}/dahuaIS/rest/picrecord/search?q={{"startDate":"{2}","endDate":"{3}","page":{{"pageNo":1,"pageSize":1000}}}}'''.format(
            self.host, self.port, st, et)
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception('url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise

    def get_device(self):
        url = '''http://{0}:{1}/dahuaIS/rest/devChn/search'''.format(
            self.host, self.port)
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception('url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise

