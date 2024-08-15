import re

mails = []
n = int(input())
for i in range(n):
    mails.append(input().split('@')[0])
new_personal = []
m = int(input())
res = []
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
        return string, None

for i in range(n):
    text, number = split_string_and_extract_number(mails[i])

for i in range(m):
    for j in range(n):
        count = 0
        if new_personal[i] == mails[j] or new_personal[i].startswith(mails[j]):
            count += 1
        elif new_personal[i] != mails[j] and new_personal[i].startswith(mails[j]):
            if mails[j][-1] != 1:

    if count == 0:
        res.append(new_personal[i] + '@beegeek.bzz')
    elif count > 0:

#    mails.append(new_personal[i])
for i in range(m):
    print(res[i])
