import numpy as np

# ex.2_1
a = np.zeros(10)
print(a)

# ex.2_2
b = np.ones(10)
print(b)

# ex.2_3
c = 5 * np.ones(10)
print(c)

# ex.2_4
d = np.arange(10,51)
print(d)

# ex.2_5
e = np.arange(10,51,2)
print(e)

# ex.2_6
f = np.arange(9).reshape((3,3))
print(f)

# ex.2_7
g = np.eye(3)
print(g)

# ex.2_8
h = np.random.random()
print(h)

# ex.2_9
i = np.random.randn(25)
print(i)

# ex.2_10
j = 0.01 * np.arange(1,101).reshape((10,10))
print(j)

# ex.2_11
k = np.linspace(0,1,20)
print(k)

# ex.2_12
mat = np.arange(1,26).reshape(5,5)
print(mat)
print(mat[:,4])
print(mat[2:,1:])
print(mat[-2,-1])
print(np.asarray(mat[:3,1:2]))
print(mat[4,:])
print(mat[-2:,:])
print(np.sum(mat))
print(np.std(mat))
print(np.sum(mat, axis=0))
