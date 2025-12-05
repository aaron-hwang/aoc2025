res = 0
with open('input', 'r') as file:
    for line in file.readlines(): 
        stack = []
        bank = list(map(int, line.strip()))
        n = len(bank)
        can_defer = n - 12
        for i in range(n):
            while can_defer > 0 and stack and stack[-1] < bank[i]:
                stack.pop()
                can_defer -= 1
            stack.append(bank[i])
        temp = ''.join(list(map(str, stack[:12])))
        print(temp)
        res += int(temp)
print(res)