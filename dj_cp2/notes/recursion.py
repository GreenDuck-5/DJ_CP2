#DJ, 1st, Recursion Notes

"""for num in range(1, 11):
    if num % 2 == 0:
        print(num)


even = []

num = 999

for x in range(1, 5):
    int(sum) *= int(x)
print(sum)

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(f"Recursion: {factorial(num)}")"""

"""fib = [1, 1]"""

"""for i in range(1, 11):
    fib.append(fib[i-1] + fib[i])

for _ in fib:
    print(_)"""

numbers = []

def fibonnaci(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return fibonnaci(n-1) + fibonnaci(n-1)

fibonnaci(10)

print(f"Recursion: {numbers}")