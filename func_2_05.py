from collections import Counter

n = int(input())
numbers = [int(num) for num in range(1, n+1)]
def counter(numbers):
    res = []
    for num in numbers:
        res.append(sum(map(int, str(num))))
    count = Counter(res)
    # Находим максимальное количество повторений
    max_repetition = max(count.values())
    return max_repetition
print(counter(numbers))