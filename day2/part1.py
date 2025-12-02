res = 0
with open("input.txt", 'r') as file:
    contents = file.read()
    ranges = contents.split(',')
    for range_ in ranges:
        temp = range_.split('-')
        lo = int(temp[0])
        hi = int(temp[1])
        # brute force; Explore every number in between and see if it can be expressed as a 
        # repetition of some number twice
        for i in range(lo, hi + 1):
            # string analysis: split in half, check
            strv = str(i)
            n = len(strv)
            if strv[0:n // 2] == strv[n // 2:]:
                res += i
print(res)


