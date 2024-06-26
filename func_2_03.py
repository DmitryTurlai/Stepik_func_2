input_string = input()

# Преобразуем входную строку в список чисел
numbers = [int(num) for num in input_string.split()]
n = numbers[0]  # Количество элементов в основном списке
x = numbers[1]  # Начало первого диапазона (включительно)
y = numbers[2]  # Конец первого диапазона (включительно)
a = numbers[3]  # Начало второго диапазона (включительно)
b = numbers[4]  # Конец второго диапазона (включительно)


def flipper(n, x, y, a, b):
    # Создаем список от 1 до n
    data = [i for i in range(1, n + 1)]

    data[x-1:y] = data[x-1:y][::-1]
    data[a-1:b] = data[a-1:b][::-1]

    return data

print(*flipper(n, x, y, a, b))
