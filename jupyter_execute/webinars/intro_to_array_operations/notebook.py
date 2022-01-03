#!/usr/bin/env python
# coding: utf-8

# # Introduction to Array Operations in Python
#
# ## Meenal Jhajharia

# ### Meenal Jhajharia. she/her.
#
# - CS and Math undergrad, University of Delhi
# - PyMC core contributor | GSoC student
# - Contact: [meenal@mjhajharia.com](mailto:meenal@mjhajharia.com) | [mjhajharia.com](https://mjhajharia.com)

# <figure style="display: table; margin: 0 auto">
#   <center>
#     <img src="banner.png" width="850vmin" style="padding: 4vmin 0 0 0">
#   </center>
# </figure>

# This banner is generated from [this code](https://raw.githubusercontent.com/pymc-devs/pymc-data-umbrella/main/banner.py), the code in this link is a trivial customization of the [original code](https://github.com/pymc-devs/pymcon/blob/gh-pages/assets/make_trajectories.py) by [Colin Caroll](https://colindcarroll.com/) who designed a [similar banner for pymcon’20](https://pymcon.com/), Colin is amazing at visualization stuff and even has a couple of talks about it!!

# Overview
#
# - Introduction
# - Python Objects
# - List Comprehension
# - Basics of NumPy

# #### Why Python?
#
# - Useful for quick prototyping
# - Dynamically Typed, Interpreted, High level data types
# - Large number of scientific open source software
#
# Best Place to learn more : [Official Python Tutorial](https://docs.python.org/3/tutorial/index.html)

# #### Let's get started!
#
# Here's what you need to begin
#
#
# - Github Repo: [pymc-devs/pymc-data-umbrella](https://github.com/pymc-devs/pymc-data-umbrella)
# - Working installation of Python3
# - A terminal (Windows or Unix)
# - Knowledge of an OOP would be nice to have

# <figure style="display: table; margin: 0 auto">
#   <center>
#     <img src="data_types.png" width="850vmin" style="padding: 4vmin 0 0 0">
#   </center>
# </figure>

# #### Numbers
#
# Certain numeric modules ship with Python

# In[1]:


import random
random.random()


# #### Strings
#
# Sequence Operations

# In[2]:


X = 'Data'
len(X)


# In[3]:


X[0:-2]


# #### Immutability
#
# Immutable objects cannot be changed

# In[4]:


X = 'Data'
X + 'Umbrella'


# In[5]:


X[0] = 'P'


# #### Polymorphism
#
# Operators or functions mean different things for different objects

# In[ ]:


1+2


# In[6]:


'Py'+'MC'


# Length or size means different things for different datatypes
#
#

# In[7]:


len("Python")


# In[8]:


len(["Python", "Java", "C"])


# In[9]:


len({"Language": "Python", "IDE": "VSCode"})


# Related: Class Polymorphism, Method Overriding and Inheritance

# #### Lists
#
# Positionally ordered collections of arbitrarily typed objects (mutable, no fixed size)

# In[10]:


L = ['Python', 45, 1.23]
len(L)


# In[11]:


L + [4, 5, 6]


# In[12]:


L[-1]


# List-specific operations

# In[13]:


L.append('Aesara');L


# In[14]:


L.pop(2); L


# More: sort(), reverse()

# List indexing and slicing

# In[15]:


L[99]


# In[16]:


X = [[1,2],[2,1]]
print(len(X), len(X[0]))


# In[17]:


X[0][0]


# In[18]:


L[:]


# In[19]:


L[-3:]


# In[20]:


L = [1,2,3,4,5,6,7,8,9,10]
L[1::2] #L[start:end:step_size]


# In[21]:


L[::-1]


# #### List Comprehension

# In[22]:


List = []

for character in 'Python':
    List.append(character)


# In[23]:


List = [character for character in 'Python']


# In[24]:


M = [['OS','Percentage of Users'],['Linux', '40'],['Windows', '20'], ['OSX','40']]


# In[25]:


[row[0] for row in M][1:]


# In[26]:


[row[0] + '*' for row in M][1:]


# In[27]:


[row[0] for row in M if row[0][0]!='O']


# Nested List Comprehension

# In[28]:


n = 3; [[ 1 if i==j else 0 for i in range(n) ] for j in range(n)]


# In[29]:


[x for x in range(21) if x%2==0 if x%3==0]


# Lambda Function

# In[30]:


[i*10 for i in range(10)]


# In[31]:


list(map(lambda i: i*10, [i for i in range(10)]))


