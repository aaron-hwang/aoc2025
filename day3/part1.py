res = 0
with open('input', 'r') as file:
    for line in file.readlines():
        largest = 0
        bank = list(map(int, line.strip()))
        l = 0
        r = 1
        while r < len(bank):
            largest = max(largest, bank[l] * 10 + bank[r])
            if bank[l] < bank[r]:
                l = r
            r += 1
        res += largest
print(res)
