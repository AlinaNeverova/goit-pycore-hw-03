"""
Phone Number Normalizer — A program for standardizing phone numbers 
to the correct format for SMS campaigns.
"""

import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r"[^\d+]", "", phone_number)                 # Видаляємо всі символи, крім цифр та знаку + за рахунок квадратних дужок
    return (                                                             # Вирішила записати умови тернарним виразом, щоб максимально спростити синтаксис
        "+" + cleaned_number if cleaned_number.startswith("380") else
        "+3" + cleaned_number if cleaned_number.startswith("8") else     # Дехто все ще пише номер через вісімку, тому додала цю умову
        "+38" + cleaned_number if cleaned_number.startswith("0") else
        str(cleaned_number)                                              # Повертаємо як string, бо за умовою задачі має бути рядок
    )

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print('Normalised phone numbers for SMS campaigns:', sanitized_numbers)
