"""
Lottery Ticket Generator — A program for generating a unique set of 
random numbers for a lottery ticket.
"""

import random

def get_numbers_ticket(min, max, quantity) -> list:            # Задала формат списку за умовою
   if not (1 <= min <= max <= 1000) \
        or quantity <= 0 \
        or quantity > (max - min + 1):
        return []                                              # Використала "Якщо не", щоб спростити синтаксис й перерахувати всі умови
   return sorted(random.sample(range(min, max + 1), quantity)) # Якщо дані введено коректно, то повертається одразу відсортований список
   
lottery_numbers = get_numbers_ticket(43, 75, 6)
print(f'Your lottery numbers: {lottery_numbers}')
