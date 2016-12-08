
import re

def textParse(file):
    file = file.strip().decode('gbk')
    #file = file.split()
    #file = file.strip().decode('gbk')
    p2 = re.compile(ur'[^\u4e00-\u9fa5]')
    file = p2.split(file)
    file = filter(lambda x: len(x) > 0 , file)


    return file

def get_data():
    training = open("pku_training.txt").read()
    training = textParse(training)
    return training
    #print training

def train(text):
    start = {'B':0, 'E':0, 'M':0, 'S':0}
    trans = {}
    emit = {}
    sfreq = [0,0,0,0]
    state = []
    chlist= []

    state_ch = ['B', 'E', 'M', 'S']
    B = 0; E = 1; M = 2; S = 3
    for word in text:
        if (len(word) == 0):
            continue
        if (len(word) == 1):
            state.append(S)
            chlist.append(word[0])
            sfreq[S] += 1
            continue

        sfreq[B] += 1
        sfreq[E] += 1
        sfreq[M] += len(word) - 2
        state.append(B)
        for i in range(len(word) - 2):
            state.append(M)
            sfreq[M] += 1
        for i in range(len(word)):
            chlist.append(word[i])
        state.append(E)


    print sfreq
    start['B'] = sfreq[B] * 1.0 / sum(sfreq)
    start['E'] = sfreq[E] * 1.0 / sum(sfreq)
    start['M'] = sfreq[M] * 1.0 / sum(sfreq)
    start['S'] = sfreq[S] * 1.0 / sum(sfreq)
    # todo : remove the punctuations
    #print start
    #print state
    trfreq = []
    for i in range(4):
        trfreq.append([])
        for j in range(4):
            trfreq[i].append(0)


    #print trfreq

    for i in range(len(state)):
        if (i == 0):
            continue
        trfreq[state[i-1]][state[i]] += 1

    for i in range(4):
        trans[state_ch[i]] = {}
        for j in range(4):
            trans[state_ch[i]][state_ch[j]] = trfreq[i][j] * 1.0 / sum(trfreq[i])
    #print trans
    emit = {}
    for i in range(4):
        emit[state_ch[i]]= {}

    efreq = [0, 0, 0, 0]
    for i in range(len(chlist)):
        si = state_ch[state[i]]
        emit[si][chlist[i]] = 0

    for i in range(len(chlist)):
        si = state_ch[state[i]]
        emit[si][chlist[i]] += 1

    for key in emit:
        for character in emit[key]:
            emit[key][character] = emit[key][character] * 1.0 / sfreq[state_ch.index(key)]


    return start, trans, emit


def viterbi(file, start, trans, emit):
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
                if (emit[sj].has_key(sentence[i])):
                    if (i == 0):
                        f[i][j] = start[sj]
                        pre[i][j] = -1
                    else:
                        f[i][j] = 0;
                        for sk in state:
                            if trans[sk].has_key(sj):
                                k = state.index(sk)
                                if (f[i-1][k] * trans[sk][sj] > f[i][j]):
                                    f[i][j] = f[i-1][k] * trans[sk][sj]
                                    pre[i][j] = k
                        #print file[i].decode('utf8')
                        f[i][j] *= emit[sj][sentence[i]]
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


        print >>fl, slabel.encode('utf-8')


        for i in range(totword):
            if (i > 0 and (slabel[i] == 'B' or slabel[i] == 'S')):
                str += '/'
            str +=sentence[i];
        str += '/'


    print >>fo,  str.encode('utf-8')

def cut(start, trans, emit,file):
    for subfile in file:
        viterbi(subfile, start, trans, emit)


def work(file):
    train_data = get_data()
    start, trans, emit = train(train_data)
    cut(start, trans, emit,file)

#    print_parameter(start, trans, emit)
#    classify(start, trans, emit)

#    filename = 'pku_test.txt'
#    file = open(filename)
#    for subfile in file:
#        work(subfile)


work(file);
