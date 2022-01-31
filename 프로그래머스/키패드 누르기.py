def solution(numbers, hand):
    answer = ''
    dist = {}
    left = [1, 4, 7]
    right = [3, 6, 9]
    for i in range(1, 4):
        for j in range(0, 3):
            dist[1+3*(i-1)+j] = [i-1, j]
    dist['*'] = [3, 0]
    dist[0] = [3, 1]
    dist['#'] = [3, 2]

    leftpos = dist['*']
    rightpos = dist['#']

    for number in numbers:
        if number in left:
            answer += 'L'
            leftpos = dist[number]
        elif number in right:
            answer += 'R'
            rightpos = dist[number]
        else:
            presspos = dist[number]
            distanceLeft = abs(leftpos[0] - presspos[0]) + abs(leftpos[1] - presspos[1])
            distanceRight = abs(rightpos[0] - presspos[0]) + abs(rightpos[1] - presspos[1])

            if distanceRight < distanceLeft:
                answer += 'R'
                rightpos = presspos
            elif distanceRight > distanceLeft:
                answer += 'L'
                leftpos = presspos
            else:
                if hand == 'left':
                    answer += 'L'
                    leftpos = presspos
                else:
                    answer += 'R'
                    rightpos = presspos
    return answer