def solution(sticker):
    answer = 0

    n = len(sticker)

    if n == 1:
        return sticker[0]

    sel1 = [0] * n
    sel2 = [0] * n

    sel1[0] = sticker[0]
    sel1[1] = sticker[0]

    sel2[1] = sticker[1]

    for i in range(2, n - 1):
        sel1[i] = max(sel1[i - 1], sel1[i - 2] + sticker[i])
    max1 = sel1[n - 2]

    for i in range(2, n):
        sel2[i] = max(sel2[i - 1], sel2[i - 2] + sticker[i])
    max2 = sel2[n - 1]

    return max(max1, max2)