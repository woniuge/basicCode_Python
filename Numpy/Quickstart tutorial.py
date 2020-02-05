
'''
#1. An example
import numpy as np

a = np.arange(15).reshape(3,5)
#a = np.arange(15)

print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(a.itemsize)
print(a.data)
print(a.dtype.itemsize)
print(a.dtype.name)
print(type(a))

b = np.array([6,7,8])
print(type(b))
'''

'''
#2. Array Creation
import numpy as np
a = np.array([2,3,4])
print(a)
print(a.dtype)
b = np.array([(1.2,3,5),(5.1,5,6)])
print(b)
c = np.array([[1,2],[3,4]],dtype=complex)
print(c)
print(np.zeros((3,4)))
print(np.ones((2,3,4),dtype=np.int16))
print(np.empty((2,3)))
print(np.arange(10,30,5))
print(np.arange(0,2,0.3))
from numpy import pi
print(np.linspace(0,2,9))
x = np.linspace(0,2*pi,100)
f = np.sin(x)
'''

'''
#3. Printing Arrays
#数组太大，Numpy就自动省略中间的部分
import numpy as np
print(np.arange(10000))
print(np.arange(10000).reshape(100,100))
#强制完整显示
np.set_printoptions(threshold=np.nan)
print(np.arange(10000))
'''

'''
#4. Basic Operations
import numpy as np

a = np.array([20,30,40,50])
print(a)
b = np.arange(4)
print(b)
c = a - b
print(c)
print(b**2)
print(10*np.sin(a))
print(a<35)

A = np.array([[1,1],[0,1]])
B = np.array([[2,0],[3,4]])
print(A*B)
print(A@B)
print(A.dot(B))

a = np.ones((2,3),dtype=int)
b = np.random.random((2,3))
a *= 3
print(a)
b += a
print(b)

a = np.ones(3,dtype=np.int32)
from numpy import pi
b = np.linspace(0,pi,3)
print(b.dtype.name)
c = a+b
print(c.dtype.name)
d = np.exp(c*1j)
print(d.dtype.name)

a = np.random.random((2,3))
print(a.max())

b = np.arange(12).reshape(3,4)
print(b)
print(b.cumsum(axis=1))
'''

'''
#5. Universal Functions
import numpy as np
B = np.arange(3)
print(np.sqrt(B))
C = np.array([2.,-1.,4.])
print(np.add(B,C))
'''

'''
#6. Indexing,Slicing and Iterating
import numpy as np
a = np.arange(10)**3
print(a)
print(a[:6])
print(a[:6:2])
a[:6:2] = -1000
print(a)
print(a[::-1])
for i in a:
    print(i**(1/3.))

def f(x,y):
    return 10*x+y

b = np.fromfunction(f,(5,4),dtype=int)
print(b)
print(b[2,3])
print(b[:,1])
print(b[1:3,:])
print(b[-1])

c = np.array([[[0,1,2],[10,12,13]],[[100,101,102],[110,112,113]]])
print(c.shape)
print(c[...,2])
for row in b:
    print(row)
for element in b.flat:
    print(element)

a = np.floor(10*np.random.random((3,4)))    #np.floor():向下取整
print(a)
print(a.ravel())
print(a.reshape(6,2))
print(a.T)  #转置
a.resize(6,2)
print(a)
print(a.reshape(3,-1))  #效果同下
print(a.reshape(3,4))
'''

'''
#7. Stacking together different arrays
import numpy as np
a = np.floor(10*np.random.random((2,2)))
print(a)
b = np.floor(10*np.random.random((2,2)))
print(b)
print(np.vstack((a,b)))
print(np.hstack((a,b)))
from numpy import newaxis
print(np.column_stack((a,b)))
a = np.array([4.,2.])
b = np.array([3.,8.])
print(np.column_stack((a,b)))
print(np.hstack((a,b)))
print(a[:,newaxis])
print(np.column_stack((a[:,newaxis],b[:,newaxis])))
print(np.hstack((a[:,newaxis],b[:,newaxis])))
print(np.r_[1:4,0,4])
'''

'''
#8. Splitting one array into several smaller ones
import numpy as np
a = np.floor(10*np.random.random((2,12)))
print(a)
print(np.hsplit(a,3))
print(np.hsplit(a,(3,4)))
'''

'''
#9. Copies and Views
import numpy as np
#No Copy at All,既不拷贝array对象，也不拷贝他们的数据
a = np.arange(12)
b = a
print(b)
b.shape = 3,4
print(a)
def f(x):
    print(id(x))
print(id(a))
f(a)

#View or Shallow Copy，拷贝array对象，但不拷贝他们的数据
c = a.view()
print(c is a)
print(c.base is a)
print(c.flags.owndata)
c.shape = 2,6
print(a.shape)
c[0,4] = 1234
print(a)
print(c)

s = a[ : ,1:3]
print(s)
s[:] = 10
print(a)

#Deep Copy，既拷贝array的对象，又拷贝他们的数据
d = a.copy()
print(d is a)
print(d.base is a)
d[0,0] = 9999
print(a)
print(d)
'''

