curr = 50
res = 0

def rotate(amt, direction):
    global curr
    if direction == 'L':
        curr -= amt
    else:
        curr += amt
    curr = curr % 100
    
# Very dumb way
with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        direction = line[0]
        amt = int(line[1:])
        for i in range(amt):
            rotate(1, direction)
            if curr == 0:
                res += 1


if __name__ == "__main__":
    print(res)