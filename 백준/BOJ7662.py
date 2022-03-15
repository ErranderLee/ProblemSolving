import sys
import heapq
read = sys.stdin.readline

t = int(read())
for i in range(t):
    n = int(read())
    check = [True for c in range(1000001)]
    ops = []
    minHeap = []
    maxHeap = []
    for j in range(n):
        ops.append(read().rstrip().split())
    count = 0
    for op in ops:
        if op[0] == 'I':
            heapq.heappush(minHeap, (int(op[1]), count))
            heapq.heappush(maxHeap, (-int(op[1]), count))
            count += 1
        else:
            if op[1] == '-1':
                while minHeap:
                    if check[minHeap[0][1]] == False:
                        heapq.heappop(minHeap)
                    else:
                        break
                if minHeap:
                    check[heapq.heappop(minHeap)[1]] = False
            else:
                while maxHeap:
                    if check[maxHeap[0][1]] == False:
                        heapq.heappop(maxHeap)
                    else:
                        break
                if maxHeap:
                    check[heapq.heappop(maxHeap)[1]] = False
    while minHeap:
        if check[minHeap[0][1]] == False:
            heapq.heappop(minHeap)
        else:
            break
    while maxHeap:
        if check[maxHeap[0][1]] == False:
            heapq.heappop(maxHeap)
        else:
            break
    if minHeap:
        print(-maxHeap[0][0], minHeap[0][0])
    else:
        print('EMPTY')