# simple pendule

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import *


#parametres physiques
m = 1
L = 1
dt = 0.01
g = 9.8
a, b = pi/2, 0
gamma=0.7

#paramètres pou l'animation
dt = 0.03
tmax = 20
Nf = int(tmax/dt)
La, Lb = [], []

#preparation des figures
fig = plt.figure(1, figsize=(10, 5))
plt.subplots_adjust(left=0.1, wspace=0.4, top=0.8)
plt.suptitle('Pendule simple', fontsize=16)
fig.text(0.05, 0.9,'g='+str(g)+' m='+str(m) +' l='+str(L)+' gamma='+str(gamma) + '. Resolution, methode de Euler' )


#-- figure espace reel
xmin, xmax, ymin, ymax = -2, 2, -2, 2
ax = plt.subplot(121)
plt.title('Espace réel')
plt.xlabel('x')
plt.ylabel('y')
pendule, = ax.plot([], [], 'ro-')
ax.axis('equal')
ax.axis([xmin,xmax,ymin,ymax])
text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

# un rectangle
x,y = -1,0
dx,dy = 2, 0.5
rect = plt.Rectangle((x,y), dx, dy, facecolor='blue', edgecolor='black')
ax.add_patch(rect)

# un cercle
c = plt.Circle((0,-1), 1/5, facecolor = 'red', edgecolor='red')
ax.add_patch(c)

#--figure espace des phases
amin, amax, bmin, bmax = -pi,pi, -10, 10
bx = plt.subplot(122) # Il y a 1*2 sous figures. bx est la 2
plt.title('Espace des phases')
plt.xlabel('a')
plt.ylabel('b')
plt.grid(True)
trajectoire, = bx.plot([], [], 'bo') # cercles (o) bleus (b)
bx.axis([amin,amax,bmin,bmax]) # selectionne la vue


#equations du mouvement
def F(a,b):
    dadt = b
    dbdt = -g/L*sin(a) - gamma/m *b
    return dadt, dbdt

it = 0

while it<Nf:
    print(it)
    Fa, Fb = F(a,b)
    a = a + Fa*dt
    b = b + Fb*dt
    
    a = (a + pi)%(2*pi) - pi
    x,y = L*sin(a), -L*cos(a)
    
    pendule.set_data([0,x],[0,y])
    text.set_text('t = %.1fs' % (it*dt))
    c.center = x,y
    
    trajectoire.set_data(a,b)
    La.append(a)
    Lb.append(b)
    bx.plot(La,Lb,'.')
    
    #plt.savefig('image_' +str(it).zfill(4) + '.png', dpi=60)
    if it%10 == 0:
        plt.pause(0.001)
    it=it+1
    #plt.show()
    
plt.show()

