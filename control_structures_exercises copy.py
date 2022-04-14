{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "657fab0e",
   "metadata": {},
   "source": [
    "## Conditional Basics"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "129fd7d6",
   "metadata": {},
   "source": [
    "### a. Prompt the user for a day of the week, print out whether the day is Monday or not"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 461,
   "id": "cacf9e65",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a day of the week: abracadabra\n",
      "This is not Monday\n"
     ]
    }
   ],
   "source": [
    "Prompt = input('Enter a day of the week: ')\n",
    "if (Prompt.lower() in ['Monday', 'monday', 'mon']):\n",
    "    print('This is Monday')\n",
    "else:\n",
    "    print('This is not Monday')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "62f622cc",
   "metadata": {},
   "source": [
    "### b. Prompt the user for a day of the week, print out whether the day is a weekday or a weekend"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 462,
   "id": "2bca4231",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a day of the week: Cookies\n",
      "This is not a day of the week\n"
     ]
    }
   ],
   "source": [
    "Prompt = input('Enter a day of the week: ')\n",
    "if (Prompt.lower() in ['Saturday', 'Sat', 'Sunday', 'Sun']):\n",
    "    print('This is a weekend')\n",
    "elif (Prompt.lower() in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']):\n",
    "    print('This is a weekday')\n",
    "else:\n",
    "    print('This is not a day of the week')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1dee6b7f",
   "metadata": {},
   "source": [
    "### c. Create variables and make up values for\n",
    "\n",
    "- the number of hours worked in one week\n",
    "- the hourly rate\n",
    "- how much the week's paycheck will be\n",
    "- write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 470,
   "id": "7f748bb1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1800"
      ]
     },
     "execution_count": 470,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Weekly_hours = 40\n",
    "Hourly_rate = 45\n",
    "Overtime_rate = Hourly_rate * 1.5\n",
    "Weekly_overtime_hours = 45\n",
    "\n",
    "if Weekly_hours <= 40:\n",
    "    Weekly_paycheck = (Weekly_hours * Hourly_rate)\n",
    "elif Weekly_hours > 40:\n",
    "    Overtime = Weekly_overtime_hours - Weekly_hours\n",
    "    Weekly_paycheck = (Weekly_hours *  Hourly_rate) + (Overtime * Overtime_rate)\n",
    "Weekly_paycheck"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "43cb85c4",
   "metadata": {},
   "source": [
    "## Loop Basics"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8e4e4947",
   "metadata": {},
   "source": [
    "### a. While\n",
    "\n",
    "- Create an integer variable i with a value of 5.\n",
    "- Create a while loop that runs so long as i is less than or equal to 15\n",
    "- Each loop iteration, output the current value of i, then increment i by one."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 401,
   "id": "9fa04593",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n",
      "11\n",
      "12\n",
      "13\n",
      "14\n",
      "15\n"
     ]
    }
   ],
   "source": [
    "i = 5\n",
    "while i <= 15:\n",
    "    print(i)\n",
    "    i += 1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b38757e5",
   "metadata": {},
   "source": [
    "- Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.\n",
    "- Alter your loop to count backwards by 5's from 100 to -10.\n",
    "- Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 293,
   "id": "a678e48f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100 "
     ]
    }
   ],
   "source": [
    "i = 0\n",
    "while i <= 101:\n",
    "    print(i, end = ' ')\n",
    "    i += 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 294,
   "id": "771d5298",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100 95 90 85 80 75 70 65 60 55 50 45 40 35 30 25 20 15 10 5 0 -5 -10 "
     ]
    }
   ],
   "source": [
    "i = 100\n",
    "while i >= (-11):\n",
    "    print(i, end = ' ')\n",
    "    i += -5"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "42cc0af0",
   "metadata": {},
   "source": [
    "- Write a loop that uses print to create the output shown below."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "1c511a83",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "4\n",
      "16\n",
      "256\n",
      "65536\n"
     ]
    }
   ],
   "source": [
    "i = 2\n",
    "while i <= 100000:\n",
    "    print(i)\n",
    "    i *= i"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "66777804",
   "metadata": {},
   "source": [
    "- Create a for loop that uses print to create the output shown below."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 403,
   "id": "616cdd0d",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n",
      "95\n",
      "90\n",
      "85\n",
      "80\n",
      "75\n",
      "70\n",
      "65\n",
      "60\n",
      "55\n",
      "50\n",
      "45\n",
      "40\n",
      "35\n",
      "30\n",
      "25\n",
      "20\n",
      "15\n",
      "10\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "i = 100\n",
    "while i > (0):\n",
    "    print(i)\n",
    "    i += -5"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0168991c",
   "metadata": {},
   "source": [
    "### b. For Loops\n",
    "\n",
    "- Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "7e01bf5e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number: 7\n",
      "The Multiplication Table of:  7\n",
      "7 x 1 = 7\n",
      "7 x 2 = 14\n",
      "7 x 3 = 21\n",
      "7 x 4 = 28\n",
      "7 x 5 = 35\n",
      "7 x 6 = 42\n",
      "7 x 7 = 49\n",
      "7 x 8 = 56\n",
      "7 x 9 = 63\n",
      "7 x 10 = 70\n"
     ]
    }
   ],
   "source": [
    "Number = int(input('Enter a number: '))\n",
    "print(\"The Multiplication Table of: \", Number)\n",
    "for count in range(1, 11):      \n",
    "    print (Number, 'x', count, '=', Number * count)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f5571c2c",
   "metadata": {},
   "source": [
    "- Create a for loop that uses print to create the output shown below."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "2217ba72",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "1\n",
      "22\n",
      "333\n",
      "4444\n",
      "55555\n",
      "666666\n",
      "7777777\n",
      "88888888\n",
      "999999999\n"
     ]
    }
   ],
   "source": [
    "for x in (range(10)):\n",
    "    print(str(x) * x)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1343e594",
   "metadata": {},
   "source": [
    "### c. Break and Continue\n",
    "\n",
    "- Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 475,
   "id": "e17adc60",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter an odd number: 8\n",
      "Not an odd number or not in the range specified. \n",
      "Plz, enter an odd one\n",
      "Enter an odd number: 9\n",
      " The number to skip is  9\n",
      "Here is an odd number 1\n",
      "Here is an odd number 3\n",
      "Here is an odd number 5\n",
      "Here is an odd number 7\n",
      "Yikes, skipping this number 9\n",
      "Here is an odd number 11\n",
      "Here is an odd number 13\n",
      "Here is an odd number 15\n",
      "Here is an odd number 17\n",
      "Here is an odd number 19\n",
      "Here is an odd number 21\n",
      "Here is an odd number 23\n",
      "Here is an odd number 25\n",
      "Here is an odd number 27\n",
      "Here is an odd number 29\n",
      "Here is an odd number 31\n",
      "Here is an odd number 33\n",
      "Here is an odd number 35\n",
      "Here is an odd number 37\n",
      "Here is an odd number 39\n",
      "Here is an odd number 41\n",
      "Here is an odd number 43\n",
      "Here is an odd number 45\n",
      "Here is an odd number 47\n",
      "Here is an odd number 49\n"
     ]
    }
   ],
   "source": [
    "user_input = input('Enter an odd number: ')\n",
    "while True:\n",
    "    if user_input.isdigit() == False or int(user_input) > 50 or int(user_input) <= 0 or int(user_input) % 2 == 0:\n",
    "        print('Not an odd number or not in the range specified. \\nPlz, enter an odd one')\n",
    "        user_input = input('Enter an odd number: ')\n",
    "    else:\n",
    "        break\n",
    "user_input = int(user_input)\n",
    "print(' The number to skip is ', user_input)\n",
    "for x in range(1, 50):\n",
    "    if x % 2 == 0:\n",
    "        continue\n",
    "    elif x == user_input:\n",
    "        print('Yikes, skipping this number', x)\n",
    "    else:\n",
    "        print('Here is an odd number', x)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "52193a25",
   "metadata": {},
   "source": [
    "- The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 480,
   "id": "80ce8a6b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter a positive number: -9\n",
      "This is not a positive number\n",
      "Please enter a positive number: -345\n",
      "This is not a positive number\n",
      "Please enter a positive number: 6\n",
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "user_input = input('Please enter a positive number: ')\n",
    "while True:\n",
    "    if (user_input.isdigit() ==  False\n",
    "       or int(user_input) < 0):\n",
    "        print('This is not a positive number')\n",
    "        user_input = input('Please enter a positive number: ')\n",
    "    else:\n",
    "        break\n",
    "\n",
    "        \n",
    "for x in range(0, int(user_input) + 1):\n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "31cf8bd1",
   "metadata": {},
   "source": [
    "- Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d7b89533",
   "metadata": {},
   "source": [
    "## Fizzbuzz\n",
    "\n",
    "One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.\n",
    "\n",
    "- Write a program that prints the numbers from 1 to 100.\n",
    "- For multiples of three print \"Fizz\" instead of the number\n",
    "- For the multiples of five print \"Buzz\".\n",
    "- For numbers which are multiples of both three and five print \"FizzBuzz\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 291,
   "id": "25c018cc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 "
     ]
    }
   ],
   "source": [
    "for x in range(1, 101):\n",
    "    print(x, end=' ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 400,
   "id": "c6c3e4df",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "fizzbuzz 1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16 17 fizz 19 buzz fizz 22 23 fizz buzz 26 fizz 28 29 fizzbuzz 31 32 fizz 34 buzz fizz 37 38 fizz buzz 41 fizz 43 44 fizzbuzz 46 47 fizz 49 buzz fizz 52 53 fizz buzz 56 fizz 58 59 fizzbuzz 61 62 fizz 64 buzz fizz 67 68 fizz buzz 71 fizz 73 74 fizzbuzz 76 77 fizz 79 buzz fizz 82 83 fizz buzz 86 fizz 88 89 fizzbuzz 91 92 fizz 94 buzz fizz 97 98 fizz buzz "
     ]
    }
   ],
   "source": [
    "for fizzbuzz in range(101):\n",
    "    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:\n",
    "        print(\"fizzbuzz\", end = ' ')\n",
    "        continue\n",
    "    elif fizzbuzz % 3 == 0:\n",
    "        print(\"fizz\", end = ' ')\n",
    "        continue\n",
    "    elif fizzbuzz % 5 == 0:\n",
    "        print(\"buzz\", end = ' ')\n",
    "        continue\n",
    "    print(fizzbuzz, end = ' ')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3516eb4e",
   "metadata": {},
   "source": [
    "## Display a table of powers.\n",
    "\n",
    "- Prompt the user to enter an integer.\n",
    "- Display a table of squares and cubes from 1 to the value entered.\n",
    "- Ask if the user wants to continue.\n",
    "- Assume that the user will enter valid data.\n",
    "- Only continue if the user agrees to.\n",
    "#### Bonus: Research python's format string specifiers to align the table\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 533,
   "id": "b7a473b4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter an positive number: 3\n",
      "Here is your table!\n",
      "number|squared|cubed\n",
      "------|-------|-----\n",
      "  1 |    1  |   1\n",
      "  2 |    4  |   8\n",
      "  3 |    9  |   27\n",
      "If you want to continue, please enter yes or y:y\n",
      "Please enter an positive number: 5\n",
      "Here is your table!\n",
      "number|squared|cubed\n",
      "------|-------|-----\n",
      "  1 |    1  |   1\n",
      "  2 |    4  |   8\n",
      "  3 |    9  |   27\n",
      "  4 |    16  |   64\n",
      "  5 |    25  |   125\n",
      "If you want to continue, please enter yes or y:no\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    user_input = input('Please enter an positive number: ')\n",
    "    print('Here is your table!')\n",
    "    print('number|squared|cubed')\n",
    "    print('------|-------|-----')\n",
    "    user_input = int(user_input)\n",
    "    for i in range(1, user_input + 1):\n",
    "        print(f'  {i} |    {i ** 2}  |   {i ** 3}')\n",
    "    New_choice = input('If you want to continue, please enter yes or y:')\n",
    "    if New_choice.lower() in ['yes', 'y']:\n",
    "        continue\n",
    "    else:\n",
    "        break"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f244cf5a",
   "metadata": {},
   "source": [
    "## 5. Convert given number grades into letter grades.\n",
    "\n",
    "- Prompt the user for a numerical grade from 0 to 100.\n",
    "- Display the corresponding letter grade.\n",
    "- Prompt the user to continue.\n",
    "- Assume that the user will enter valid integers for the grades.\n",
    "- The application should only continue if the user agrees to.\n",
    "Grade Ranges:\n",
    "\n",
    "A : 100 - 88\n",
    "B : 87 - 80\n",
    "C : 79 - 67\n",
    "D : 66 - 60\n",
    "F : 59 - 0\n",
    "\n",
    "#### Bonus\n",
    "- Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 532,
   "id": "21905445",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter the numeric grade: 88\n",
      "A\n",
      "Do you want to continue? Please enter yes or y to continue:y\n",
      "Please enter the numeric grade: 55\n",
      "F\n",
      "Do you want to continue? Please enter yes or y to continue:no\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    grade_input = input('Please enter the numeric grade: ')\n",
    "    grade_input = int(grade_input)\n",
    "    if grade_input >= 88:\n",
    "        print('A')\n",
    "    elif grade_input >= 80:\n",
    "        print('B')\n",
    "    elif grade_input >= 67:\n",
    "        print('C')\n",
    "    elif grade_input >= 60:\n",
    "        print('D')\n",
    "    else:\n",
    "        print('F')\n",
    "        \n",
    "    New_choice = input('Do you want to continue? Please enter yes or y to continue:')\n",
    "    if New_choice.lower() in ['yes', 'y']:\n",
    "        continue\n",
    "    else:\n",
    "        break"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "97c5e49f",
   "metadata": {},
   "source": [
    "### 6. Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.\n",
    "\n",
    "### a. Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 592,
   "id": "a65c0acb",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " The book 20000 lieues sous les mers by author Jules Verne belongs to Science fiction\n",
      " The book Weapons of Math Destruction by author Cathy O'Neil belongs to Non-fiction\n",
      " The book Python Crash Course by author Eric Matthes belongs to Non-fiction\n",
      " The book 1984 by author George Orwell belongs to Dystopian fiction\n"
     ]
    }
   ],
   "source": [
    "Books_read = [\n",
    "    {\n",
    "        'title': '20000 lieues sous les mers',\n",
    "        'author': 'Jules Verne',\n",
    "        'genre': 'Science fiction'\n",
    "    },\n",
    "    {\n",
    "        'title': 'Weapons of Math Destruction',\n",
    "        'author': 'Cathy O\\'Neil',\n",
    "        'genre': 'Non-fiction'\n",
    "    },\n",
    "    {\n",
    "        'title': 'Python Crash Course',\n",
    "        'author': 'Eric Matthes',\n",
    "        'genre': 'Non-fiction'\n",
    "    },\n",
    "    {\n",
    "        'title': '1984',\n",
    "        'author': 'George Orwell',\n",
    "        'genre': 'Dystopian fiction'\n",
    "    }\n",
    "]\n",
    "for book in Books_read:\n",
    "    print(f\" The book {book['title']} by author {book['author']} belongs to {book['genre']}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 595,
   "id": "02448101",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please choose a genre: Non-fiction\n"
     ]
    }
   ],
   "source": [
    "user_input = input('Please choose a genre: ')\n",
    "for book in Books_read:\n",
    "    if user_input.lower() == book['genre']:\n",
    "        print(book['title'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f063d0be",
   "metadata": {},
   "outputs": [],
   "source": []
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
