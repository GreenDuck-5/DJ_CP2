#DJ, 1st, Library Notes


#in terminal
#pip install numpy
#pip install pandas
#pip install Faker

from faker import Faker
import pandas
import numpy as np
print(np.__version__)


#What is a library?
# A group of functions and classes that are availble for you to use
 
#What are some standard python libraries?
# Time, csv, random

#Why do we import other libraries? 
# The abilities have already been made, it makes to quicker and saves brainpower

#What information do you find in the documentaton for a library?
# The libraries pages through googlei

#What are good sources for tutorials on a library you have never used before?
# documention on the site, youtube videos


a = np.arange(15).reshape(3, 5)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
print(type(a))
b = np.array([6, 7, 8])
print(type(b))
