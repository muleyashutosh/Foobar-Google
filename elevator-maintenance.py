def solution(l):
    if len(l) == 1:
        print(l[0])
        quit()
    count = 0
    for item in l:
        x = item.split('.')
        l[count] = [int(z) for z in x]
        count += 1
    l.sort()
    count = 0
    for item in l:
        z = [str(x) for x in item]
        l[count] = ".".join(z)
        count += 1
    count = 0
    return l