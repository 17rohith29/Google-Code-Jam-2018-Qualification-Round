def damage(string): # O(n)
    x = 1
    damage = 0
    for i in string:
        if i == 'C':
            x *= 2
        if i == 'S':
            damage += x
    return damage

def swapOnce(string): #O(n)
    for i in range(len(string)-1, 0, -1):
        if string[i] == "S" and string[i-1] == "C":
            string = string[:i-1] + "SC" + string[i+1:]
            return [string,True]
    return [string,False]

def times(string, max):
    count = 0
    while True:
        if damage(string) <= max: # n
            return count
        else: # n
            string,pos = swapOnce(string)
            if not pos:
                return -1
            else:
                count += 1

for i in range(0, int(input())):
    max, string = input().split(' ')
    max = int(max)
    time = times(string, max)
    output = str(time) if time != -1 else "IMPOSSIBLE"
    print('Case #{}: {}'.format(i+1, output))
