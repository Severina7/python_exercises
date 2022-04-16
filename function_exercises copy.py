{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d9863ace",
   "metadata": {},
   "source": [
    "### "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fed6e898",
   "metadata": {},
   "source": [
    "### Function Exercises"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "310194cc",
   "metadata": {},
   "source": [
    "1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "103599e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "def is_two(x):\n",
    "    if x == 2 or x == '2':\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "print(is_two('mango'))\n",
    "print(is_two(2))\n",
    "print(is_two(2.0))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "119ddcc9",
   "metadata": {},
   "source": [
    "2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "id": "402c5e0e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n",
      "False\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "def is_vowel(letter):\n",
    "    if letter in ('a', 'e', 'i', 'o' , 'u'):\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "print(is_vowel('a'))\n",
    "print(is_vowel('x'))\n",
    "print(is_vowel('aeiou'))\n",
    "print(is_vowel('m'))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8ee5a974",
   "metadata": {},
   "source": [
    "3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "15cc5882",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "def is_consonant(letter):\n",
    "    if letter not in ('a', 'e', 'i', 'o' , 'u'):\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "print(is_consonant('a'))\n",
    "print(is_consonant('n'))\n",
    "print(is_consonant('mnlop'))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7a802f12",
   "metadata": {},
   "source": [
    "4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "id": "71f3d1e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "Bool\n",
      "Mesmerize\n"
     ]
    }
   ],
   "source": [
    "def first_letter_capitalization(word):\n",
    "    if type(word) != str:\n",
    "        return False\n",
    "    first_letter = word[0]\n",
    "    if first_letter not in ('a', 'e', 'i', 'o' , 'u'):\n",
    "        return word.capitalize()\n",
    "print(first_letter_capitalization(10))\n",
    "print(first_letter_capitalization('bool'))\n",
    "print(first_letter_capitalization('mesmerize'))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "678f3b1c",
   "metadata": {},
   "source": [
    "5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "id": "aef6f517",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.0\n",
      "4.5\n",
      "False\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "def calculate_tip(x, y):\n",
    "    if x <0 or x > 1:\n",
    "        return False\n",
    "    if (type(x) == float) and (type(y) == int):\n",
    "        calculate_tip = y * x\n",
    "        return calculate_tip\n",
    "print(calculate_tip(0.2, 15))\n",
    "print(calculate_tip(0.3, 15))\n",
    "print(calculate_tip(4, 15))\n",
    "print(calculate_tip(1.5, 15))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6bc785b2",
   "metadata": {},
   "source": [
    "6. Define a function named apply_discount. It should accept an original price, and a discount percentage, and return the price after the discount is applied."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "eb657d8f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "326.25"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def apply_discount(price, discount_percentage):\n",
    "    if (type(price) == int) and (type(discount_percentage) == float):\n",
    "        discount = price * discount_percentage\n",
    "        return price - discount\n",
    "    \n",
    "apply_discount(435, 0.25)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5cb88d53",
   "metadata": {},
   "source": [
    "7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "c2f0f265",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "def handle_commas(thousands):\n",
    "    if type(thousands) != str:\n",
    "        return False\n",
    "    thousands = thousands.replace(',', '')\n",
    "    if thousands.isdigit():\n",
    "        return thousands\n",
    "    else:\n",
    "        return False\n",
    "print(handle_commas(25000))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e77e0440",
   "metadata": {},
   "source": [
    "8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "dd794b74",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your grade is: F\n",
      "Your grade is: A\n"
     ]
    }
   ],
   "source": [
    "def get_letter_grade(grade):\n",
    "    if type(grade) == int or type(grade) == float:\n",
    "        if grade >= 92.5:\n",
    "            return ('Your grade is: A')\n",
    "        elif grade >= 82.5:\n",
    "            return ('Your grade is: B')\n",
    "        elif grade >= 72.5:\n",
    "            return ('Your grade is: C')\n",
    "        elif grade >= 62.5:\n",
    "            return ('Your grade is: D')\n",
    "        elif grade >= 52.5:\n",
    "            return ('Your grade is: E')\n",
    "        elif grade < 52.5:\n",
    "            return ('Your grade is: F')\n",
    "        else:\n",
    "            return False\n",
    "print(get_letter_grade(50))\n",
    "print(get_letter_grade(95.5))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8470ed76",
   "metadata": {},
   "source": [
    "9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "bbd9595f",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'new_word' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/5k/zptdym41293159jft7y2b6cm0000gp/T/ipykernel_10373/1950578242.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      7\u001b[0m             \u001b[0mnew_word\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0mletter\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mnew_word\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 9\u001b[0;31m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnew_word\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'6'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'new_word' is not defined"
     ]
    }
   ],
   "source": [
    "def remove_vowels(word):\n",
    "    if type(word) != str:\n",
    "        return False\n",
    "    new_word = ''\n",
    "    for letter in word:\n",
    "        if letter not in ['a', 'e', 'i', 'o' , 'u']:\n",
    "            new_word += letter\n",
    "    return new_word\n",
    "print(new_word('banana'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "a986d913",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "bnn\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "def remove_vowel(a):\n",
    "    vowels = ['a', 'e', 'i', 'o' , 'u']\n",
    "    s = ''\n",
    "    if type(a) == str:\n",
    "        for i in a.lower():\n",
    "            if i not in vowels:\n",
    "                s = s + i\n",
    "        return s\n",
    "print(remove_vowel('banana'))\n",
    "print(remove_vowel(5000))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9fd4751a",
   "metadata": {},
   "source": [
    "10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:\n",
    "- anything that is not a valid python identifier should be removed\n",
    "- leading and trailing whitespace should be removed\n",
    "- everything should be lowercase\n",
    "- spaces should be replaced with underscores\n",
    "- for example:\n",
    "    - Name will become name\n",
    "    - First Name will become first_name\n",
    "    - % Completed will become completed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "b93b51dd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "rickymajestical\n"
     ]
    }
   ],
   "source": [
    "def normalize_name(weird_word):\n",
    "    output = ''\n",
    "    weird_word = weird_word.lower()\n",
    "    for character in weird_word:\n",
    "        if character.isidentifier() or character == ' ':\n",
    "            output += character\n",
    "    output = output.strip()\n",
    "    output = output.replace(' ', '_')\n",
    "    return output\n",
    "print(normalize_name(\"  Ricky@majestical !   \"))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b01b560f",
   "metadata": {},
   "source": [
    "11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.\n",
    "- cumulative_sum([1, 1, 1]) returns [1, 2, 3]\n",
    "- cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "id": "0c20e534",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 3, 6, 10]\n"
     ]
    }
   ],
   "source": [
    "def cumulative_sum(somenums):\n",
    "    output = []\n",
    "    for x, num in enumerate(somenums):\n",
    "        sum_so_far = sum(somenums[:i + 1])\n",
    "        output.append(sum_so_far)\n",
    "    return output\n",
    "\n",
    "def cumulative_sum(lists):\n",
    "    cumulative_sum = []\n",
    "    length = len(lists)\n",
    "    cumulative_sum = [sum(lists[0:x:1]) for x in range(0, length+1)]\n",
    "    return cumulative_sum[1:]\n",
    "lists = [1, 2, 3, 4]\n",
    "print(cumulative_sum(lists))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
