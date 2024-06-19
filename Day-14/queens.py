def solveNQueens( n):

    def test(i, j, cols, left_d, right_d):
        return not (cols[j] or left_d[i+j] or right_d[i-j])

    def place(i, j, cols, left_d, right_d):
        bd[i][j] = "Q"
        cols[j] = left_d[i+j] = right_d[i-j] = True

    def remove(i, j, cols, left_d, right_d):
        bd[i][j] = "."
        cols[j] = left_d[i+j] = right_d[i-j] = False

    def back(row):
        if row == n:
            temp = []
            for r in bd:
                temp.append("".join(r))
            sol.append(temp)
            return

        for col in range(n):
            if test(row, col, cols, left_d, right_d):
                place(row, col, cols, left_d, right_d)
                back(row + 1)
                remove(row, col, cols, left_d, right_d)

    sol = []
    bd = [["." for i in range(n)] for j in range(n)]
    cols = [False] * n
    left_d = [False] * (2*n-1)
    right_d = [False] * (2*n-1)
    back(0)
    return sol


n = int(input())


sol = solveNQueens(n)
print(sol)
print(len(sol))
