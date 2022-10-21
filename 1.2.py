#1.2 Asoslari a va b (a>b), katta asosdagi burchagi α bo’lgan teng yonli trapetsiyaning perimetri hamda yuzasi topilsin. (burchak radianda beriladi)

import math
a=float(input('katta tomonni kiriting: '))
b=float(input('kichik tomonni kiriting: '))
alfa=float(input('burchakni kiriting(radianda): '))
h=(math.atan(alfa)*(a-b))/2
c=(h**2+((a-b)/2)**2)**0.5
p=a+b+2*c
s=0.5*(a+b)/h
print(f'perimetr={int(p)} yuza={int(s)}')