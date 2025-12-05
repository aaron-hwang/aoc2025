res = 0
with open('input', 'r') as file:
    # ALWAYS STRIP YOUR INPUT
    lines = [line.strip() for line in file.readlines()]
    flattened = []
    rowlen = len(lines[0])
    print("rowlen", rowlen)
    # a list of indices where the initial rolls of paper are stored
    rolls_of_paper = []
    def translate(row, col) -> int:
        return (row*(rowlen))+col

    # Create a flattened array, note each index of a roll of paper and use that
    # to traverse out later
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '@':
                rolls_of_paper.append((i, j))
            flattened.append(0)
    transforms = [[0, 1], [1, 0], [1, 1], [0, -1], [-1, 0], [-1, -1], [1, -1], [-1, 1]]
    for i, j in rolls_of_paper:
        for r, c in transforms:
            if (i + r) >= 0 and (i + r) < len(lines) and (j + c) >= 0 and j + c < rowlen:
                index = translate(i+r, j + c)
                if index < len(flattened) and index > 0:
                    #print(i+r, j+c)
                    flattened[index] += 1
    for i, j in rolls_of_paper:
        if flattened[translate(i,j)] < 4:
            res += 1
    print(flattened)
print(res)
    