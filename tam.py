import numpy as np
def lu_decomp(A):
    """(L, U) = lu_decomp(A) is the LU decomposition A = L U
       A is any matrix
       L will be a lower-triangular matrix with 1 on the diagonal, the same shape as A
       U will be an upper-triangular matrix, the same shape as A
    """
    n = A.shape[0]
    if n == 1:
        L = np.array([[1]])
        U = A.copy()
        return (L, U)

    A11 = A[0,0]
    A12 = A[0,1:]
    A21 = A[1:,0]
    A22 = A[1:,1:]

    L11 = 1
    U11 = A11

    L12 = np.zeros(n-1)
    U12 = A12.copy()

    L21 = A21.copy() / U11
    U21 = np.zeros(n-1)

    S22 = A22 - np.outer(L21, U12)
    (L22, U22) = lu_decomp(S22)
    print("L11: ", L11,np.shape(L11))
    print("L12: ", L12,np.shape(L12))
    print("L21: ", L21,np.shape(L21))
    print("L22: ", L22,np.shape(L22))
    L = np.block([[L11, L12], [L21, L22]])
    U = np.block([[U11, U12], [U21, U22]])
    return (L, U)

A = np.array([[1,-2,-2,-3],[3,-9,0,-9],[-1,2,4,7],[-3,-6,26,2]])

lu_decomp(A)