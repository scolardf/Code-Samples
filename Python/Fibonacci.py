# standard recursion
# def fib(x):
#     if x == 0:
#         return 0
#     elif x == 1:
#         return 1
#     else:
#         return fib(x-1) + fib(x-2)

# recursion with memoization
found = {0: 1, 1: 1}
def fib(x):
    if x not in found:
        found[x] = fib(x-1) + fib(x-2)
    return found[x]

# print first 100 fibonacci numbers
for i in range(0,100):
    print (fib(i))