# #### NumPy

# NumPy’s array class -> ndarray(array)
#
# - ndarray.ndim
# - ndarray.shape
# - ndarray.size

# In[32]:


import numpy as np

a = np.arange(16).reshape(4, 4)


# In[33]:


a


# Simple array operation

# In[34]:


2*a


# General Properties of ndarrays

# In[35]:


a.shape


# In[36]:


a.ndim


# In[37]:


a.size


# Ways to create new arrays
#
#

# In[38]:


a = np.array(['PyMC', 'Arviz', 'Aesara'])


# In[39]:


np.zeros((4, 4))


# In[40]:


np.ones((4, 4))


# Generate values in a certain range
#
#

# In[41]:


np.arange(1, 100, 10)


# #### Random Number Generator

# In[42]:


rg = np.random.default_rng(1)
x = rg.random(3);x


# Cumulative sum against specified axis (in this case only one axis is present)
#
#

# In[43]:


x.cumsum()


# Multi-dimensional arrays
#
#

# In[44]:


c = np.array([[[0,  1,  2],[ 10, 12, 13]],
[[100, 101, 102],[110, 112, 113]]])


# In[45]:


c.shape


# In[46]:


for row in c:
    print(row,'-')


# Element-wise printing
#
#

# In[47]:


for row in c.flat:
    print(row)


# Transpose

# In[48]:


c.T


# Reshape

# In[49]:


c.reshape((12,1))


# #### Stacking

# In[50]:


a = np.ones((2,2))
b = np.zeros((2,2))


# In[51]:


np.vstack((a, b))


# In[52]:


np.hstack((a, b))


# #### Broadcasting
#
# Used to deal with inputs that do not have exactly the same shape
#
# - If all input arrays do not have the same number of dimensions, a “1” will be repeatedly prepended to the shapes of the smaller arrays until all the arrays have the same number of dimensions.
#
# - Arrays with a size of 1 along a particular dimension act as if they had the size of the array with the largest shape along that dimension. The value of the array element is assumed to be the same along that dimension for the “broadcast” array.

# Arrays with same dimensions
#
#

# In[53]:


a = np.array([1, 2, 3])
b = np.array([3, 3, 3])
a*b


# 1-d Array and a Scalar
#
#

# In[54]:


a = np.array([1, 2, 3])
b = 3
a*b


# Intuitively: scalar b being "stretched" to same shape as a
#
# Reality:  broadcasting moves less memory around (computationally efficient)

# Arrays where dimensions aren’t exactly same, but are aligned along the leading dimension

# In[55]:


a = np.ones((5,2,3))
b = np.ones((2,3))
a*b


# Arrays where dimensions aren’t exactly same, but leading dimension is 1, so it works

# In[56]:


a = np.ones((5,2,1))
b = np.ones((2,3))
a*b


# Broadcasting fails!
#
#

# In[57]:


a = np.ones((5,2,2))
b = np.ones((2,3))
a*b


# NumPy compares shapes element-wise for two given arrays
#
# It starts with the trailing (i.e. rightmost) dimensions Two dimensions are compatible when
# - they are equal, or
# - one of them is 1
#
# Arrays do not need to have the same exact number of dimensions to be compatible. Broadcasting is a convenient way of taking the outer product (or any outer operation)
#
# Here broadcasting fails because of the mismatch of leading dimensions

# In[58]:


a = np.array([1,2,3,4])
b = np.array([1,2,3])
a*b


# We transpose a to reshape it along a new axix
#
#

# In[59]:


a = np.asarray([a]).T #a[:, np.newaxis]
a.shape


# Now it works!

# In[60]:


a*b


# #### Indexing

# In[61]:


a = np.array([0, 6, 9, 8, 8, 6, 2, 7, 2, 8, 1, 0, 4, 6, 9, 0])
i = np.array([1, 1, 2, 3])
a[i]


# In[62]:


j = np.array([[3, 0], [2, 1]])
a[j]


# In[63]:


print(a.shape, i.shape, j.shape)
a[i,j]


# In[64]:


a = a.reshape((4,4))
print(a.shape, i.shape, j.shape)
a[i,j]


# In[65]:


i = i.reshape((2,2))
print(a.shape, i.shape, j.shape)
a[i,j]


# Next thing to look at -> https://numpy.org/doc/stable/user/basics.html
#
# Note / Reference: A lot of the things here are modified/original versions of examples given in official Python or NumPy documentation, so that’s the best source to learn comprehensively, this is meant to be an accessible introduction!!
