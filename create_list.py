from functools import reduce

def not_even(n):
    return n % 2 != 0

nums = [9, 8, 6, 7, 1, 5, 4, 3, 2,10, 19]

odd = list(filter(not_even, nums))
print(odd)

even = list(filter(lambda n: n%2 == 0, nums))
print(even)

double = list(map(lambda n : n**2, even))
print(double)

sum = reduce(lambda a,b: a+b,double)
print(sum)
