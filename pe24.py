# https://projecteuler.net/problem=24

def nth_permutation(max_digit: int, nth: int) -> str:
    # based on https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
    digits = list(range(0, max_digit + 1))
    permutation = 1

    while permutation != nth:
        # find the longest descending suffix
        suffix_start = max_digit

        while suffix_start > 0 and digits[suffix_start - 1] > digits[suffix_start]:
            suffix_start -= 1

        if suffix_start == 0:
            raise str(permutation) + ' is the last permutation'

        pivot = suffix_start - 1

        # find pivot's predecessor
        predecessor = max_digit

        while (digits[predecessor] < digits[pivot]):
            predecessor -= 1

        # swap with pivot
        pivot_value = digits[pivot]
        digits[pivot] = digits[predecessor]
        digits[predecessor] = pivot_value

        # reverse suffix
        i = suffix_start
        j = max_digit

        while i < j:
            i_value = digits[i]
            digits[i] = digits[j]
            digits[j] = i_value

            i += 1
            j -= 1

        permutation += 1

    return ''.join(str(n) for n in digits)


def solve() -> str:
    return nth_permutation(9, 1_000_000)


if __name__ == '__main__':
    print('#24 Lexicographic Permutations')

    solution = solve()
    assert solution == '2783915460'
    print(solution)
