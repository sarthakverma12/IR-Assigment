#Roll number: 2019BCS-056
#Name: Sarthak Verma
import math
import numpy as np
import matplotlib.pyplot as plt
p = np.zeros((4, 2), dtype=np.float64)
for i in range(4):
    p[i][0] = float(input("Enter p{} x-coordinate: ".format(i)))
    p[i][1] = float(input("Enter p{} y-coordinate: ".format(i)))

d = np.zeros((3, 1), dtype=np.float64)
for i in range(3):
    d[i] = math.dist(p[i], p[i + 1])

t = np.zeros((1, 2), dtype=np.float64)
t[:, 0] = float(input("Enter goal x-coordinate: "))
t[:, 1] = float(input("Enter goal y-coordinate: "))

plt.title("Initial Graph")
plt.plot(p[:, 0], p[:, 1], color="orange", marker='o', markerfacecolor='blue')
plt.show()
if d.sum() < math.dist(t[0], p[0]):
    for i in range(3):
        r = math.dist(t[0], p[i])
        la = d[i] / r
        p[i + 1] = (1 - la) * p[i] + la * t[0]
    print("The goal is unreachable")
    print("Final positions: ")
    for i in range(4):
        print("p{} = ({} , {})".format(i, p[i, 0], p[i, 1]))
else:
    b = np.copy(p[0])
    dif = math.dist(p[3], t[0])
    itr = 0
    while dif > 0.001:
        p[3] = t[0]
        for i in range(2, -1, -1):
            r = math.dist(p[i + 1], p[i])
            la = d[i] / r
            x = (1 - la) * p[i + 1] + la * p[i]
            p[i] = x
        p[0] = b
        for i in range(3):
            r = math.dist(p[i + 1], p[i])
            la = d[i] / r
            x = (1 - la) * p[i] + la * p[i + 1]
            p[i + 1] = x
        dif = math.dist(p[3], t[0])
        itr += 1
    print("Final positions: ")
    for i in range(4):
        print("p{} = ({} , {})".format(i, p[i, 0], p[i, 1]))
    print("Number of iterations: {}".format(itr))
    plt.title("Final graph")
    plt.plot(p[:, 0], p[:, 1], color="orange", marker='o', markerfacecolor='blue')
    plt.show()
