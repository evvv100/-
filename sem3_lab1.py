import random

comp_number = random.randint(1, 20)
a = 0
count = 0
while True:
    a = input("Ваше число: ")
    if count==2:
        print("Количество попыток ограничено. Вы не угадали число.")
        break
    count += 1
    if not a.isdigit():
        print("Невозможно преобразовать строку в число, попробуйте снова.")
        continue
    a = int(a)
    if a==0 or a>20:
        print("Число не должно выходить за диапазон. Попробуйте снова.")
        continue
    if a<comp_number:
        print("Загаданное число больше. Попробуйте снова.")
    elif a>comp_number:
        print("Загаданное число меньше. Попробуйте снова.")
    elif a==comp_number:
        print(f"Вы угадали число {comp_number}. Количество попыток: {count}")
        break