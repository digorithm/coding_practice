"""
You are given a square matrix of size N×N. Calculate the absolute difference of the sums across the two main diagonals.

PS: I'm not treating invalid inputs.
"""


class DiagonalDifference():
    def solve(self,mat):
        return abs(sum([mat[i][i] for i in range(len(mat))]) 
                    - sum([ row[-i-1] for i,row in enumerate(mat)]))



if __name__ == "__main__":
    dd = DiagonalDifference()
    n = int(raw_input())
    mat = []
    
    for i in range(n):
        row = map(int, raw_input().split())
        mat.append(row)
    
    print dd.solve(mat)
