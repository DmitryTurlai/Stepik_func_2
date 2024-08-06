n = int(input())
word_list = []
for i in range(n):
    word_list += input().split(", ")
def language(n, word_list):
    word_dict = {word: word_list.count(word) for word in word_list}
    result_list = [word for word, count in word_dict.items() if count >= n]
    return result_list

if not language(n, word_list):
    print("Сериал снять не удастся")
else:
    sorted_word_list = sorted(language(n, word_list))
    print(*sorted_word_list, sep=", ")





