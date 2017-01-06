#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import viterbi
import supervised
import hw1Small
import hw1Large
import os

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

def hw4Seg(data):

    toseg = open("static/crf/to_seg.txt","w")
    #data = data.encode('gbk')
    #print data.encode('utf-8')
    print >> toseg, data

    toseg.close()

    status = os.system('./exec.sh')
    #time.sleep(0)
    print 'exec.sh STATUS:', status
    print 'STATUS:', status>>8

    output = open("static/crf/segfile.txt").read().decode("gbk")
    return output




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
