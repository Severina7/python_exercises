#!/usr/bin/env python
# coding: utf-8

# #### 1.c. Create a jupyter notebook named import_exercises.ipynb. Use from to import the get_letter_grade function and give it an alias. Test this function in your notebook.

# In[2]:


from functions_exercises import get_letter_grade


# In[5]:


get_letter_grade(96)


# In[7]:


import itertools


# #### 2.

# - How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

# We can combine "abc" and "123" in 4 different ways: through a product, a permutation, a combination, or a combination with a replacement.

# In[32]:


#For product ABC and 123 need to be combined inside the same argument then associated to the iterative argument
itertools.product('ABCD123', repeat = 1)
list(itertools.product('ABCD123', repeat = 2))


# In[34]:


itertools.permutations('ABCD123', 2)
list(itertools.permutations('ABCD123', 2))


# In[37]:


itertools.combinations('ABCD123', 2)
list(itertools.combinations('ABCD123', 2))


# In[38]:


itertools.combinations_with_replacement('ABCD123', 2)
list(itertools.combinations_with_replacement('ABCD123', 2))


# - How many different combinations are there of 2 letters from "abcd"?

# In[39]:


itertools.combinations('ABCD', 2)
list(itertools.combinations('ABCD', 2))


# - How many different permutations are there of 2 letters from "abcd"?

# In[40]:


itertools.permutations('ABCD', 2)
list(itertools.permutations('ABCD', 2))


# In[ ]:




