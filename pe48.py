# https://projecteuler.net/problem=48

import math


def self_power(n: int, decimals: int) -> int:
    result = 0
    mod = int(math.pow(10, decimals))

    for i in range(1, n + 1):
        add = 1
        for j in range(1, i + 1):
            add = (add * i) % mod

        result = (result + add) % mod

    return result


def solve() -> int:
    return self_power(1000, 10)


if __name__ == '__main__':
    print('#48 Self Powers')

    print('1^1 + 2^2 + 3^3 + ... + 10^10 = ' + str(self_power(10, 11)))

    solution = solve()
    assert solution == 9_110_846_700
    print('(1^1 + 2^2 + 3^3 + ... + 1000^1000) % 10^10 = ' + str(solution))
