def gcdString(A, B):
    str_c = ''
    len1, len2 = len(A), len(B)

    for i in range(len1):
        match = ''
        for j in range(len2):
            if (i + j < len1 and A[i + j] == B[j]):
                match += B[j]
            else:
                if (len(match) > len(str_c)):
                    str_c = match
                match = ''
    return str_c

A = 'abababab'
B = 'abab'

print(gcdString(A, B))