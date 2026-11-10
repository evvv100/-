import numpy as np
import random as rnd

while True:
    N = str(input("Введите число N: "))
    if not N.isdigit():
        print("Это не целое число!")
    else:
        N = int(N)
        break
while True:
    M = str(input("Введите число M: "))
    if not M.isdigit():
        print("Это не целое число!")
    else:
        M = int(M)
        break

arr = np.full((N, M), ' ')
arr[:, 0] = '#'
arr[0, :] = '#'
arr[-1, :] = '#'
arr[:, -1] = '#'
steps = 0

def show():
    for row in arr:
        print("".join(row))
    print()

def divide_room(x1, y1, x2, y2):
    global steps
    if x2 - x1 + 1 < 3 or y2 - y1 + 1 < 3:
        return

    if x2 - x1 >= y2 - y1:
        wall = rnd.randrange(x1 + 1, x2, 2)
        passage = rnd.randrange(y1, y2 + 1, 2)

        arr[y1 : y2 + 1, wall] = '#'
        arr[passage, wall] = ' '
        # |
        steps += 1
        print(f"Шаг {steps}: добавляем стену по вертикали, x={wall}, проход y={passage}")
        show()
        divide_room(x1, y1, wall-1, y2)
        divide_room(wall+1, y1, x2, y2)
    else:
        wall = rnd.randrange(y1 + 1, y2, 2)
        passage = rnd.randrange(x1, x2 + 1, 2)
        arr[wall, x1:x2 + 1] = '#'
        arr[wall, passage] = ' '
        # _
        steps += 1
        print(f"Шаг {steps}: добавляем стену по горизонтали, y={wall}, проход x={passage}")
        show()
        divide_room(x1, y1, x2, wall - 1)
        divide_room(x1, wall + 1, x2, y2)
print("Шаг 0: начальное состояние")
show()

divide_room(1, 1, M - 2, N - 2)