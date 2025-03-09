"""
Days from Today Calculator — A program for calculating the number of days 
between a given date and the current date.
"""

import datetime as dt

def get_days_from_today(date) -> str:                  # Обрала str, щоб потім перетворити на потрібний формат дати
    try:                                               # Вирішила використати try-except, щоб вивести повідомлення про помилку
        current_datetime = dt.datetime.today()
        date = dt.datetime.strptime(date, '%Y-%m-%d')
        return int((current_datetime - date).days)     # Задала int для виведення кількості днів цілим числом
    except Exception as e:                             # Використала Exception, як рекомендував вчитель, бо може бути як TypeError, так і ValueError
        return f'Error: {e}. Please, use YYYY-MM-DD and be sure format is string.'

print(get_days_from_today('2025-03-05'))               # Тестуємо на даті з минулого
print(get_days_from_today('2025-10-26'))               # Тестуємо на даті з майбутнього
print(get_days_from_today(dt.datetime.today()))        # Тестуємо на введені дати в форматі datetime
print(get_days_from_today(dt.datetime.today().strftime('%Y-%m-%d')))     # Тестуємо на сьогоднішній даті, попередньо перетворивши її в str
print(get_days_from_today('2025/03/05'))               # Тестуємо на некоректному форматі дати