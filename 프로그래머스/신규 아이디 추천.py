import re
def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9._-]', '', new_id)
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    if len(new_id) > 0 and new_id[0] == '.':
        new_id = new_id.replace('.', '', 1)
    if len(new_id) > 0 and new_id[len(new_id)-1] == '.':
        new_id = new_id[0:len(new_id)-1]
    if len(new_id) == 0:
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[0:15]
        if new_id[14] == '.':
            new_id = new_id[0:14]
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[len(new_id)-1]

    answer = new_id
    return answer

print(solution("=.="))