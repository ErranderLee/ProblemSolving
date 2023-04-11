from itertools import permutations

operator = ['*', '+', '-']

def separate(expression):
  expression = list(expression)
  operators = []
  for i in range(len(expression)):
    if expression[i] in operator:
      operators.append(expression[i])
      expression[i] = ' '

  return operators, list(map(int, ''.join(expression).split(' ')))


def create_candidates(operators):
  return list(permutations(operators, len(operators)))


def calc(opt, opr1, opr2):
  if opt == '-':
    return opr1 - opr2
  elif opt == '+':
    return opr1 + opr2
  else:
    return opr1 * opr2


def get_result(candidate, operators, operand):
  opr_cp = list(operand)
  opt_cp = list(operators)
  for i in range(len(candidate)):
    opr1 = opr_cp[0]
    opr_list = []
    opt_list = []
    for j in range(len(opt_cp)):
      opt = opt_cp[j]
      opr2 = opr_cp[j + 1]
      if opt == candidate[i]:
        calc_value = calc(opt, opr1, opr2)
        opr1 = calc_value
      else:
        opr_list.append(opr1)
        opt_list.append(opt)
        opr1 = opr2
    opr_cp = opr_list
    opt_cp = opt_list
    opr_cp.append(opr1)
  return opr_cp[0]


def solution(expression):
  answer = 0
  operators, operand = separate(expression)
  print(operators, operand)
  candidates = create_candidates(set(operators))
  print(candidates)
  for candidate in candidates:
    answer = max(abs(get_result(candidate, operators, operand)), answer)
  return answer