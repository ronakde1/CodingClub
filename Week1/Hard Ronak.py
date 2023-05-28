import math
combinations=0
score=9
updatescore=score
n_drats=4

def combinatorics(n_drats,updatescore):
    updatescore=updatescore-n_drats
    if 20>=updatescore >= 0:
        return math.comb(updatescore+n_drats-1,updatescore)
    elif updatescore > 20:
        pass
    else:
        return 0

for i in range(score//2):
    if i < 20: 
        updatescore -= 2
        combinations+=combinatorics(n_drats-1,updatescore)
    else:
        combinations+=combinatorics(n_drats-1,updatescore)
    
print(combinations)
