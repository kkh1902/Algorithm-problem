n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

nl = [i for i in range(n)]

from itertools import combinations
ans = 1e9

def score(team):
    total = 0
    for i, j in combinations(team, 2):
        total += s[i][j] + s[j][i]
    return total

for team_a in combinations(nl, n // 2):
    if 0 not in team_a:
        continue

    team_b = [i for i in nl if i not in team_a]
    diff = abs(score(team_a) - score(team_b))
    ans = min(ans, diff)

print(ans)
