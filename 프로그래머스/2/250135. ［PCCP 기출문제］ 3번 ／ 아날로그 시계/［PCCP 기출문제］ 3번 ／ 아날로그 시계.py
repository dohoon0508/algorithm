def solution(h1, m1, s1, h2, m2, s2):
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2

    def count(t):
        return (59 * t) // 3600 + (719 * t) // 43200 + 1 - (1 if t >= 43200 else 0)

    answer = count(end) - count(start)

    if start % 3600 == 0:
        answer += 1

    return answer