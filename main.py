# 1
n = int(input())
a = 0
b = 1
for i in range(n):
    print(a)
    a, b = b, a + b

# 2
n = int(input())
prime = True
if n < 2:
    prime = False
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        prime = False
        break
print(prime)

# 3
n = int(input())
rev = 0
temp = abs(n)
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print(-rev if n < 0 else rev)

# 4
n = int(input())
s = 0
for i in range(1, n + 1):
    s += i ** 3
print(s)

# 5
n = int(input())
print(str(n) == str(n)[::-1])
