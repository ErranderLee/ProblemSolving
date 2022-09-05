def solution(sizes):
    large, small = [], []
    for size in sizes:
        if size[0] >= size[1]:
            large.append(size[0])
            small.append(size[1])
        else:
            large.append(size[1])
            small.append(size[0])
    return max(large) * max(small)