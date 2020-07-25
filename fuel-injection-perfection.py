
# DICTIONARY = {}
# # solve
# def solve(n):
#     '''
#     DOC
#     '''
#     global DICTIONARY

#     if n == 1:
#         return 0
#     cnt = 0
#     cnt1 = 1
#     cnt2 = 1
#     if n % 2 == 0:
#         cnt += 1
#         try:
#             ans = DICTIONARY[int(n / 2)]
#         except KeyError:
#             ans = solve(int(n / 2))
#             DICTIONARY[int(n / 2)] = ans
#         cnt += ans
#     else:
#         try:
#             ans1 = DICTIONARY[n + 1]
#         except KeyError:
#             ans1 = solve(n + 1)
#             DICTIONARY[n + 1] = ans1
#         cnt1 += ans1
#         try:
#             ans2 = DICTIONARY[n - 1]
#         except KeyError:
#             ans2 = solve(n - 1)
#             DICTIONARY[n - 1] = ans2

#         cnt2 += ans2
#         cnt += min(cnt1, cnt2)
#     DICTIONARY[n] = cnt
#     return cnt
def fast(n):
    count = 0
    while(n != 1):
        if (n & 1) == 0:
            n //= 2
        elif (n == 3) or ((n + 1) & n) > ((n - 1) & (n - 2)):
            n -= 1
        else:
            n += 1
        count += 1
    return count
# convert string to long   
def solution(n):
    '''
    DOC
    '''
    n = int(n)
    if n in (1, 0):
        return 0
    return fast(n)

print(fast(int(input())))
# for k, v in DICTIONARY.items():
#     print(k, v)
