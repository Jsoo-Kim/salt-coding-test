def main():
    print(solution([14, 6, 5, 11, 3, 9, 2, 10]))


def solution(sticker):
    answer = 0
    n = len(sticker)

    if n == 1:
        return sticker[0]

    isEven = True if len(sticker) % 2 == 0 else False
    sum = 0
    sum2 = 0
    if isEven:
        for i in range(len(sticker)):
            if i % 2 == 0:
                sum += sticker[i]

        for i in range(len(sticker)):
            if i % 2 == 1:
                sum2 += sticker[i]
        return max(sum, sum2)
    else:
        for i in range(len(sticker)):
            start = sticker[0]
            end = sticker[len(sticker) - 1]
            max_sticker = max(start, end)
            if i % 2 == 0 and i != 0 and i != len(sticker) - 1:
                sum += sticker[i]

        for i in range(len(sticker)):
            if i % 2 == 1:
                sum2 += sticker[i]
        return max(sum, sum2)


if __name__ == "__main__":
    main()
