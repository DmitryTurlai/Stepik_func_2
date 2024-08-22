import re

mails = ['ivan-petrov', 'petr-ivanov', 'ivan-petrov1',
         'ivan-ivanov', 'ivan-ivanov1', 'ivan-ivanov2']
n=6

new_personal = ['ivan-ivanov', 'petr-petrov', 'petr-ivanov']
m=3
res = []

#mails = []
#n = int(input())
#for i in range(n):
#    mails.append(input().split('@')[0])
#new_personal = []
#m = int(input())
#for i in range(m):
#    new_personal.append(input())
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
        return string, 0

def chek_number(n, mas_num):
    for i in range(1, n + 2):
        if i not in mas_num:
            return i

mas_num = []
for i in range(m):
    new_personal[i]

#for i in range(m):
#    print(res[i] + '@beegeek.bzz')

