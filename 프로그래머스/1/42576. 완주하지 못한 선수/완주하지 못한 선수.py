def solution(participant, completion):
    players = {}

    for name in participant:
        if name in players:
            players[name] += 1
        else:
            players[name] = 1

    for name in completion:
        players[name] -= 1

    for name in players:
        if players[name] > 0:
            return name