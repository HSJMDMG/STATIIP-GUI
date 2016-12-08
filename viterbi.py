import prob_start as start
import prob_trans as trans
import prob_emit as emit
import re

def textParse(file):
    print file[0]
    #file = file.decode('gbk')
    file = file.strip().decode('gbk')
    p2 = re.compile(ur'[^\u4e00-\u9fa5]')
    file = p2.split(file)
    #file  = file.split()
    file = filter(lambda x: len(x) > 0 , file)
    #print file
    return file

def work(file):
    file = textParse(file)
    state = ['B', 'E','M','S']
    str = ""
    # dp
    for sentence in file:
        totword = len(sentence)
        f = []
        pre = []
        for i in range(totword):
            f.append([])
            pre.append([])
            for sj in state:
                f[i].append(0)
                pre[i].append(-1)
                j = state.index(sj)
                if (emit.matrix[sj].has_key(sentence[i])):
                    if (i == 0):
                        f[i][j] = start.matrix[sj]
                        pre[i][j] = -1
                    else:
                        f[i][j] = 0;
                        for sk in state:
                            if trans.matrix[sk].has_key(sj):
                                k = state.index(sk)
                                if (f[i-1][k] * trans.matrix[sk][sj] > f[i][j]):
                                    f[i][j] = f[i-1][k] * trans.matrix[sk][sj]
                                    pre[i][j] = k
                        #print file[i].decode('utf8')
                        f[i][j] *= emit.matrix[sj][sentence[i]]
                else:
                    f[i][j] = 0

        #print >>fo, pre

        pos = 3
        maxprob = 0
        slabel = ''
        for i in range(4):
            if f[totword - 1][i] > maxprob:
                maxprob = f[totword - 1][i]
                pos = i

        t = totword - 1
        while (t>=0):
            slabel = state[pos] + slabel
            pos = pre[t][pos]
            t -= 1


        #print >>fl, slabel.encode('utf-8')


        for i in range(totword):
            if (i > 0 and (slabel[i] == 'B' or slabel[i] == 'S')):
                str += '/'
            str +=sentence[i];
        str += '/'


    return str
