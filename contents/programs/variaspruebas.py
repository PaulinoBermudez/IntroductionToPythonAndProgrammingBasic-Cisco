ML = ['red','orange','blue','green']
ML[2] = 'purple'
print(ML)


d = {
    'food' : ["Pasta", "bread","Rice"],
    "with": ["Butter", "sauce","stir fry"],
}

print(d['food'][0]+ " goes with " + d['with'][1])

#!/bin/python 
import os
os.system('clear')
os.system('cls')
# @author: [ Paulino Bermúdez R.]
# @Description: 

i = 0
while i <= 3:
    i += 2
    print("*----------")

i = 0
while i <= 5: 
    i += 1
    if i % 2 == 0: 
        break 
    print("+")

for y in range(1):
    print("@")
else:
    print("@")

var = 0
while var < 6:
    var +=1
    if var %2 == 0:
        continue
    print("#")

v = 1 
while v < 10:
    print("---------&")
    v = v << 1
    print(v)

z = 10 
y = 0

X = y < z and z > y or y > z and z < y
print(X)



lst = [ 3, 1, -2]
print(lst[lst[-1]])

lst = [1,2,3,4]
print(lst[-3:-2])

from random import random

for i in range(5):
    r = (random()*100)
    print("Sus probabilidades son: {:e}".format(r))

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)
print(python_implementation)



l1 = [1,2,3]
l2 = []
for v in l1:
	l2.insert(0,v)
print(l2)
print(len(l1))
print(len(l2))

L = [I for I in range (-1,2)]
print(len(L))

T = [[3-i for i in range (3)] for j in range(3)]
S = 0
for i in range(3):
    S += T[i][i]
print(S)

#L = [[0,1,2,3,] for I in range(2)]
#print(L[2][0])


def f(x):
	if x == 0:
		return 0
	return x + f(x-1)
print(f(3))

def fun(X):
	X += 1
	return X
X = 2 
X = fun(X+1)
print(X)		

Dct = {}
Lst = ['a','b','c','d']
for I in range (len(Lst)-1):
	Dct [Lst[i]] = (lst[I], )
for I in sorted (Dct.keys()):
	K = Dct[I]
print(K[0])



def func1(a):
	return a**a 
def func2(a):
	return func1(a)*func1(a)
print(func2(2))

def fun(x,y,z):
	return x+2*y+3*z
print(fun(0, z=1, y = 3))


print(chr(ord('z') -2))

class A:
	X = 0
	def __init__(self, v = 0):
		self.Y = v
A.X += v
a = A()
b = A(1)
c = A(2)
print(c.X)

class A:
	A = 1
print(hasattr(A,'A'))


l = [[ x for x in range(3) ] for y in range(3)]
for r in range(3):
    for c in range(3):
        if l[r][c] % 2 != 0:
            print("#")
print("------------")

def f(i=2,o=3):
    return i*o 
print(f(o=2))
print("------------")


d = {}
d['1']=(1,2)
d['2']=(2,1)
for x in d.keys():
    print(d[x][1], end='')
print("------------")

d = {"1":"0","0":"1"}
for x in d.values():
    print(x, end='\n')
print("------------")

t = (1,2,4,8)
t = t[-2:-1]
t = t[-1]
print(t)
print("------------")
def fun(x,y):
    if x == y:
        return x 
    else:
        return fun(x, y-1)
