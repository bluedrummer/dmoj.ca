turn_around = 0
scored_before_half_time = 0
half_time = 1441
scores_a = []
scores_b = []
score_of_a = 0
score_of_b = 0
ahead_team = ""
number_of_points_scored = int(input())
for i in range(0, number_of_points_scored):
    t = int(input())
    scores_a.append(t)
    if t < half_time:
        scored_before_half_time += 1

number_of_points_scored = int(input())
for i in range(0, number_of_points_scored):
    t = int(input())
    scores_b.append(t)
    if t < half_time:
        scored_before_half_time += 1
        
for s in range(1, 2880):
    if scores_a.count(s) == 1:
        score_of_a += 1
    if s in scores_b:
        score_of_b += 1
    if score_of_a > score_of_b and ahead_team == "B":
        turn_around += 1
    if score_of_b > score_of_a and ahead_team == "A":
        turn_around += 1
    if score_of_a > score_of_b:
        ahead_team = "A"
    if score_of_b > score_of_a:
        ahead_team = "B"

print(scored_before_half_time)
print(turn_around)        

    





           
    

