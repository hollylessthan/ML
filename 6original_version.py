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


#1-n-n function
def dis(a, b, c, d):
    return ( (a - eval(new_list[t][0]))**2 + (b - eval(new_list[t][1]))**2 + (c - eval(new_list[t][2]))**2 + (d - eval(new_list[t][3]))**2 ) **(1/2)

sum_error = []
WEE = []
for f in range(9): 
    #select random number
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
    #end of selection
    #建立1nn classifier
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
    #test example 放10個來分類
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
        
    #按照上課講義計算錯誤率，然後重新估計機率
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
    WEE.append(weighted_error)    
    beta = (weighted_error / (1 - weighted_error)) ** (1/2)
    
    normal = 0
    if beta == 0:
        beta = 1
    else:
        beta = beta
    for i in range(len(rad)):
        if error[i] == 0:
            new_list[rad[i]][5] = new_list[rad[i]][5] * beta
            normal += new_list[rad[i]][5]
                
        else:
            new_list[rad[i]][5] = new_list[rad[i]][5] / beta
            normal += new_list[rad[i]][5]

            
    for i in range(len(rad)):
        new_list[rad[i]][5] = new_list[rad[i]][5] / normal / 9
#apha
def weight(weightederror):
    return (1/2) * math.log(weightederror / (1 - weightederror)) 
perform = []

#計算分類testing example的表現
for d in range(len(WEE)):
    POS = 0
    NEG = 0
    for i in range(10):
        if sum_error[d][i] ==  0: 
            POS += weight(WEE[d])
        else:
            NEG += weight(WEE[d])
    if POS > NEG:
        perform.append(0)
    else:
        perform.append(1)
   
print(perform)
