def main():
    print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))


def solution(k, tangerine):
    dic_tan = {}
    if k == len(tangerine):
        return k

    for i in tangerine:
        dic_tan[i] = dic_tan.get(i, 0) + 1

    dic_tan = sorted(dic_tan.values(), reverse=True)

    sum = 0
    for k, count in enumerate(dic_tan):
        sum += count
        if sum >= k:
            return k + 1
    return len(dic_tan)


if __name__ == "__main__":
    main()
