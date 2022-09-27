

def calc_all(temp_opts, temp_oprs):
    sum = calc_num(temp_oprs[0], temp_oprs[1], temp_opts[0])
    for i in range(1, len(temp_opts)):
        sum = calc_num(sum, temp_oprs[i + 1], temp_opts[i])
    return sum


def calc_num(opr1, opr2, opt):
    if opt == '+':
        return opr1 + opr2
    elif opt == '*':
        return opr1 * opr2
    elif opt == '-':
        return opr1 - opr2


def calc(candidate, opts, oprs):
    temp_opts = []
    temp_oprs = []
    len_opts = len(opts)
    len_oprs = len(oprs)
    i = 0
    while i < len_opts:
        if i in candidate:
            temp_oprs.append(calc_num(oprs[i], oprs[i + 1], opts[i]))
            if i + 1 < len_opts:
                temp_opts.append(opts[i + 1])
            i += 2
            if i == len_oprs - 1:
                temp_oprs.append(oprs[-1])
        else:
            temp_oprs.append(oprs[i])
            temp_opts.append(opts[i])
            if i == len_opts - 1:
                temp_oprs.append(oprs[-1])
            i += 1
    if temp_opts:
        return calc_all(temp_opts, temp_oprs)
    return -1e9


def insert_bracket(opts, oprs):
    if not opts:
        return oprs[0]
    max_sum = calc_all(opts, oprs)
    len_opts = len(opts)
    stack = []
    for i in range(len(opts)):
        stack.append([i])
    while stack:
        opt_ind = stack.pop()
        max_sum = max(max_sum, calc(opt_ind, opts, oprs))
        calc(opt_ind, opts, oprs)
        last_ind = opt_ind[-1]
        for next_ind in range(last_ind, len_opts):
            if next_ind != last_ind and next_ind - last_ind > 1:
                temp = opt_ind[:]
                temp.append(next_ind)
                stack.append(temp)
    return max_sum


if __name__ == '__main__':
    n = int(input())
    # 수식 입력
    string = input()
    # 피연산자
    oprs = [int(string[i * 2]) for i in range(n // 2 + 1)]
    # 연산자
    opts = [string[(i * 2) + 1] for i in range(n // 2)]
    print(insert_bracket(opts, oprs))
