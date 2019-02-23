from pylab import *
from numpy import *
def f(x,v,t):
    return -x
n=200
h=6.28/float(n)
t=zeros(n,float)
x=zeros(n,float)
v=zeros(n,float)
v[0]=1.0
for i in range(1,n):
    t[i]=h*i
    x[i]=x[i-1]+v[i-1]*h
    v[i]=v[i-1]+f(x[i-1],v[i-1],t[i-1])*h
plot(t,x,"k-")
plot(t,v,"k--")
xlabel("t")
ylabel("y= sin x ve y = cos x")
show()
