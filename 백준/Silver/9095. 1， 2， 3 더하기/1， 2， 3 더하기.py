import sys
input = sys.stdin.readline

t = int(input().strip())

dp = [0] * 12
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, 12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

inputs = [int(input().strip()) for _ in range(t)]
results = [str(dp[n]) for n in inputs]

sys.stdout.write("\n".join(results) + "\n")
