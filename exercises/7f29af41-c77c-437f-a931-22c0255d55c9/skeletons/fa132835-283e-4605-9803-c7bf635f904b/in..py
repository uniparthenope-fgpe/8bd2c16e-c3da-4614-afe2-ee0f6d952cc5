goals = 3
fouls = 1
score = 0
# Fix the logic below
if goals > 0:
    score += goals * 10
if fouls > 0:
    score -= fouls * 5
print('Final Score:', score)