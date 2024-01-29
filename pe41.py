# https://projecteuler.net/problem=41

import math
from typing import Tuple


def permute(digits: list[int]) -> Tuple[bool, list[int]]:
    # based on https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
    last_index = len(digits) - 1

    while True:
        # find the longest ascending suffix
        suffix_start = last_index

        while suffix_start > 0 and digits[suffix_start - 1] < digits[suffix_start]:
            suffix_start -= 1

        if suffix_start == 0:
            return False, []

        pivot = suffix_start - 1

        # find pivot's predecessor
        predecessor = last_index

        while digits[predecessor] > digits[pivot]:
            predecessor -= 1

        # swap with pivot
        pivot_value = digits[pivot]
        digits[pivot] = digits[predecessor]
        digits[predecessor] = pivot_value

        # reverse suffix
        i = suffix_start
        j = last_index

        while i < j:
            i_value = digits[i]
            digits[i] = digits[j]
            digits[j] = i_value

            i += 1
            j -= 1

        # skip numbers divisible by 2 and 5 right away (intentionally no 8 since we only consider 4-digit & 7-digit numbers)
        if digits[last_index] != 2 and digits[last_index] != 4 and digits[last_index] != 5 and digits[last_index] != 6:
            break

    return True, digits


def digits_to_int(digits: list[int]) -> int:
    n = 0
    for digit in digits:
        n = n * 10 + digit

    return n


def is_prime(n: int) -> bool:
    sq = int(math.sqrt(n))

    # intentionally not testing below 7 since permutations do not generate numbers divisible by 2-6
    for d in range(7, sq + 1, 2):
        if n % d == 0:
            return False

    return True


def generate_initial_pandigital_number_array(n: int) -> list[int]:
    digits = [0] * n
    for i in range(0, n):
        digits[i] = n - i

    return digits


def solve() -> int:
    ns = [7, 4]  # only 4-digit & 7-digit pandigital numbers are not divisible by 3

    for n in ns:
        digits = generate_initial_pandigital_number_array(n)

        while True:
            num = digits_to_int(digits)

            if is_prime(num):
                return num

            permuted, digits = permute(digits)

            if not permuted:
                break

    raise 'No pandigital prime number found.'


if __name__ == '__main__':
    print('#41 Pandigital Prime')

    solution = solve()
    assert solution == 7_652_413
    print(solution)
