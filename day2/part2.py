res = 0
with open('intput.txt', 'r') as file:
    contents = file.read()
    ranges = contents.split(',')
    for range_ in ranges:
        temp = range_.split('-')
        lo = int(temp[0])
        hi = int(temp[1])
        # brute force: check every number in range of digit length, check if string is 
        # made of repetitions of it 
        for i in range(lo, hi + 1):
            temp = str(i)
            for j in range(len(temp) // 2):
                # TODO
                pass