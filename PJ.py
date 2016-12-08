#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
def work():
    csvfile = file('static/data.csv', 'wb')
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'url', 'keywords'])
    data = [
      ('1', 'http://www.xiaoheiseo.com/', 'aa'),
      ('2', 'http://www.baidu.com/', 'bb'),
      ('3', 'http://www.jd.com/', 'cc')
    ]
    writer.writerows(data)
    csvfile.close()

def hw3Chinese(data):
    result = u'你好, ' + data;
    return result
