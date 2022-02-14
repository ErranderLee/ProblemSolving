s = input()

zero = 0
one = 0

for i in range(len(s)):
    if i == len(s)-1:
        if s[i] == '0':
            zero += 1
        else:
            one += 1
        break
    if s[i] == s[i + 1]:
        pass
    else:
        if s[i] == '0':
            zero += 1
        else:
            one += 1
if zero == 0 or one == 0:
    print(0)
else:
    print(min(zero, one))