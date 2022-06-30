def solution(phone_book):
    answer = True
    hashMap = dict()
    for number in phone_book:
        hashMap[number] = 1
    for number in phone_book:
        temp = ''
        for ch in number:
            temp += ch
            if temp in hashMap.keys() and temp != number:
                return False
    return answer
