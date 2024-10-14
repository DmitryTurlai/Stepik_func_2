from datetime import datetime
def read_file_to_dict(filename):
    result = {}

    with open(filename, 'r', encoding='utf-8') as file:
        key = None
        value_lines = []

        for line in file:
            line = line.strip()  # Убираем пробелы и символы новой строки
            if line:  # Если строка не пустая
                if key is None:
                    key = datetime.strptime(line.replace(';', ' '),'%d.%m.%Y %H:%M') # Устанавливаем ключ
                else:
                    value_lines.append(line)  # Собираем строки значения
            else:  # Если строка пустая, сохраняем значение и сбрасываем
                if key is not None:
                    result[key] = '\n'.join(value_lines)  # Сохраняем в словарь
                    key = None  # Сбрасываем ключ
                    value_lines = []  # Сбрасываем значения

        # Сохраняем последнюю пару ключ-значение, если файл не заканчивается пустой строкой
        if key is not None:
            result[key] = '\n'.join(value_lines)

    return result


# Пример использования
filename = 'diary.txt'  # Укажите имя вашего файла
data_dict = read_file_to_dict(filename)
sorted_data = dict(sorted(data_dict.items()))

# Вывод результата
for k, v in sorted_data.items():
    print(f"{k.strftime('%d.%m.%Y; %H:%M')}\n{v}\n")
#print(data_dict)