#!/usr/bin/env python
# coding: utf-8

# Que1. Write a RegEx pattern in python program to check that a string 
# contains only a certain set of characters (in this case a-z, A-Z and 0-9).

# In[27]:


import re
string = "Hello Fliprobo 123"
result = re.findall("[^A-Za-z0-9|\s]",string)
if result:
    print("this string contains",result)
else:
    print("this string don't contain any special character it contains  only a-z, A-Z and 0-9")


# Question 2- Write a RegEx pattern that matches a string that has an a followed by zero or more b's
# 
# 

# In[3]:


pattern2 = '^a(b*)$'
result_2 = re.search(pattern2, "abb")
print(result_2)
if re.search(pattern2, "abb"):
    print('Found a match contains b at end of string')
else:
    print("zero b's at end of string")


# Question 3-  Write a RegEx pattern that matches a string that has an a followed by one or more b's

# In[4]:


pattern3 = 'a(b+)$'
result_3 = re.search(pattern3, "ac")
print(result_3)
if re.search(pattern3, "ac"):
     print('Found a match contains one or more  b at end of string')
else:
    print("no b at end of string")


# Question 4- Write a RegEx pattern that matches a string that has an a followed by zero or one 'b'

# In[5]:


pattern4 = '(ab+?)$'
result_4 = re.search(pattern4, "abb")
print(result_4)


# Question 5- Write a RegEx pattern in python program that matches a string that has an a followed by three 'b'.
# 
# 

# In[6]:


pattern5 = 'ab{3}?'
result_5 = re.search(pattern5, "abcabbb1")
print(result_5)


# Question 6- Write a RegEx pattern in python program that matches a string that has an a followed by two to three 'b'.

# In[7]:


pattern6 = 'ab{2,3}'
result_6 = re.search(pattern6, "abb1")
print(result_6)


# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'
# 
# 

# In[14]:


pattern7 = 'a.*.?b$'
result_7 = re.search(pattern7,"agbb")
print(result_7)


# Question 8- Write a RegEx pattern in python program that matches a word at the beginning of a string.

# In[16]:


pattern8 = '^\w+'
result_8 =re.search(pattern8,"abcdsfds sdve")
print(result_8)


# Question 9- Write a RegEx pattern in python program that matches a word at the end of a string.

# In[23]:


pattern9 = '\w+$'
result_9 =re.search(pattern9,"abc dsfds sdve")
print(result_9)


# Question 10- Write a RegEx pattern in python program to find all words that are 4 digits long in a string.
# Sample text- '01 0132 231875 1458 301 2725.'
# Expected output- ['0132', '1458', '2725']
# 

# In[52]:


string1 = "Hello Fliprobo 123 1234"
result9 = re.findall(r"\b\w{4}\b",string1)
print(result9)
if result9:
    print("this string contains",result9)


# In[ ]:




