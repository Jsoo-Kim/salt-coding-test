import math


def main():
    print(solution(16, [2, 9], 2))


def solution(n, stations, w):
    answer = 0
    w_range = w * 2 + 1
    start = 0

    for station in stations:
        left = station - w - 1
        if left > start:
            answer += math.ceil((left - start) / w_range)
        start = station + w

    if start < n:
        answer += math.ceil((n - start) / w_range)

    return answer


if __name__ == "__main__":
    main()
