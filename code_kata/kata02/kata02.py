"""Write a binary chop method that takes an integer search target and a sorted array of integers. It should return the integer index of the target in the array, or -1 if the target is not in the array. The signature will logically be:

chop(int, array_of_int)  -> int

You can assume that the array has less than 100,000 elements. For the purposes of this Kata, time and memory performance are not issues (assuming the chop terminates before you get bored and kill it, and that you have enough RAM to run it)."""


# for profiling line by line, on terminal:
# kernprof -l -v kata02.py
# remove comments on @profile

@profile
def chop(l, value):
    low = 0
    high = len(l)-1
    while low <= high: 
        mid = (low+high)//2
        if l[mid] > value: 
            high = mid-1
        elif l[mid] < value: 
            low = mid+1
        else: 
            return mid
    return -1

@profile
def recursive_chop(l, value, low = 0, high = -1):
    if not l:
        return -1
    if(high == -1):
        high = len(l)-1
    if low == high:
        if l[low] == value:
            return low
        else:
            return -1
    mid = (low+high)//2
    if l[mid] > value:
        return recursive_chop(l, value, low, mid-1)
    elif l[mid] < value:
        return recursive_chop(l, value, mid+1, high)
    else:
        return mid
    

if __name__ == '__main__':
    l = [x for x in xrange(10000000)]
    value = 6000
    print recursive_chop(l,value) 
    print chop(l, value)
