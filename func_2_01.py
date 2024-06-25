a = int(input())
b = int(input())
c = int(input())
def distance(a, b, c):
    return min(2 * a + 2 * b, a + c + b, 2 * a + 2 * c, 2 * c + 2 * b)

print(distance(a, b, c))