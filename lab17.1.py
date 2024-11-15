import pandas as pd

# 1. Зчитування таблиці з файлу mark.csv
try:
    df = pd.read_csv('mark.csv')

    # 2. Обчислення середньої оцінки за сесію
    df['Average'] = df.iloc[:, 1:].mean(axis=1)

    # 3. Запит прізвища студента і виведення середньої оцінки
    student_name = input("Введіть прізвище студента: ")
    if student_name in df.iloc[:, 0].values:
        avg_mark = df.loc[df.iloc[:, 0] == student_name, 'Average'].values[0]
        print(f"Середня оцінка студента {student_name}: {avg_mark:.2f}")
    else:
        print("Студента з таким прізвищем немає в таблиці.")

except FileNotFoundError:
    print("Файл mark.csv не знайдено. Переконайтесь, що файл знаходиться в тому ж каталозі, що й програма.")
except Exception as e:
    print(f"Сталася помилка: {e}")