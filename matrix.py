# ---------------
# matrix code
# ---------------


import math
from vector import dot

def rows(A):
    return len(A)

def cols(A):
    return len(A[0]) # too simple?

def shape(A):
    return rows(A), cols(A)

def get_row(A,i):
    return A[i]

def get_column(A,j):
    return [A_i[j] for A_i in A]

def make_matrix(num_rows,num_cols,fn):
    return [[fn(i,j)
             for j in range(num_cols)]
            for i in range(num_rows)]

def is_diagonal():
    pass

def identity(n):
    return make_matrix(n,n,lambda i,j: 1 if i==j else 0)

def matrix_multiply(A,B):
    if cols(A) != rows(B):
        raise RuntimeError(f"{shape(A)}{shape(B)}")
    return [[dot(row,col) for col in zip(*B)] for row in A] # zip(*B) can iterate all the element from each row at the same time, aka looping through the columns

    