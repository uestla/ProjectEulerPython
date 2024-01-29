# https://projecteuler.net/problem=35

from typing import Generator


def get_circular_prime_candidates(limit: int) -> dict[int, bool]:
    candidates = {2: True}

    sieve = [True] * limit

    for n in range(3, limit, 2):
        if sieve[n]:
            sn = str(n)
            if n == 2 or ('0' not in sn and '2' not in sn and '4' not in sn and '6' not in sn and '8' not in sn):
                candidates[n] = True

            m = n * n

            while m < limit:
                sieve[m] = False
                m += n

    return candidates


def get_rotations(n: int) -> Generator[int, None, None]:
    n_len = len(str(n))

    for i in range(0, n_len):
        yield int(str(n)[i:] + str(n)[:i])


def count_circular_primes(limit: int) -> int:
    counter = 0
    checked = {}
    candidates = get_circular_prime_candidates(limit)

    for candidate in candidates:
        if candidate in checked:
            continue

        is_circular_prime = True
        rotations = 0

        for n in get_rotations(candidate):
            if n in checked:
                break

            checked[n] = True
            rotations += 1

            if n not in candidates:
                is_circular_prime = False

        if is_circular_prime:
            counter += rotations

        checked[candidate] = True

    return counter


def solve() -> int:
    return count_circular_primes(1_000_000)


if __name__ == '__main__':
    print('#35 Circular Primes')

    print('Under 100: ' + str(count_circular_primes(100)))

    solution = solve()
    assert solution == 55
    print('Under 1000000: ' + str(solution))
