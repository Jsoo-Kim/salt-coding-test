def solution(n):
    number = bin(n).count("1")

    i = n + 1
    while bin(i).count("1") != number:
        i += 1
    return i