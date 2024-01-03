import time
import numpy as np


print ("Primer matriz")
aa= int(input("Primer :"))
ab= int(input("segundo:"))
ac= int(input("tercer :"))
ad= int(input("cuarto :"))
ae= int(input("quinto :"))
af= int(input("sexto  :"))
ag= int(input("septimo:"))
ah= int(input("octavo :"))
ai= int(input("noveno :"))


print("Segunda Matriz")
ba= int(input("Primer :"))
bb= int(input("segundo:"))
bc= int(input("tercer :"))
bd= int(input("cuarto :"))
be= int(input("quinto :"))
bf= int(input("sexto  :"))
bg= int(input("septimo:"))
bh= int(input("octavo :"))
bi= int(input("noveno :"))

ta=time.time()
A = np.array([[aa,ab,ac],
              [ad,ae,af],
              [ag,ah,ai]])
B = np.array([[ba,bb,bc],
              [bd,be,bf],
              [bg,bh,bi]])

C = A + B
tb=time.time()

print(C)
print(tb-ta)  

tc=time.time()
D = np.multiply(A,B)
E = np.multiply(D,C)
F = np.multiply(E,B)
G = np.multiply(A,A,A)
H = np.multiply(B,B,B)
I = np.multiply(G,H)
J = np.dot(I,H)
K = np.dot(G,H)
L = np.dot(E,A)
M = np.dot(G,H)
N = np.multiply(A,A,A)
O = np.multiply(B,B,B)
P = np.multiply(G,N)
Q = np.multiply(H,O)
td=time.time()


print("C")
print(C)
print("D")
print(D)
print("E")
print(E)
print("F")
print(F)
print("I")
print(I)
print("J")
print(J)
print("K")
print(K)
print("L")
print(L)
print("M")
print(M)
print("P")
print(P)
print("Q")
print(Q)
print(td-tc)
print(td-ta)

