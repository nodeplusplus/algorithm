def count_inversion(A: [str]) -> int:
    if len(A) <= 1:
        return A, 0

    pointer = round(len(A)/2)
    B, x = count_inversion(A[:pointer])
    C, y = count_inversion(A[pointer:])
    D, z = count_split_inversion(A, B, C)  # should pass A + B
    return (D, x+y+z)


def count_split_inversion(A: [str], B: [str], C: [str]) -> ([str], int):
    D, z, i, j = [], 0, 0, 0

    while i < len(B) and j < len(C):
        b, c = B[i], C[j]
        if b < c:
            D.append(b)
            i += 1
        elif b > c:
            D.append(c)
            # Here
            z += len(B[i:])
            j += 1
        else:
            D.append(b)
            D.append(c)
            i += 1
            j += 1

    return [*D, *B[i:], *C[j:]], z


tests = [
    ([1, 3, 5, 2, 4, 6], 3),
    ([8, 4, 2, 1], 6),
]


for A, r in tests:
    _A, a = count_inversion(A)
    if a != r:
        print(f"{A} -> {a} # {r}")
    else:
        print(f"{A} -> OK")
