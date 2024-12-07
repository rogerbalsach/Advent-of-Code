with open('input.txt') as file:
    content = file.readlines()


def main() -> None:
    left_list = [0] * len(content)
    right_list = [0] * len(content)
    left_counter: dict[int, int] = {}
    right_counter: dict[int, int] = {}
    for i, line in enumerate(content):
        x, y = map(int, line.split())
        left_list[i], right_list[i] = x, y
        left_counter[x] = left_counter.get(x, 0) + 1
        right_counter[y] = right_counter.get(y, 0) + 1

    left_list = sorted(left_list)
    right_list = sorted(right_list)

    s1 = 0
    for i, j in zip(left_list, right_list):
        s1 += abs(i-j)

    print(s1)

    s2 = 0
    for (k1, v1) in left_counter.items():
        s2 += k1 * v1 * right_counter.get(k1, 0)

    print(s2)


if __name__ == '__main__':
    main()
