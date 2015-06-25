

def func(levels):
    for i in xrange(1,levels+1):
        print ("#" * i).rjust(levels)

n = int(raw_input())
func(n)

