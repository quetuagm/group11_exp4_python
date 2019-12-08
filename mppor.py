# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 00:09:33 2019

@author: asus
"""
import numpy as np
import math as m
import matplotlib.pyplot as plt
h=float(input ('Enter the value of initial height in meters:'));
v=float(input ('Enter the value of velocity:'));
d=float(input ('Enter the value of angle in degrees:'));
x=float(input ('Enter the value of x-component of the accelaration:'));
y=float(input ('Enter the value of y-component of the accelaration(must negative):'));
if y >= 0:
    print('Try again')

a= d*(m.pi/180)
tt=(2*v*m.sin(a))/(-y)
t=np.linspace(0,tt,100);
sx=v*(m.cos(a)*t);
sy=v*(m.sin(a)*t)+(0.5*y*(t**2));

plt.plot(sx,sy)
plt.grid()
plt.xlabel('Horizontal')
plt.ylabel('Vertical')
plt.title('Projectile Trajectory')
