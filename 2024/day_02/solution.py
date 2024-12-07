with open('input.txt') as file:
    content = file.read()


def report_is_safe(levels: list[int], remove: int = 0) -> bool:
    sign = None
    prev = levels[0]
    for curr in levels[1:]:
        diff = curr - prev
        if (diff == 0 or abs(diff) > 3
                or sign is not None and diff / abs(diff) != sign):
            if remove == 0:
                return False
            remove -= 1
        else:
            if sign is None:
                sign = diff // abs(diff)
            prev = curr
    return True


def main() -> None:
    s1 = s2 = 0
    for line in content.splitlines():
        levels = list(map(int, line.split()))
        if report_is_safe(levels):
            s1 += 1
        if report_is_safe(levels, remove=1) or report_is_safe(levels[1:]):
            s2 += 1

    print(s1)
    print(s2)


if __name__ == '__main__':
    main()
