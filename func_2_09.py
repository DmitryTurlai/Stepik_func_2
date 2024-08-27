slov = {}

with open('files.txt', 'r') as file:
    for line in file:
        values = line.strip().split()
        print (values)
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

        # Здесь вы можете обрабатывать полученные значения
sorted_keys = sorted(slov.keys())
sorted_slov = {key: slov[key] for key in sorted_keys}
print(sorted_slov)