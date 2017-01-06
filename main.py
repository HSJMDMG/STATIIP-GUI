#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, request, redirect, flash, g
from werkzeug import secure_filename
from PJ import *
import csv

app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/guide')
def guide():
    return render_template('guide.html')

@app.route('/overview')
def overview():
    return render_template('overview.html')


@app.route('/presentation')
@app.route('/presentation/<hwname>')
def presentation(hwname=None):
    if (hwname == None):
        return render_template('presentation.html')
    else:
        return render_template( hwname + '.html')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)



@app.route('/tools')
def tools():
    return render_template('tools.html')




@app.route('/hw3text', methods=['POST'])
def post_text3():
    # success = 1; fail = 2
#    f = request.files['the_file'];


#    if (len(request.form['content']))
    if (len(request.form['content']) < 3):
        return render_template('hw3.html', inputData = request.form['content'], alertbar = 2)

    result = hw3Chinese(request.form['content'].encode('gbk'), request.form['wordchoice']);
    return render_template('hw3.html', inputData = request.form['content'], resultData = result , alertbar = 1)

@app.route('/hw3file', methods=['GET', 'POST'])
def upload_file3():
    if request.method == 'POST':
        f = request.files['filecontent']
        f.save('static/uploads/data.txt')
        inputData = open("static/uploads/data.txt").read()

        result = hw3Chinese(inputData, request.form['wordchoice']);


    return render_template('hw3.html', resultData = result , alertbar = 1)



@app.route('/hw4text', methods=['POST'])
def post_text4():
    if (len(request.form['content']) < 3):
        return render_template('hw4.html', inputData = request.form['content'], alertbar = 2)

    result = hw4Seg(request.form['content'].encode('gbk'));
    return render_template('hw4.html', inputData = request.form['content'], resultData = result , alertbar = 1)

@app.route('/hw4file', methods=['GET', 'POST'])
def upload_file4():
    if request.method == 'POST':
        f = request.files['filecontent']
        f.save('static/uploads/data.txt')
        inputData = open("static/uploads/data.txt").read()

        result = hw4Seg(inputData);


    return render_template('hw4.html', resultData = result , alertbar = 1)






@app.route('/hw1text', methods=['POST'])
def post_text1():

    result = hw1NB(request.form['content'], request.form['wordchoice']);
    return render_template('hw1.html', alertbar = result)

@app.route('/hw1file', methods=['GET', 'POST'])
def upload_file1():
    if request.method == 'POST':
        f = request.files['filecontent']
        #print f
        f.save('static/uploads/data.txt')
        inputData = open("static/uploads/data.txt").read()
        #print inputData
        result = hw1NB(inputData, request.form['wordchoice']);
        #print result
        return render_template('hw1.html', alertbar = result)





    # success = 1; fail = 2
#    f = request.files['the_file'];


#    if (len(request.form['content']))
#    if (len(request.form['content']) < 3):
#        return render_template('index.html', inputData = request.form['content'], alertbar = 2)
#
#    result = generateContent(request.form['content']);
#    return render_template('index.html', inputData = request.form['content'], resultData = result , alertbar = 1)

#    return render_template('index.html', inputData = request.form['content'], resultData = len(request['filecontent']) , alertbar = 1)







@app.route('/tool')
def tool():
    # a test case
    work()
    return render_template('tool.html')

if __name__ == '__main__':
    app.run(debug = True)
