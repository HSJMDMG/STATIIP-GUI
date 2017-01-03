#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import viterbi
import supervised
import hw1Small
import hw1Large

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

def hw3Chinese(data, choicestr):
    if (choicestr[0] == 'v'):
        return viterbi.work(data)
    else:
        return supervised.work(data)

def hw1NB(data, choicestr):
    if (choicestr[0] == 'e'):
        return hw1Small.SpamTest(data)
    else:
        return hw1Large.SpamTest(data)
