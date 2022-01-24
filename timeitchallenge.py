# In the section on Functions, we looked at 2 different ways to calculate the factorial
# of a number.  We used an iterative approach, and also used a recursive function.
#
# This challenge is to use the timeit module to see which performs better.
#
# The two functions appear below.
#
# Hint: change the number of iterations to 1,000 or 10,000.  The default
# of one million will take a long time to run.
 
import timeit


iters = '''\
def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result
'''
 
recursive = '''\
def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
'''

print(timeit.timeit(iters, number=100000))
print(timeit.timeit(recursive, number=100000))
