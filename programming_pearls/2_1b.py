"""
rotate a one-dimensional array of N elements left by I positions
"""


"""
Original Pearls Programming Solution: 
    What we do is pretty simple, we reverse the first part
    of the array, which is arr[0] to arr[I] (I == Number of shifts)
    then we reverse the other part, concatenate these two reversed 
    arrays, then reverse this concatenated array
    
    AB == Original Array
    Ar == reversed A
    Br == reversed B
    ArBr == concatenated reversed arrays
    rotated_array == reversed ArBr

"""

def rotate_original_solution_with_reversed(arr, i):
    n = len(arr)
    array_A_reversed = list(reversed(arr[0:i]))
    array_B_reversed = list(reversed(arr[i:n]))
    ArBr = array_A_reversed + array_B_reversed
    rotated_array = list(reversed(ArBr))
    return rotated_array


def rotate_original_solution_with_reverse(arr, i):
    n = len(arr)
    
    array_A = arr[0:i]
    array_B = arr[i:n]
    
    array_A.reverse()
    array_B.reverse()
    

    ArBr = array_A + array_B
    ArBr.reverse()
    return ArBr


def rotate_pythonic_way(arr, i):
    return arr[i:] + arr[:i]


def rotate_pop_append(arr, i):
    print arr
    for x in xrange(i):
        popped = arr.pop(0)
        arr.append(popped)
    print arr
    return arr

import cProfile
if __name__ == "__main__":
    l = [x for x in xrange(10000000)]
    print "Original Idea using reversed(arr): "
    print ""
    cProfile.run('rotate_original_solution_with_reversed(l, 1)')
    
    print "Original Idea using arr.reversed(): "
    print ""
    cProfile.run('rotate_original_solution_with_reverse(l, 1)')

    print "Pythonic Way: "
    print ""
    cProfile.run('rotate_pythonic_way(l,1)')

    print "Pop and append way: "
    print ""
    cProfile.run('rotate_pop_append(l,1)')
