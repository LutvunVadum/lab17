import pandas as pd

# Читання файлу matrix.txt
matrix = pd.read_csv('matrix.txt', sep=' ', header=None)

# Перетворення в серії
series_list = [matrix[col] for col in matrix.columns]

# Об'єднання всіх серій в один список
all_numbers = pd.concat(series_list)

# Пошук унікальних чисел
unique_numbers = all_numbers[all_numbers.duplicated(keep=False) == False]

# Запис унікальних чисел у файл un.txt
unique_numbers.to_csv('un.txt', index=False, header=False)

print("Унікальні числа збережено у файл un.txt.")