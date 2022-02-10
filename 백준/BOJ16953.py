A, B = list(map(int, input().split()))
count = 0

def func(A, B):
    count = 1
    Bstr = str(B)
    while True:
        Bstr = str(B)
        if B == A:
            return count
        elif B < A:
            return -1
        else:
            if B % 2 == 0:
                B = int(B / 2)
                count += 1
            elif Bstr[-1] == '1':
                Bstr = Bstr[0:len(Bstr)-1]
                B = int(Bstr)
                count += 1
            else:
                return -1
print(func(A, B))
