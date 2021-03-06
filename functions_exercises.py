#!/usr/bin/env python
# coding: utf-8

# ### 

# ### Function Exercises

# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[5]:


def is_two(x):
    if x == 2 or x == '2':
        return True
    else:
        return False
# print(is_two('mango'))
# print(is_two(2))
# print(is_two(2.0))


# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[142]:


def is_vowel(letter):
    if letter in ('a', 'e', 'i', 'o' , 'u'):
        return True
    else:
        return False
# print(is_vowel('a'))
# print(is_vowel('x'))
# print(is_vowel('aeiou'))
# print(is_vowel('m'))


# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[49]:


def is_consonant(letter):
    if letter not in ('a', 'e', 'i', 'o' , 'u'):
        return True
    else:
        return False
# print(is_consonant('a'))
# print(is_consonant('n'))
# print(is_consonant('mnlop'))


# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[178]:


def first_letter_capitalization(word):
    if type(word) != str:
        return False
    first_letter = word[0]
    if first_letter not in ('a', 'e', 'i', 'o' , 'u'):
        return word.capitalize()
# print(first_letter_capitalization(10))
# print(first_letter_capitalization('bool'))
# print(first_letter_capitalization('mesmerize'))


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[179]:


def calculate_tip(x, y):
    if x <0 or x > 1:
        return False
    if (type(x) == float) and (type(y) == int):
        calculate_tip = y * x
        return calculate_tip
# print(calculate_tip(0.2, 15))
# print(calculate_tip(0.3, 15))
# print(calculate_tip(4, 15))
# print(calculate_tip(1.5, 15))


# 6. Define a function named apply_discount. It should accept an original price, and a discount percentage, and return the price after the discount is applied.

# In[72]:


def apply_discount(price, discount_percentage):
    if (type(price) == int) and (type(discount_percentage) == float):
        discount = price * discount_percentage
        return price - discount
    
# apply_discount(435, 0.25)


# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[85]:


def handle_commas(thousands):
    if type(thousands) != str:
        return False
    thousands = thousands.replace(',', '')
    if thousands.isdigit():
        return thousands
    else:
        return False
# print(handle_commas(25000))


# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[10]:


def get_letter_grade(grade):
    if type(grade) == int or type(grade) == float:
        if grade >= 92.5:
            return ('Your grade is: A')
        elif grade >= 82.5:
            return ('Your grade is: B')
        elif grade >= 72.5:
            return ('Your grade is: C')
        elif grade >= 62.5:
            return ('Your grade is: D')
        elif grade >= 52.5:
            return ('Your grade is: E')
        elif grade < 52.5:
            return ('Your grade is: F')
        else:
            return False
# print(get_letter_grade(50))
# print(get_letter_grade(95.5))


# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[60]:


def remove_vowel(a):
    vowels = ['a', 'e', 'i', 'o' , 'u']
    s = ''
    if type(a) == str:
        for i in a.lower():
            if i not in vowels:
                s = s + i
        return s
# print(remove_vowel('banana'))
# print(remove_vowel(5000))


# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores
# - for example:
#     - Name will become name
#     - First Name will become first_name
#     - % Completed will become completed

# In[61]:


def normalize_name(weird_word):
    new_word = ''
    weird_word = weird_word.lower()
    for character in weird_word:
        if character.isidentifier() or character == ' ':
            new_word += character
    new_word = new_word.strip()
    new_word = new_word.replace(' ', '_')
    return new_word
# print(normalize_name("  Ricky@majestical !   "))


# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# In[62]:


def cumulative_sum(lists):
    cumulative_sum = []
    length = len(lists)
    cumulative_sum = [sum(lists[0:x:1]) for x in range(0, length+1)]
    return cumulative_sum[1:]
# lists = [1, 2, 3, 4]
# print(cumulative_sum(lists))


# In[ ]:




