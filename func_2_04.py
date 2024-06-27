from collections import Counter

input_string = input()
# Преобразуем входную строку в список чисел
numbers = [int(num) for num in input_string.split()]

def count(numbers):
    # Подсчитываем количество вхождений каждого элемента в список
    counter = Counter(numbers)

    # Находим повторяющиеся элементы
    repeated_numbers = [num for num, count in counter.items() if count > 1]
    return sorted(repeated_numbers)

print(*count(numbers))