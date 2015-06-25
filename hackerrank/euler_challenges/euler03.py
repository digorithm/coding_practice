
def main_function(n):
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1
    return n

n = int(raw_input())
for i in xrange(n):
    x = int(raw_input())
    print main_function(x)
