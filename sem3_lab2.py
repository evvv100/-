import random

#шифрование
line = input("Введите строку: ")
arr = line.split(" ")
arr1 = arr[::-1]
while True:
    k = input("Введите число k: ")
    if k.isdigit():
        k = int(k)
        k = k%len(arr)
        break
    else:
        print("Ошибка ввода! Попробуйте снова.")
while True:
    m = input("Введите число m: ")
    if m.isdigit():
        m = int(m)
        break
    else:
        print("Ошибка ввода! Попробуйте снова.")
print(f"-Шифрование-")
print(f"1. Разделяем строку на массив строк: {arr}")
print(f"2. Меняем порядок слов на обратный: {arr1}")
arr2 = arr1[-k:]+arr1[:-k]
print(f"3. Делаем циклический сдвиг вправо на k: {arr2}")

for i in range(len(arr2)):
    x = arr2[i]
    if len(x)<=1:
        continue
    x1 = x[-1]
    x2 = x[0]
    x3 = x[1:-1]
    arr2[i] = x1+x3+x2
print(f"4. Меняем местами первую и последнюю букву каждой строки в массиве: {arr2}")

# ord('A') = 65 (код первой заглавной буквы)
# ord('Z') = 90 (код последней заглавной буквы)
# ord('a') = 97 (код первой строчной буквы)
# ord('z') = 122 (код последней строчной буквы)

for i in range (len(arr2)):
    x = arr2[i]
    new_x = ""
    for u in range(len(x)):
        symb = x[u]
        if symb.isalpha():
            if symb.isupper():
                kod = (ord(symb) - ord('A') + m) % 26 + ord('A')
            else:
                kod = (ord(symb) - ord('a') + m) % 26 + ord('a')
            new_x += chr(kod)
        else:
            new_x += symb
    arr2[i] = new_x
print(f"5. Делаем циклический сдвиг на m позиций по номеру позиции буквы в алфавите (шифр Цезаря): {arr2}")
new_line = " ".join(arr2)
print(f"6. Соединяем строки через пробел в переменную new_line: {new_line}")
dict1 = {}
new_dict = {}
print(f"7. Создаем два словаря: dict1 для добавления случайных трехзначных ключей и new_dict для того, чтобы убрать повторяющиеся буквы в словаре dict1.")
for i in range(len(new_line)):
    while True:
        c = random.randint(100, 999)
        if c not in dict1:
            dict1[new_line[i]] = c
            break
print(f"8. Заполняем словарь dict1, ключи - символы строки new_line: {dict1}")
new_dict = {v: l for l, v in dict1.items()}
print(f"9. Меняем местами ключи и значения, записываем это в словарь new_dict, повторяющиеся символы записываются только 1 раз: {new_dict}")

line1 = "".join(str(dict1[char]) for char in new_line)
print(f"10. Создаем строку line1, записываем в нее уже зашифрованные коды вместе с пробелами с помощью генератора: {line1}")

final = int(line1)
print(f"11. Конвертируем строку в целом число: {final}")
#дешифрование
text = str(final)
print(f"-Дешифрование-")
print(f"1. Конвертируем целое число в строку: {text}")

dtesh = "".join(str(new_dict[int(text[i:i+3])]) for i in range(0, len(text), 3) if int(text[i:i+3]) in new_dict)
print(f"2. Создаем строку dtesh, записываем в нее расшифрованные символы с помощью перевернутого словаря new_dict: {dtesh}")
dtesh_arr = dtesh.split(" ")
print(f"3. Разделяем строку на массив строк и записываем в dtesh_arr: {dtesh_arr}")
for i in range (len(dtesh_arr)):
    x = dtesh_arr[i]
    new_x = ""
    for u in range(len(x)):
        symb = x[u]
        if symb.isalpha():
            if symb.isupper():
                kod = (ord(symb) - ord('A') - m) % 26 + ord('A')
            else:
                kod = (ord(symb) - ord('a') - m) % 26 + ord('a')
            new_x += chr(kod)
        else:
            new_x += symb
    dtesh_arr[i] = new_x
print(f"4. Делаем циклический сдвиг влево на m символов строки каждого элемента массива: {dtesh_arr}")
dtesh_arr2 = dtesh_arr[int(k):]+dtesh_arr[:int(k)]
print(f"5. Делаем циклический сдвиг влево на k каждого элемента массива: {dtesh_arr2}")
for i in range(len(dtesh_arr2)):
    x = dtesh_arr2[i]
    if len(x)<=1:
        continue
    x1 = x[-1]
    x2 = x[0]
    x3 = x[1:-1]
    dtesh_arr2[i] = x1+x3+x2
print(f"6. Меняем местами первый и последний символ каждой строки: {dtesh_arr2}")
dtesh_arr3 = dtesh_arr2[::-1]
print(f"7. Переворачиваем порядок слов: {dtesh_arr3}")
final_line = " ".join(dtesh_arr3)
print(f"8. Соединяем все строки в одну строку final_line: {final_line}")



