from collections import defaultdict


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
        comparison_plays_count.append((sum, key))

    comparison_plays_count.sort(key= lambda x: -x[0])

    for sum_minus, key in comparison_plays_count:
        comparison_songs_count_and_id = []
        for id, play_count in genre_songs[key]:
            comparison_songs_count_and_id.append((play_count, id))
        comparison_songs_count_and_id.sort(key= lambda x : (-x[0], x[1]))
        if len(comparison_songs_count_and_id) == 1:
            answer.append(comparison_songs_count_and_id[0][1])
        else:
            answer.append(comparison_songs_count_and_id[0][1])
            answer.append(comparison_songs_count_and_id[1][1])

    return answer


print(solution(
    ["classic", "pop", "classic", "classic", "pop", "jazz"],
    [500, 600, 150, 800, 2500, 15000]
))