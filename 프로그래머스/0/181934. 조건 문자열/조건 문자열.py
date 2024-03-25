def solution(ineq, eq, n, m):

    a = ineq == "<" and eq == "=" and n <= m and True
    b = ineq == ">" and eq == "=" and n >= m and True
    c = ineq == "<" and eq == "!" and n < m and True
    d = ineq == ">" and eq == "!" and n > m and True

    if a or b or c or d:
        return 1
    else :
        return 0