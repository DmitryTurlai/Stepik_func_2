import re

# mails = ['anri-tabuev1', 'arthur-kharisov3']
# n=2
#
# new_personal = ['anri-tabuev', 'anri-tabuev', 'arthur-kharisov', 'arthur-kharisov',
#                 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov',
#                 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov',
#                 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov']
# m=15
# res = []

mails = []
n = int(input())
for i in range(n):
    mails.append(input().split('@')[0])
new_personal = []
m = int(input())
for i in range(m):
    new_personal.append(input())
res = []
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
    count = 0
    for j in range(m):
        if text == new_personal[j]:
            count += 1
            if count == 1 and number != None:
                res.append(new_personal[j] + str(count))
            else:
                if count != number:
                    res.append(new_personal[j] + str(count))
                elif count == number:
                    res.append(new_personal[j] + str(count+1))
                    count += 1

for i in range(m):
    print(res[i] + '@beegeek.bzz')