'''
#10. Fancy indexing and index tricks
import numpy as np
#Indexing with Arrays of Indices
a = np.arange(12)**2
i = np.array([1,1,3,8,5])
print(a[i])
j = np.array([[3,4],[9,7]])
print(a[j])

palette = np.array([[0,0,0],        # black
                   [255,0,0],       # red
                   [0,255,0],       # green
                   [0,0,255],       # blue
                   [255,255,255]])  # white
image = np.array([[0,1,2,0],    #each value corresponds to a color in the palette
                  [0,3,4,0]])
print(palette[image])

a = np.arange(12).reshape(3,4)
print(a)
i = np.array([[0,1],[1,2]])
j = np.array([[2,1],[3,3]])
print(a[i,j])   #由i和j各取相同位置上的两个数字组成坐标
print(a[i,2])
print(a[:,j])
l = (i,j)
print(a[l])
s = np.array([i,j])
print(a[tuple(s)])

time = np.linspace(20,145,5)
data = np.sin(np.arange(20)).reshape(5,4)
print(time)
print(data)
ind = data.argmax(axis=0)
print(ind)
time_max = time[ind]
data_max = data[ind,range(data.shape[1])]
print(time_max)
#print(data.shape)
#print(range(data.shape[1]))
print(data_max)
print(np.all(data_max == data.max(axis = 0)))
a = np.arange(5)
print(a)
a[[1,3,4]] = 0
print(a)
a = np.arange(5)
a[[0,0,2]] = [1,2,3]
print(a)

a = np.arange(5)
a[[0,0,2]] += 1 #得不到期望的结果
print(a)
#Indexing with Boolean Arrays
a = np.arange(12).reshape(3,4)
b = a > 4
print(b)
print(a[b])
a[b] = 0
print(a)
#generate an image of the Mandelbrot set:
import numpy as np
import matplotlib.pyplot as plt
def mandelbrot(h,w,maxit=20):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    y,x = np.ogrid[-1.4:1.4:h*1j,-2:0.8:w*1j]
    c = x + y*1j
    z = c
    divtime = maxit + np.zeros(z.shape,dtype=int)

    for i in range(maxit):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2       # who is diverging
        div_now = diverge & (divtime == maxit)  #who is diverging now
        divtime[div_now] = i    # note when
        z[diverge] = 2          # avoid diverging too much

    return divtime
plt.imshow(mandelbrot(400,400))
plt.show()

a = np.arange(12).reshape(3,4)
b1 = np.array([False,True,True])    # first dim selection
b2 = np.array([True,False,True,False])# second dim selection

print(a[b1,:])
print(a[b1])
print(a[:,b2])
print(a[b1,b2])#很奇怪

#The ix_() function
a = np.array([2,3,4,5])
b = np.array([8,5,4])
c = np.array([5,4,6,8,3])
ax,bx,cx = np.ix_(a,b,c)
print(ax.shape,bx.shape,cx.shape)
result = ax+bx*cx
print(result)
print(result[3,2,4])
print(a[3]+b[2]*c[4])

def ufunc_reduce(ufct,*vectors):
    vs = np.ix_(*vectors)
    r = ufct.identity
    for v in vs:
        r = ufct(r,v)
    return r
print(ufunc_reduce(np.add,a,b,c))
'''

'''
#11. Linear Algebra
import numpy as np
a = np.array([[1.0,2.0],[3.0,4.0]])
print(a)
print(a.transpose())
print(np.linalg.inv(a))
u = np.eye(2)
print(u)
j = np.array([[0.0,-1.0],[1.0,0.0]])
print(j @ j)
print(np.trace(u))
y = np.array([[5.],[7.]])
print(np.linalg.solve(a,y))
print(np.linalg.eig(j))
'''


#12. Tricks and Tips
#"Automatic" Reshaping
import numpy as np
a = np.arange(30)
a.shape = 2,-1,3 # -1 means "whatever is needed"
print(a.shape)
print(a)
# Vector Stacking
x = np.arange(0,10,2)   # x = ([0,2,4,6,8])
y = np.arange(5)        # y = ([0,1,2,3,4])
m = np.vstack([x,y])    # m = ([[0,2,4,6,8],
                        #   [0,1,2,3,4]])
xy = np.hstack([x,y])   # xy = ([0,2,4,6,8,0,1,2,3,4])

print(xy)
#Histograms(直方图)
import numpy as np
import matplotlib.pyplot as plt

#Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
mu,sigma = 2,0.5
v = np.random.normal(mu,sigma,10000)
#Plot a normalized histogram with 50 bins
plt.hist(v,bins=50,density=1)   #matplotlib version (plot)
plt.show()

#Compute the histogram with numpy and then plot it
(n,bins) = np.histogram(v,bins=50,density=True) #Numpy version(no plot)
plt.plot(.5*(bins[1:]+bins[:-1]),n)
plt.show()






























