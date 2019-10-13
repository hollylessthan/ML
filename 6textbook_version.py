import random as rd
import numpy as np
import math
desk ="/Users/lofangyu/Desktop/"
f = open(desk + "training data.txt", "r")
list = f.readlines()
new_list=[]
for i in range(len(list)):
    m = list[i]
    n = m.replace(","," ")
    new_list.append(n.split())

desk ="/Users/lofangyu/Desktop/"
f = open(desk + "testing-data.txt", "r")
list = f.readlines()
test_list=[]
for i in range(len(list)):
    m = list[i]
    n = m.replace(","," ")
    test_list.append(n.split())

m = 90
for i in range(90):
    new_list[i].append(1/m)

WEE = []
sum_error = []
#1-n-n function
def dis(a, b, c, d):
    return ( (a - eval(new_list[t][0]))**2 + (b - eval(new_list[t][1]))**2 + (c - eval(new_list[t][2]))**2 + (d - eval(new_list[t][3]))**2 ) **(1/2)
#random number based on probability
for f in range(9): 
    rad = []

    select = []
    for k in range(len(new_list)):
        times = 0
        for l in range(len(new_list)):
            if new_list[k][5] > new_list[l][5]:
                times += 1
            else:
                times = times
        if times >= 80:
            select.append(k)
        else:
            select = select
    
    other = []
    if len(select) != 0 and len(select)< 10:
        for k in range(len(new_list)):
            for g in range(len(select)):
                if k != select[g]:
                    other.append(k)
                else:
                    other = other
        Tim = []
        for d in range(len(other)):
            tim = 0
            for v in range(len(other)):
                if new_list[other[d]][5] > new_list[other[v]][5]:
                    tim += 1
                else:
                    tim = tim
            Tim.append(tim)
        maxi = []
        maxi = rd.sample(range(0,(90 - len(select))),(10 - len(select)))
        for h in range(len(maxi)):
            select.append(other[maxi[h]])
        
        rad = select
        
    elif len(select) == 0:
        rad =rd.sample(range(0,90),10)            
    else:
        rad = select
   
    #1nn classifier for selected 10 training examples
    test=[]
    k_n_n = []
    test_class = []  
    for r in range(len(rad)):
        for t in range (len(new_list)):
            t1 = dis(eval(new_list[rad[r]][0]), eval(new_list[rad[r]][1]), eval(new_list[rad[r]][2]), eval(new_list[rad[r]][3]))
            t2 = new_list[t][4]
            test.append([t1, t2])
        
        k_n_n = sorted(test)
        if k_n_n[0][1] == "Iris-setosa":
            test_class.append("Iris-setosa")
        else:
            test_class.append("Iris-versicolor")
        test = []
        k_n_n = []
    #1nn for testing examples
    TEST = []
    K_N_N = []
    TEST_class = []
    for a in range(10):
        for t in range (len(new_list)):
            t1 = dis(eval(test_list[a][0]), eval(test_list[a][1]), eval(test_list[a][2]), eval(test_list[a][3]))
            t2 = new_list[t][4]
            TEST.append([t1, t2])
        
        K_N_N = sorted(TEST)
        if K_N_N[0][1] == "Iris-setosa":
            TEST_class.append("Iris-setosa")
        else:
            TEST_class.append("Iris-versicolor")
        TEST = []
        K_N_N = []
    #count error rate and revise the probability
    error = []
    for g in range (len(test_class)):
        if test_class[g] == new_list[g][4]:
            error.append(0)
        else:
            error.append(1)
     
 
    ERROR = []

    for g in range (len(TEST_class)):
        if TEST_class[g] == new_list[g][4]:
            ERROR.append(0)
        else:
            ERROR.append(1)
     
    sum_error.append(ERROR)
   
    weighted_error = 0
    beta = 0
    
    for m in range(len(error)):
        weighted_error += new_list[rad[m]][5] * error[m]
        
    beta = weighted_error / (1 - weighted_error)
    WEE.append(weighted_error)  

    #normalization
    normal = 0
    for i in range(len(rad)):
        if error[i] == 0:
            new_list[rad[i]][5] = new_list[rad[i]][5] * beta
            normal += new_list[rad[i]][5]
                
        else:
            new_list[rad[i]][5] = new_list[rad[i]][5]
            normal += new_list[rad[i]][5]

                
    for i in range(len(rad)):
        new_list[rad[i]][5] = new_list[rad[i]][5] / normal / 9
#perceptron learning for deciding weight of the 9 classifiers
init = [0.1, 0.1, 0.1, 0.1, 0.1]
learn = 0.2

dis = []
def per(w0, w1, w2, w3, w4, w5, w6, w7, w8, w9, x1, x2, x3, x4, x5, x6, x7, x8, x9):
    cal = w0  + w1*x1 + w2*x2 +w3*x3 + w4*x4 + w5*x5 + w6*x6 +w7*x7 + w8*x8 + w9*x9 
    if cal >0:
        return 1
    else:
        return 0
init = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,0.1]
for i in range(len(WEE)):
    h1 = per(0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, WEE[0], WEE[1], WEE[2], WEE[3], WEE[4], WEE[5], WEE[6], WEE[7], WEE[8])

    if h1 == 0:
        dis.append(0)

    else:
        dis.append(1)
    
    init[0] = init[0] +learn*(dis[0])
    for k in range(4):
            init[k+1] = init[k+1] +learn*(dis[i])* eval(new_list[i][k])

#performance for classifying testing examples

perform = []

for d in range(9):
    POS = 0
    NEG = 0
    for i in range(10):
        if sum_error[d][i] ==  0: 
            POS += init[d+1]
        else:
            NEG += init[d+1]
    if POS > NEG:
        perform.append(0)
    else:
        perform.append(1)
   
print(perform)