print(fun(0,3))
print("------------")
L = [i for i in range(-1,-2)]
print(L)
print("------------")
x = 2.0
y = 4.0
print(y**(1/x))
print(1//2)

d = {
    "one":"two", "three":"one", "two":"three"
}
v = d['three']
for k in range(len(d)):
    v = d[v]
print(v)

print("_______@@@@@@@@@____________")
def f(i=2,o=3):
    print( i*o)
print(f(o=2))
print("_______@@@@@@@@@@____________")
a = 1
b = 0
a = a ^ b
b = a ^ b 
a = a ^ b

print(a,b)

l = [ i for i in range(-1,-2)]
print(l)
print("___________________")

print(1//5+1/5)
print("___________________")
print('a','b','c',sep='sep')

n = [1,2,3]
v = n
print(v,n)
d = {"1":"0", "0":"1"}

x = 1
y = 2
x, y, z = x, x , y
z, y, z = z, y, z 
print(x,y,z)

def fun(x,y):
    if x == y:
        return x
    else:
        return fun(x, y-1)
print(fun(0,3))
t = (1,2,4,8)
t = t[-2:-1]
t = t[-1]
print("_________//__________")
print(t)
print("_________//__________")
d = {}
d['1'] = (1,2)
d['2'] = (2,1)
for x in d.keys():
    print(d[x][1], end="")
print("__________|||||||||||||||_________")
print("__________|||||||||||||||_________")
print("__________|||||||||||||||_________")

l = [ x*x for x in range(5)] 
print("\n")
def fun(ls):
    del ls[ls[2]]
    return ls 
print(fun(l))

x = 3
y = 2
x = x % y
x = x % y
y = y % x 
print(y)

print("___________________")
n = [1,2,3]
v = n
del v[:]
print(v,n)
print("________*******___________")
l = [1,2]
for v in range(2):
    l.insert(-1, l[v])
print(l)
print("_______*****____________")
z = 0
y = 10
print(y < z and z > y or y > z and z < y)


x = 2.0
y = 4.0
print( y ** (1/x))

print(1//2)
print("___________________")
print("__________|||||||||||||||_________")


print("__________|||||||||||||||_________")
print("__________|||||||||||||||_________")

import math
print(dir(math))

print(chr(ord('p')+2))

class A:
    def __init__(self, v = 2):
        self.v = v 
    def set(self, v = 1):
        self.v += v
        return self.v 
a = A()
b = a
b.set() 
print(a.v)

try:
    raise Exception (1,2,3)
except Exception as e:
    print(len(e.args))

class A:
    A = 1
    def __init__(self):
        self.a = 0
print(hasattr(A,'a'))

class A:
    def a(self):
        print('a')
class B:
    def a(self):
        print('b')
class C(B,A):        
    def c(self):
        self.a()
o = C()
o.c()

from math import sqrt
print(sqrt(2))
print(math.sqrt(2))

print(float("1.3"))

print(len("\\\\"))



class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0
    def __iter__(self):
        return self 
    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i+= 1
        return v 
for x in I():
    print(x, end='')

try: 
    raise Exception
except BaseException:
    print("a")
except Exception:
    print("b")
except:
    print("c")


class A:
    def __init__(self):
        pass
a = A()
print(hasattr(a, 'A'))


class A: 
    pass
class B(A):
    pass
class C(B):
    pass
print(issubclass(A.C))

#!/bin/python 
import os
os.system('clear')
os.system('cls')
# @author: [ Paulino Bermúdez R.]
# @Description: 

v = 1 + 1 // 2 + 1 / 2 + 2
print(v)

d = {}
d['2'] = [1,2]
d['1'] = [3,4]
for x in d.keys():
    print(d[x][1], end="")
t = (1,2,3,4)
t = t[-2:-1]
t = t[-1]
print(t)
l = [1,2,3,4]
l = list(map(lambda x: 2*x,l))
print(l)

def f(d,k,v):
    d[k]= v
dc = {}
print(f(dc,'1','v'))

l = [[c for c in range(r)] for r in range(3)]
for x in l:
    if len(x) < 2:
        print("_")

x = """
"""
print(len(x))

class A:
    A = 1
    def __init__(self, v=2):
        self.v = v + A.A 
        A.A += 1
    def set(self,v):
        self.v += v
        A.A += 1
        return 
a = A()
a.set(2)
print(a.v)

class A:
    A = 1
    def __init__(self):
        self.a = 0
print(hasattr(A,'A'))

class A: pass
class B: pass
class C(A,B): pass 
print(issubclass(C,A) and issubclass(C,B)) 

class A:
    def __init__(self,v):
        self._a = v +1 
a = A(0)
print(a._a)
class A:
    def a(self):
        print('a')
class B:
    def a(self):
        print('b')
class C(A,B):
    def c(self):
        self.a()
o = C()
o.c()

def I(n):
    s = ''
    for i in range(n):
        s += '*'
        yield s
for x in I(3):
    print(x, end="")

def a(x):
    def b():
        return x+x
    return b
x = a('x')
y = a('')
print(x() + y())

class A:
    def __init__(self, name):
        self.name = name
a = A("class")        
print(a)

l = [[c for c in range(r)] for r in range(3)]
for x in l :
    if len(x) < 2:
        print()

print(len((1,)))


print(len([i for i in range(0, -2)]))

print(__name__)

s1 = 'string'
s2 = s1[:]
print(s1,s2)


def funcion(d,k,v):
    d[k]=v
dc={}
print(funcion(dc,'1','v'))


x = 16 
while x > 0 :
    print('*', end='')
    x//=2


class X:
    pass
class Y(X):
    pass
class Z(Y):
    pass
x = X()
z = Z()
print(isinstance(x,Z), isinstance(z,X))


a = True
b = False
a = a or b
b = a and b
a = a or b 
print(a,b)

t = (1, )
t = t[0] + t[0]
print(1//2)