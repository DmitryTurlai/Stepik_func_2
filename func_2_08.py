mails = []
n = int(input())
for i in range(n):
    mails.append(input().split('@')[0])
new_personal = []
m = int(input())
res = []
for i in range(m):
    new_personal.append(input())
#    count = 0
#    for item in mails:
#        if new_personal[i] in item:
#            count += 1
#    if count > 0:
#        res.append(new_personal[i] + str(count) + '@beegeek.bzz')
#    elif count == 0:
#        res.append(new_personal[i] + '@beegeek.bzz')
for i in range(m):
    for j in range(n):
        count = 0
        if new_personal[i] == mails[j]:
            count += 1
        elif new_personal[i].startswith(mails[j]):
            res.append(new_personal[i] + '@beegeek.bzz')
#    mails.append(new_personal[i])
for i in range(m):
    print(res[i])

#def is_prefix(string, prefix):
#    return string == prefix or string.startswith(prefix)

#print(is_prefix("hello world", "hello"))  # True
#print(is_prefix("hello world", "world"))  # False
#print(is_prefix("hello", "hello"))  # True