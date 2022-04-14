{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "61c0781a",
   "metadata": {},
   "source": [
    "You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f0f2ded1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "27"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "The_little_mermaid = 3\n",
    "Brother_Bear = 5\n",
    "Hercules = 1\n",
    "\n",
    "Cost = (The_little_mermaid * 3) + (Brother_Bear * 3) + (Hercules * 3)\n",
    "Cost"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f3ec3cf1",
   "metadata": {},
   "source": [
    "Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8e449019",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7420"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Google = 400\n",
    "Amazon = 380\n",
    "Facebook = 350\n",
    "\n",
    "Weekly_pay = (Google * 6) + (Amazon * 4) + (Facebook * 10)\n",
    "Weekly_pay"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "03cebf3c",
   "metadata": {},
   "source": [
    "A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "02209eec",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "class_full = False\n",
    "class_empty = True\n",
    "empty_class_schedule_slots = True\n",
    "no_class_schedule_slots = False\n",
    "\n",
    "Enrolled = class_full and empty_class_schedule_slots\n",
    "Enrolled"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "03724983",
   "metadata": {},
   "source": [
    "A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "0aa680ed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "three_and_more_products_bought = True\n",
    "two_products_or_less_bought = False\n",
    "offer_present = True\n",
    "offer_expired = False\n",
    "premium = True\n",
    "\n",
    "get_promo = three_and_more_products_bought and offer_present\n",
    "get_promo"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "69b7c3da",
   "metadata": {},
   "source": [
    "- the password must be at least 5 characters\n",
    "- the username must be no more than 20 characters\n",
    "- the password must not be the same as the username\n",
    "- bonus neither the username or password can start or end with whitespace\n",
    "\n",
    "- username = 'codeup'\n",
    "- password = 'notastrongpassword'\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1d8f14d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "password_length = len(password) >= 5\n",
    "username_length = len(username) <= 20\n",
    "password_diff_username = username != password\n",
    "no_space_username = username.strip()\n",
    "no_space_password = password.strip()"
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
