
def solution(series, tieNum):
    indexOfOne = series.index(min(series))
    seriesLength = len(series)
    minValue = 999999
    for i in range(tieNum):
        count = 0
        rightStartIndex = indexOfOne + i + 1
        leftStartIndex = rightStartIndex - tieNum - 1
        divideUnit = tieNum - 1
        if leftStartIndex < 0 and rightStartIndex >= seriesLength:
            continue
        else:
            numOfLeftElements = leftStartIndex + 1
            if numOfLeftElements % divideUnit == 0:
                count += numOfLeftElements // divideUnit
            elif numOfLeftElements % divideUnit > 0:
                count += numOfLeftElements // divideUnit + 1

            numOfRightElements = seriesLength - rightStartIndex
            if numOfRightElements % divideUnit == 0:
                count += numOfRightElements // divideUnit
            elif numOfRightElements % divideUnit > 0:
                count += numOfRightElements // divideUnit + 1
        minValue = min(minValue, count)

    return minValue + 1

n, k = list(map(int, input().split()))
series = list(map(int, input().split()))

print(solution(series, k))