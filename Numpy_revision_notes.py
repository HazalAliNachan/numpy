#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


a = np.array([10,20,30,40,50,60,70])
print(a)
print(type(a))


# In[9]:


b = np.array([[1,2],[3,4]])
print("2D Array:")
print(b)


# In[22]:


c = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("2D Array:")
print(c)

print("Shape:")
print(c.shape)



# In[24]:


print(c.ndim)


# In[21]:


d = np.array([[[1,2,3]],[[4,5,6]],[[7,8,9]]])
print("3D Array:")
print(d)

print("Shape:")
print(d.shape)


# In[19]:


print(d.ndim)


# In[26]:


c = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("2D Array:")
print(c)

print("Shape:")
print(c.shape)

print(c.dtype)
print(c.size)


# # SPECIAL ARRAYS

# In[27]:


np.zeros(5)


# In[28]:


np.ones(5)


# In[30]:


np.arange(1,11)


# In[31]:


np.linspace(0,10,5)


# # INDEXING AND SLICING 

# In[34]:


a = np.array([59,26,28,36,18])
print(a[0])
print(a[3])
print(a[-1])


# In[35]:


print(a[1:4])


# In[42]:


a = np.array([[1,2,3],[5,6,7]])
print(a[1,1])
print(a[0])
print(a[:,1])


# # DATATYPES AND CONVERSION

# In[43]:


a = np.array([1, 2, 3])
print(a.dtype)


# In[45]:


b = np.array([1.5, 2.5, 3.5])
print(b.dtype)


# In[46]:


a = np.array([1, 2, 3], dtype=float)
print(a)


# In[47]:


a = np.array([1.2, 2.8, 3.9])
b = a.astype(int)
print(b)


# # MATHEMATICAL OPERATION

# In[48]:


a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**2)


# # Aggregate & Statistical Functions

# In[54]:


marks = np.array([70, 80, 90, 60, 100])
print(np.min(marks))
print(np.max(marks))
print(np.mean(marks))
print(np.sum(marks))
print(np.std(marks))
print(np.var(marks))

print(np.argmax(marks)) # returns the index


# # LINEAR ALGEBRA

# In[63]:


A = np.array([
    [1,2],
    [3,4]
])
B = np.array([
    [3,6],
    [9,2]
])

print(A+B)


print(A*B)



# In[64]:


print(A@B) # MATRIX MULTIPLICATION

np.matmul(A, B)


# In[65]:


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.dot(a, b)


# In[71]:


A.T #TRANSPOSE


# In[72]:


print(A.transpose())


# # RESHAPING

# In[77]:


a = np.array([1, 2, 3, 4, 5, 6])
a.shape


# In[78]:


a.reshape(2,3)


# In[83]:


a.reshape(2, -1) #(-1)NumPy automatically calculates the missing dimension.


# # STACKING

# In[88]:


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.vstack((a,b))


# In[89]:


np.hstack((a,b))


# # Conditional Operations

# In[93]:


marks = np.array([35, 80, 45, 90, 20])
marks>50 #Boolean mask


# In[94]:


marks[marks>50]


# In[95]:


np.where(marks>50,"Pass","Fail")


# # BROADCASTING

# In[ ]:


#Broadcasting = NumPy automatically stretches dimensions of size 1 (or a scalar) so arrays can perform element-wise operations.
#Broadcasting means NumPy lets a smaller value/array participate in an operation with a bigger array by reusing its values wherever needed.


# In[117]:


a = np.array([1, 2, 3])
b = 10

print(a + b)  #NumPy reuses 10 for every element. We don't have to manually create [10, 10, 10]


# # RANDOM MODULE

# In[118]:


np.random


# In[119]:


np.random.rand() #Gives a random number between:0 and 1


# In[120]:


np.random.rand(5)


# In[121]:


np.random.randint(1,11)


# In[122]:


np.random.randint(1,11,size=5)


# In[123]:


np.random.randint(1,100,5)


# # FUNCTIONS

# In[124]:


a = np.array([30, 10, 50, 20])

np.sort(a)


# In[126]:


a = np.array([1, 2, 2, 3, 3, 3])

np.unique(a)


# In[134]:


a = np.array([[2,3],[1, 2]])
b = np.array([[4,7],[3, 4]])

# axis=0 → add rows ↓
# axis=1 → add columns →

np.concatenate((a, b),axis=0)




# In[135]:


np.concatenate((a, b),axis=1)


# In[136]:


a = np.array([
    [1, 2],
    [3, 4]
])

a.ravel() #Converts multidimensional array into 1D.


# In[137]:


a.flatten() #Converts multidimensional array into 1D.

