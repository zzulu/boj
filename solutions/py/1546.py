N = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
scores = list(map(lambda score: (score/max_score)*100, scores))
print(sum(scores)/N)
