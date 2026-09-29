2.1
def transpose(mat: list[list[float | int]]) -> list[list]:
    """Поменять строки и столбцы местами в прямоугольной матрице
    [[1, 2], [3, 4]] → [[1, 3], [2, 4]]
    """
    for row in mat:
        if len(row)!=len(mat[0]):
            raise ValueError('«матрица рваная» (строки разной длины)')
    
    
# #2.2
# def row_sums(mat: list[list[float | int]]) -> list[float]:
#     """Сумма по каждой строке. Требуется прямоугольность 
#     [[1, 2, 3], [4, 5, 6]] → [6, 15]
#     """
#     for row in mat:
#         if len(row)!=len(mat[0]):
#             raise ValueError('Рваная матрица')
#     ans=[]
#     for row in mat:
#         ans.append(sum(row))
#     return ans

# print(row_sums([[1, 2, 3], [4, 5, 6]]))
# print(row_sums([[-1, 1], [10, -10]]))
# print(row_sums([[0, 0], [0, 0]]))
# print(row_sums([[1, 2], [3],]))



# #2.3
# def col_sums(mat: list[list[float | int]]) -> list[float]:
#     """ Сумма по каждому столбцу. Требуется прямоугольность.
#     [[1, 2, 3], [4, 5, 6]] → [5, 7, 9] """
    
#     for row in mat:
#         if len(row)!=len(mat[0]):
#             raise ValueError('рвананя матрица')
#     ans=[]
#     st=len(mat[0])
#     for j in range(st):
#         cnt=0
#         for row in mat:
#             cnt+=row[j]
#         ans.append(cnt)
#     return ans

# print(col_sums([[1,2,3],[4,5,6]]))
# print(col_sums([[-1, 1], [10, -10]]))
# print(col_sums([[0, 0], [0, 0]]))
# print(col_sums([[1, 2], [3]]))