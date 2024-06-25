a = input()
b = input()
c = input()

def letters(a, b, c):
    if ord(a) < 1000 and ord(b) < 1000 and ord(c) < 1000:
        res = 'en'
    elif ord(a) > 1000 and ord(b) > 1000 and ord(c) > 1000:
        res = 'ru'
    else:
        res = 'mix'
    return(res)

print(letters(a, b, c))