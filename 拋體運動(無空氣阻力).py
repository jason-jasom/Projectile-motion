import math as m
while True:
    h=float(input('height:'))#起始高度
    v=float(input('velocity:'))#速度
    d=float(input('degree:'))#角度
    t=float(input('time:'))#時間
    g=float(input('gravity:'))#重力加速度
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

    print(a,b)
    
