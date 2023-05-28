combinations = 0

def AddNewDrat(workingScore, depth):
    global combinations

    if depth == 0:
        return workingScore
    
    for i in range(1, 21):
        if workingScore + i > targetScore:
            break
        elif workingScore + i == targetScore and depth == 1:
            combinations += 1
            break
        else:
            AddNewDrat(workingScore + i, depth-1)
            
            

tests = [
    (7, 3, 6),
    (33, 1, 0),
    (101, 4, 0),
    (8, 7, 1),
    (28, 1, 1),
    (18, 2, 8),
    (9, 4, 22),
    (36, 3, 191),
    (33, 4, 2075),
    (83, 5, 40000),
    (73, 6, 1402584),
    (95, 8, 515725220)
]

for targetScore, numDrats, answer in tests:
    combinations = 0
    for i in range(1, 21):
        AddNewDrat(i*2, numDrats-1)
        if i*2 == targetScore and numDrats == 1:
            combinations += 1

    print(f"Score = {targetScore}, Drats = {numDrats}, number of combinations = {combinations}, {True if combinations == answer else False}")
    print()