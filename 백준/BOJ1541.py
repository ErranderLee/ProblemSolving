
input = input()
sum = 0
minusCheck = False
pos = -1
for i in range(len(input)):
    if i == len(input) - 1:
        if minusCheck:
            sum -= int(input[pos + 1:i+1])
        else:
            sum += int(input[pos + 1:i+1])
    if input[i] == '+' and not minusCheck:
        sum += int(input[pos+1:i])
        pos = i
    elif input[i] == '+' and minusCheck:
        sum -= int(input[pos+1:i])
        pos = i
    elif input[i] == '-':
        if minusCheck:
            sum -= int(input[pos+1:i])
            pos = i
        elif not minusCheck:
            sum += int(input[pos + 1:i])
            pos = i
            minusCheck = True

print(sum)