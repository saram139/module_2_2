first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))
if first == second and second == third:
    print("Одинаковых чисел:", 3)
elif first == second or second == third or first == third:
    print("Одинаковых чисел:", 2)
else:
    print("Одинаковых чисел:", 0)
