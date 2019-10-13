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

init = [0.2, 0.2, 0.2, 0.2, 0.2]
learn = 0.2


def per(w0, w1, w2, w3, w4, x1, x2, x3, x4):
    cal = w0  + w1*x1 + w2*x2 +w3*x3 + w4*x4 
    if cal >0:
        return 1
    else:
        return 0
dis = []
for i in range (len(new_list)):
    
    h0 =per(init[0], init[1], init[2], init[3], init[4], eval(new_list[i][0]), eval(new_list[i][1]), eval(new_list[i][2]), eval(new_list[i][3]))
    
    
    if (h0 == 1 and new_list[i][0] == 'Iris-setosa') or (h0 == 0 and new_list[i][0] == 'Iris-versicolor'):
        dis.append(0)
    elif (h0 == 1 and new_list[i][0] == 'Iris-versicolor'):
        dis.append(-1)
    else:
        dis.append(1)
    
    init[0] = init[0] +learn*(dis[0])
    for k in range(4):
            init[k+1] = init[k+1] +learn*(dis[i])* eval(new_list[i][k])

print(init)
dis = []
for i in range (10):
    h0 =per(init[0], init[1], init[2], init[3], init[4], eval(test_list[i][0]), eval(test_list[i][1]), eval(test_list[i][2]), eval(test_list[i][3]))
    if (h0 == 1 and new_list[i][0] == 'Iris-setosa') or (h0 == 0 and new_list[i][0] == 'Iris-versicolor'):
        dis.append(0)
    elif (h0 == 1 and new_list[i][0] == 'Iris-versicolor'):
        dis.append(-1)
    else:
        dis.append(1)
print(dis)