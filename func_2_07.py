word = input()
n = int(input())
word_list = []
#n = 8
#word = 'машина'
#word_list = ['сеть', 'машинист', 'дорога', 'урок', 'работа', 'аксиома', 'железо', 'ветеран']

for i in range(n):
    word_list.append(input())
def similar_words(n, word, word_list):
    res = []
    examp = 'ауоыиэяюёе'
    i=0
    res_count = []
    for char in word:
        i+=1
        if char in examp:
            res_count.append(i)
    for i in range(n):
        c=0
        res_count_1 = []
        for char in word_list[i]:
            c+=1
            if char in examp:
                res_count_1.append(c)
        if res_count_1 == res_count:
            res.append(word_list[i])
    return res

output = similar_words(n, word, word_list)

for w in output:
    print(w)
