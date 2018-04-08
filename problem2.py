def tsort(lst):# O(n)
    done = False
    while not done:
        done = True
        for i in range(0, len(lst)-2):
            if lst[i] > lst[i+2]:
                done = False
                temp = lst[i+2]
                lst[i+2] = lst[i]
                lst[i] = temp

def canT(lst):#o(n)
    ok = True
    tsort(lst)

    for i in range(0, len(lst)-1):
        if lst[i] > lst[i+1]:
            return i
            break
    return -1 if ok else -100

for i in range(0, int(input())):
    n = int(input())
    lst = list(map(int, input().split(' ')))
    x = canT(lst)
    output = str(x) if x != -1 else 'OK'
    print('Case #{}: {}'.format(i+1, output))