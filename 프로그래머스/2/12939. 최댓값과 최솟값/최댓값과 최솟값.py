def solution(s):
    numbers = [int(x) for x in s.split()]
    max_val = max(numbers)
    min_val = min(numbers)
    return f"{min_val} {max_val}"