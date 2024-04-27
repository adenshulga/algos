from copy import deepcopy


def merge(A, B):
    C = A + B
    i_a, i_b, i_c = 0, 0, 0

    while (i_a < len(A)) and (i_b < len(B)):
        if B[i_b] < A[i_a]:
            C[i_c] = B[i_b]
            i_b += 1
        else:
            C[i_c] = A[i_a]
            i_a += 1
        i_c += 1

    while i_a < len(A):

        C[i_c] = A[i_a]
        i_c += 1
        i_a += 1

    while i_b < len(B):

        C[i_c] = B[i_b]
        i_c += 1
        i_b += 1

    return C

def mergeSort(A):

    A = [[i] for i in A]

    num_slices = len(A)


    while num_slices != 1: 
        C = []
        for i in range(num_slices // 2):
            C.append(merge(A[2*i], A[2*i+1]))
            print(C)

        if num_slices % 2 == 1:
            C.append(A[-1])
            print(C)
        
        A = C
        num_slices = len(A)

    return A[0]


arr = list(map(int, input().split()))
print(arr)

print(mergeSort(arr))

