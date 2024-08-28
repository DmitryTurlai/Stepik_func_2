slov = {}

with open('files.txt', 'r') as file:
    for line in file:
        values = line.strip().split()
        parts = values[0].split('.', 1)
        key = parts[1]
        if values[2] == 'KB':
            values[1] = int(values[1]) * 1024
        elif values[2] == 'MB':
            values[1] = int(values[1]) * 1024 * 1024
        elif values[2] == 'GB':
            values[1] = int(values[1]) * 1024 * 1024 * 1024
        value = parts[0], int(values[1])
        if key in slov:
            slov[key].append(value)
        else:
            slov[key] = [value]


def transform_data(data):
    result = {}

    for key, value in data.items():
        words = []
        total_sum = 0

        for item in value:
            if isinstance(item, tuple):
                words.append(item[0])  # Добавляем слово
                total_sum += item[1]  # Добавляем число
            elif isinstance(item, list):
                for sub_item in item:
                    words.append(sub_item[0])  # Добавляем слово из списка
                    total_sum += sub_item[1]  # Добавляем число из списка
        words = sorted(words)
        result[key] = [words, total_sum]

    return result

def transfor_size_files(n):
    res = n
    count = 1
    while res > 1024:
        res = round(res/1024)
        count += 1
    if count == 1:
        res = str(res) + ' B'
    elif count == 2:
        res = str(res) + ' KB'
    elif count == 3:
        res = str(res) + ' MB'
    elif count == 4:
        res = str(res) + ' GB'
    return (res)


sorted_keys = sorted(slov.keys())
sorted_slov = {key: slov[key] for key in sorted_keys}

transformed_data = transform_data(sorted_slov)

for key, value in transformed_data.items():
    words_list = value[0]  # Список слов
    # Проходим по каждому слову в списке
    for item in words_list:
        print(f'{item}.{key}')  # Форматированный вывод
    print('----------')
    res = transfor_size_files(value[1])
    print(f'Summary: {res}')
    print()







