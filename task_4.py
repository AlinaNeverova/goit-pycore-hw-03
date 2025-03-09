"""
Upcoming Birthday Reminder — A program for determining upcoming birthdays with a shift 
to the next working day if the birthday falls on a weekend.
"""

import datetime as dt

def get_upcoming_birthdays(users) -> dict:        # Вказую, що список має бути у форматі словника із key-value
    upcoming_birthdays = []                       # Задаємо, що в результаті має бути список
    today = dt.datetime.today().date()

    for user in users:
        birthday = dt.datetime.strptime(user["birthday"], "%Y.%m.%d").date()  # Змінюємо формат з рядка на дату
        birthday_this_year = birthday.replace(year=today.year)                # Замінюємо рік народження на поточний
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)        # Якщо ДН вже пройшов, переносимо спрацювання функції на наступний рік
        days_to_birthday = (birthday_this_year - today).days
        if 0 <= days_to_birthday <= 7:                                        # Відняли кількість днів й задали поріг попередження
            if birthday_this_year.weekday() in [5, 6]:                        # Понеділок має індекс 0, тому вихідні припадають на 5 та 6
                birthday_this_year += dt.timedelta(days=(7 - birthday_this_year.weekday())) # Якщо ДН припадає на вихідний, знаходимо різницю між 7 й індексом дня та додаємо її до дати народження
            upcoming_birthdays.append({                                       # Якщо умова кількості днів виконана, задаємо вигляд списку з результатами
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.03.09"},   # Це Неділя
    {"name": "Ann Doe", "birthday": "1985.03.15"},    # Це Субота
    {"name": "Tim Smith", "birthday": "1985.03.08"},  # Цей ДН вже пройшов 
    {"name": "Jane Smith", "birthday": "1990.03.13"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print ('This week\'s congratulations:', upcoming_birthdays)     # Ну й використала \, щоб прийняло апостроф
