import math
import numpy as np


def tmat(dh_table, i):
    c = math.cos(dh_table[i][3])
    s = math.sin(dh_table[i][3])
    a = dh_table[i][1]
    cs = math.cos(dh_table[i][0]) * s
    cc = math.cos(dh_table[i][0]) * c
    sal = math.sin(dh_table[i][0])
    ds = dh_table[i][2] * math.sin(dh_table[i][0])
    ss = math.sin(dh_table[i][0]) * s
    sc = math.sin(dh_table[i][0]) * c
    cal = math.cos(dh_table[i][0])
    dc = dh_table[i][2] * math.cos(dh_table[i][0])
    return np.array([[c, -s, 0, a], [cs, cc, -sal, -ds], [ss, sc, cal, dc], [0, 0, 0, 1]])


print("Enter dh_table[alpha,a,d,theta]")
dht = np.zeros(shape=(6, 4))
for i in range(6):
    for j in range(4):
        val = int(input("Enter parameter of {}th row and {}th column: ".format(i + 1, j + 1)))
        if j == 0 or j == 3:
            val = math.radians(val)
        dht[i][j] = val

tmats = []
for i in range(6):
    tmats.append(tmat(dht, i))

m = tmats[0]
for i in range(5):
    m = np.dot(m, tmats[i + 1])

print("Final coordinates of end effector: ", m[0:3, 3])
print("Final orientation of the end effector: ")
print(m[0:3, 0:3])