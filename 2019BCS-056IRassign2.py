#Name: Sarthak Verma
#Roll no: 2019BCS-056
import numpy as np
import math

co = np.ones((4, 1))
co[0] = float(input('Enter X coordinate: '))
co[1] = float(input('Enter Y coordinate: '))
co[2] = float(input('Enter Z coordinate: '))
ch = 'y'
while ch == 'y':
    a = input('Enter axis for rotation: ')
    th = float(input('Enter angle of rotation: '))
    rot = np.zeros((4, 4))
    rot[3][3] = 1
    if a == 'x':
        rot[0][0] = 1;
        rot[1][1] = math.cos(math.radians(th))
        rot[1][2] = -math.sin(math.radians(th))
        rot[2][1] = math.sin(math.radians(th))
        rot[2][2] = math.cos(math.radians(th))
    if a == 'y':
        rot[0][0] = math.cos(math.radians(th))
        rot[0][2] = math.sin(math.radians(th))
        rot[2][0] = -math.sin(math.radians(th))
        rot[2][2] = math.cos(math.radians(th))
        rot[1][1] = 1
    if a == 'z':
        rot[0][0] = math.cos(math.radians(th))
        rot[1][0] = math.sin(math.radians(th))
        rot[0][1] = -math.sin(math.radians(th))
        rot[1][1] = math.cos(math.radians(th))
        rot[2][2] = 1
    rot[0][3] = float(input('Input translation for x axis(0 if none): '))
    rot[1][3] = float(input('Input translation for y axis(0 if none): '))
    rot[2][3] = float(input('Input translation for z axis(0 if none): '))
    result = np.zeros((4, 1))
    for i in range(len(rot)):
        for j in range(len(co[0])):
            for k in range(len(co)):
                result[i][j] += rot[i][k] * co[k][j]
    co = result
    ch = input("Want to add another set of rotation and translation(y/n): ")

print('Coordinates w.r.t original frame are: ')
print('X: {}'.format(float(co[0])))
print('Y: {}'.format(float(co[1])))
print('Z: {}'.format(float(co[2])))
