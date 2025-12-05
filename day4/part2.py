res = 0
with open('input', 'r') as file:
    # ALWAYS STRIP YOUR INPUT
    lines = [line.strip() for line in file.readlines()]
    rowlen = len(lines[0])
    # a list of indices where the initial rolls of paper are stored
    rolls_of_paper = {}
    
    # Initial population
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '@':
                rolls_of_paper[(i, j)] = 0

    can_remove = True
    transforms = [[0, 1], [1, 0], [1, 1], [0, -1], [-1, 0], [-1, -1], [1, -1], [-1, 1]]
    while can_remove:
        can_remove = False
        # For every roll of paper, increment the 8 surrounding blocks;
        # The only ones that matter are the ones that contain other rolls of paper though
        for i, j in rolls_of_paper:
            for r, c in transforms:
                index = (i+r, j+c)
                if index in rolls_of_paper:
                    rolls_of_paper[index] += 1
        for roll in list(rolls_of_paper.keys()):
            if rolls_of_paper[roll] < 4:
                can_remove = True
                del rolls_of_paper[roll]
                res += 1
        rolls_of_paper = rolls_of_paper.fromkeys(rolls_of_paper, 0)
print(res)

