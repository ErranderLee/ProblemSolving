import sys
sys.setrecursionlimit(10000000)

def solution(babbling):
  answer = 0
  given = ["aya", "ye", "woo", "ma"]
  global result
  result = False
  def concat(string, word, prev):
    global result
    if string == word:
      return True
    if len(string) > len(word):
      return False
    if word[0:len(string)] != string:
      return False
    for given_word in given:
      if prev != given_word:
        result |= concat(string + given_word, word, given_word)
    return result

  for word in babbling:
    for given_word in given:
      if concat(given_word, word, given_word):
        result = False
        answer += 1
  return answer