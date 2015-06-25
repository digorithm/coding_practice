"""
You are given an array of integers of size N. 
You need to print the sum of the elements of the array.
"""

def solution():
    n = int(raw_input())
    ins = raw_input()
    nums = map(int,ins.split())
    if (len(nums) != n): return 0
    return sum(nums)


if __name__ == "__main__":
    print solution()



