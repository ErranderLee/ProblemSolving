import re


def solution(emails):
    top_level_domain = ['com', 'net', 'org']
    is_valid = re.compile('(?P<name>[a-z\\.]+)[@](?P<domain>[a-z]+)[.](?P<top_level_domain>[a-z]+)')
    answer = 0
    for email in emails:
        match = is_valid.match(email)
        if match:
            if match.group('top_level_domain') in top_level_domain:
                answer += 1
    return answer


print(solution(["d@co@m.com", "a@abc.com", "b@def.com", "c@ghi.net"]))
print(solution(["abc.def@x.com", "abc", "abc@defx", "abc@def.xyz", "@def.xyz"]))