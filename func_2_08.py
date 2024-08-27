import re

mails = []
n = int(input())
for i in range(n):
    mails.append(input().split('@')[0])
new_personal = []
m = int(input())
for i in range(m):
    new_personal.append(input())
def split_string_and_extract_number(string):
    # Используем регулярное выражение для разделения строки на текстовую часть и число
    pattern = r"(\D+)(\d+)"
    match = re.match(pattern, string)
    if match:
        text_part = match.group(1).strip()
        number_part = int(match.group(2))
        return text_part, number_part
    else:
        return string, 0

def chek_number(m, mas_num):
    for i in range(1, m + 2):
        if i not in mas_num:
            return i
def find_and_add_missing_number(d, key):
    if key in d:
        # Получаем список значений, связанных с ключом
        values = d[key]

        # Создаем список из чисел от 1 до максимального значения в списке + 1
        all_numbers = list(range(0, max(values) + 2))

        # Находим разницу между всеми числами и значениями в списке
        missing_number = next((n for n in all_numbers if n not in values), None)

        if missing_number is not None:
            # Добавляем недостающее число в список
            d[key].append(missing_number)
            return missing_number
        else:
            return None
    else:
        # Если ключа нет, создаем новую пару ключ-значение
        d[key] = [0]
        return 0

slov_num = {}
for i in range(n):
    text, number = split_string_and_extract_number(mails[i])
    if text in slov_num:
        slov_num[text].extend([number])
    else:
        slov_num[text] = [number]

for i in range(m):
    n = find_and_add_missing_number(slov_num, new_personal[i])
    if n > 0:
        new_personal[i] = new_personal[i] + str(n)

for i in range(m):
    print(new_personal[i] + '@beegeek.bzz')