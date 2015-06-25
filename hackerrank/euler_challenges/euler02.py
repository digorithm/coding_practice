# Enter your code here. Read input from STDIN. Print output to STDOUT


def even_fib(limit):
    a, b = 0, 1
    while a < limit:
        if not a % 2:         
            yield a
        a, b = b, a + b

qt = int(raw_input())
for i in xrange(qt):
    n = int(raw_input())
    print sum(even_fib(n))
