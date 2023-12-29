from test_framework import generic_test


def power(x: float, y: int) -> float:
    # TODO - you fill in here.
    if y == 0:
        return 1.0
    elif y > 0:
        pow = power(x, y // 2)
        if y % 2 == 0:
            return pow * pow
        else:
            return x * pow * pow
    elif y < 0:
        return 1 / power(x, -y)


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
