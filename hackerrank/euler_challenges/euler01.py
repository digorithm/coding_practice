import cProfile
def multiples_of_3_or_5_alternative_method(n):
    s = 0
    for i in xrange(3,n,3): s += i
    for i in xrange(5,n,15): s += i
    for i in xrange(10,n,15): s += i
    return s

def multiples_of_3_or_5(n):
    total = 0
    for number in xrange(n):
        if not number % 3 or not number % 5:
            total = total + number
    return total

n = int(raw_input())
test_cases = []
for i in xrange(n):
    test_cases.append(int(raw_input()))
    
for test in test_cases:
    print multiples_of_3_or_5_alternative_method(test)

cProfile.run('multiples_of_3_or_5(1000000000)')
cProfile.run('multiples_of_3_or_5_alternative_method(1000000000)')
