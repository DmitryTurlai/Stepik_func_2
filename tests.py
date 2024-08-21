import re

mails = ['ivan-ivanov', 'petr-petrov', 'petr-ivanov']
# mails = ['anri-tabuev1', 'arthur-kharisov3']

n = 6
# n = int(input())
# for i in range(n):
#    mails.append(input().split('@')[0])
new_personal = ['ivan-petrov', 'petr-ivanov', 'ivan-petrov1',
                'ivan-ivanov', 'ivan-ivanov1', 'ivan-ivanov2']
# new_personal = ['anri-tabuev', 'anri-tabuev', 'arthur-kharisov', 'arthur-kharisov',
#                'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov',
#                'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov',
#                'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov']
# m = int(input())
m = 3
# m=15
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

for i in range(m):
#    mails[i]
    mas_num = []
    for j in range(n):
        text, number = split_string_and_extract_number(new_personal[j])
        if text == mails[i]:
            mas_num.append(number)

    for j in range(m):
#        text, number = split_string_and_extract_number(new_personal[j])
        if mails[i] == mails[j] and i != j:
            num = chek_number(n, mas_num)
            if num != 0:
                res.append(mails[i] + str(num))
                mas_num.append(num)
            else:
                res.append(mails[i])

            #                 mas_num.append(num)


# for i in range(n):
#     mas_num = []
#     text, number = split_string_and_extract_number(new_personal[i])
#     print('Person=', text + str(number))
#     for her in range(m):
#         count = 0
#         text1, number1 = split_string_and_extract_number(mails[her])
#         #        print('chek text = ', text)
#         #        print(text1)
#         if text == text1:
#             #            print('bingo')
#             mas_num.append(number1)
#             mas_num.append(count)
#             count += 1
#     print('mas after mails =', mas_num)
#     for j in range(m):
#         if text == new_personal[j]:
#             num = chek_number(m, mas_num)
#             if num != 0:
#                 res.append(new_personal[j] + str(num))
#                 mas_num.append(num)
#             else:
#                 res.append(new_personal[j])
#                 mas_num.append(num)
#     print('mas after new =', mas_num)
print(res)
#for i in range(m):
#    print(res[i] + '@beegeek.bzz')




