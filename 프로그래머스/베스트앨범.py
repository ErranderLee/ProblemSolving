from collections import defaultdict
import heapq


def solution(genres, plays):
    answer = []
    genre_songs = defaultdict(list)
    for i, genre in enumerate(genres):
        genre_songs[genre].append((i, plays[i]))
    comparison_plays_count = list()

    for key in genre_songs.keys():
        sum = 0
        for id, play_count in genre_songs[key]:
            sum += play_count
        heapq.heappush(comparison_plays_count, (-sum, key))

    while comparison_plays_count:
        sum_minus, key = heapq.heappop(comparison_plays_count)
        comparison_songs_count_and_id = []
        for id, play_count in genre_songs[key]:
            heapq.heappush(comparison_songs_count_and_id, (-play_count, id))

        if len(comparison_songs_count_and_id) == 1:
            answer.append(heapq.heappop(comparison_songs_count_and_id)[1])
        else:
            answer.append(heapq.heappop(comparison_songs_count_and_id)[1])
            answer.append(heapq.heappop(comparison_songs_count_and_id)[1])

    return answer


print(solution(
    ["classic", "pop", "classic", "classic", "pop", "jazz"],
    [500, 600, 150, 800, 2500, 15000]
))