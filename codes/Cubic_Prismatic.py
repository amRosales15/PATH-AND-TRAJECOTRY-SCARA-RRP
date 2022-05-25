import numpy as np
import matplotlib.pyplot as plt

# mm to m converter
def mm_to_m(d):
    m=1000
    return d/m

di = float(input('di = ')) # initial position  0, for testing
di = mm_to_m(di)

vi = float(input('vi = ')) # initial velocity  0, for testing
vi = mm_to_m(vi)

df = float(input('df = ')) # final position    120, for testing
df = mm_to_m(df)

vf = float(input('vf = ')) # final velocity    50, for testing
vf = mm_to_m(vf)

ti = float(input('ti = ')) # initial time      0, for testing   
tf = float(input('tf = ')) # final time        9, for testing

# Cubic
# Solve the solution for d(t) = a + (3*(b-a)/c**2)*t**2 - (2*(b-a)/c**3)*t**3

x = np.arange(ti,tf,0.05)

def cubic(t,a,b,c):
    return a + (3*(b-a)/c**2)*t**2 - (2*(b-a)/c**3)*t**3

y = cubic(x,di,df,tf)

plt.figure()
plt.plot(x,y,'r',linestyle='-')
plt.text(1,1.5,'d(t) = a + (3*(b-a)/c**2)*t**2 - (2*(b-a)/c**3)*t**3')
plt.grid(True)
plt.show()