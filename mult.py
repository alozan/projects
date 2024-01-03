# Adding two matrices
import time
import numpy as np

start = time.time()
# Define two matrices
A = np.array([[1100,2100,3100],
              [4200,5200,6200],
              [7300,8300,9300],
              [9999,7777,8888],
              [4444,5555,9999]])

B = np.array([[9900,8900,7900],
              [6800,5800,4800],
              [3700,2700,1700],
              [1111,3333,2222],
              [6666,5555,1111]])

C = A+B   # Do the addition
end = time.time()

l=time.time()
d = A*B
k=time.time()
n=time.time()
e = C*d
p=time.time()
q=time.time()
f= d*e*C
r=time.time()
y=time.time()
ans=A*B*C*d*e*f
z=time.time()
x=time.time()
po=(A*B*C*d*e*f)*3
w=time.time()
aa=time.time()
ab= A*A*A*A*A*A
ac= B*B*B*B*B*B
ad= ab*ac
ae=time.time()






print(C)
print (end-start)
print (d)
print (k-l)
print (e)
print(p-n)
print(f)
print(r-q)
print(ans)
print(z-y)
print(po)
print(w-x)
print(ab)
print(ac)
print(ad)
print(ae-aa)
