import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
total = 0
ans = n + 1

for right in range(n):
    total += nums[right]

    while total >= s:
        ans = min(ans, right - left + 1)
        total -= nums[left]
        left += 1

print(ans if ans != n + 1 else 0)