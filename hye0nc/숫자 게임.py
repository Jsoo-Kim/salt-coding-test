def main():
    print(solution([5, 1, 3, 7, 4, 2], [2, 2, 6, 5, 4, 3]))


def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    count = 0
    b_index = 0
    for i in range(len(A)):
        if A[i] < B[b_index]:
            count += 1
            b_index += 1
    return count


if __name__ == "__main__":
    main()
