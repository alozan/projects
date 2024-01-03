import time
import numpy as np


print ("Primer matriz")
aa= float(input("Primer :"))
ab= float(input("segundo:"))
ac= float(input("tercer :"))
ad= float(input("cuarto :"))
ae= float(input("quinto :"))
af= float(input("sexto  :"))
ag= float(input("septimo:"))
ah= float(input("octavo :"))
ai= float(input("noveno :"))


print("Segunda Matriz")
ba= float(input("Primer :"))
bb= float(input("segundo:"))
bc= float(input("tercer :"))
bd= float(input("cuarto :"))
be= float(input("quinto :"))
bf= float(input("sexto  :"))
bg= float(input("septimo:"))
bh= float(input("octavo :"))
bi= float(input("noveno :"))

ta=time.time()
A = np.array([[aa,ab,ac],
              [ad,ae,af],
              [ag,ah,ai]])
B = np.array([[ba,bb,bc],
              [bd,be,bf],
              [bg,bh,bi]])

C = A+B
tb=time.time()

print(C)
print(tb-ta)  

tc=time.time()
D = A*B
E = D*C
F = E*A
td=time.time()

print(D)
print(E)
print(F)
print(td-tc)


