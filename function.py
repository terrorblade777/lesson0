def get_matrix(n, m, value):
    matrix=[]
    for i in range(n):
        a=[]
        for j in range(m):
            a.append(value)
            matrix.append(a)
    return matrix
result1 = get_matrix(2,2 ,3 )
result2 = get_matrix(1,5 ,6 )
result3 = get_matrix(6,2 ,3 )
print(result1)
print(result2)
print(result3)
