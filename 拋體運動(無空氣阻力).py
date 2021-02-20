import math as m
h=float(input('起始高度(公尺):'))
v=float(input('速度(公尺/秒):'))
d=float(input('角度(度):'))
t=float(input('時間(秒):'))
g=float(input('重力加速度(公尺/秒平方):'))
s=m.sin(m.pi*d/180)#sin
c=m.cos(m.pi*d/180)#cos
T=v*s/g+s*m.sqrt(v*v+2*g*h)/g#飛行時間
a=v*t*c
b=h+v*s*t-0.5*g*m.pow(t,2)

if t>T:
    a=v*T*c
    b=0
        
x=a #x座標
y=b #y座標

print('x座標(公尺):',x,'y座標(公尺):',y)
input()   
