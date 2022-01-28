from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    reported_dict = defaultdict(set)
    report_dict = defaultdict(set)
    for item in report:
        reporter, reportee = item.split()
        reported_dict[reportee].add(reporter)
        # if len(reported_dict[reportee]) >= k:
        #     if len(reported_dict[reportee]) == k:
        #         for id in reported_dict[reportee]:
        #             report_dict[id].add(reportee)
        #     else:
        #         report_dict[id].add(reportee)
    for key in reported_dict:
        if len(reported_dict[key]) >= k:
            for id in reported_dict[key]:
                report_dict[id].add(key)
    for id in id_list:
        answer.append(len(report_dict[id]))
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi", "muzi apeach", "neo apeach"], 2))