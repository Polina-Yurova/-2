#15 
import math
x=2.444
y=0.869*0.01
z=-0.13*1000
s=((x**(y+1)+math.exp(y-1))/(1+x*abs(y-math.tan(z))))*(1+abs(y-x))+(((y-x)**2)/2)-((abs(y-x)**3)/3)
print(s)