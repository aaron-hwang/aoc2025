import re
res = 0
with open("input.txt", 'r') as file:
    contents = file.read()
    ranges = contents.split(',')
    for range_ in ranges:
        temp = range_.split('-')
        lo = int(temp[0])
        hi = int(temp[1])
        curr = []
        for i in range(lo, hi + 1):
            tmp = str(i)
            if re.match(r"^(\d+)\1+$", tmp):
                curr.append(i)
                res += i
        print(curr)
print(res)