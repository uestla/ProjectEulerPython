# https://projecteuler.net/problem=49

def get_primes() -> list[int]:
    primes = []

    limit = 10_000
    sieve = [True] * limit

    for n in range(3, limit, 2):
        if sieve[n]:
            if n > 1000 and n != 1487 and n != 4817 and n != 8147:
                primes.append(n)

            m = n * n
            while m < limit:
                sieve[m] = False
                m += n

    return primes


def is_permutation(a: int, b: int) -> bool:
    a_list = list(str(a))
    b_list = list(str(b))
    a_list.sort()
    b_list.sort()
    return a_list == b_list


def solve() -> int:
    primes = get_primes()

    for i in range(len(primes) - 2):
        for j in range(i + 1, len(primes) - 1):
            if not is_permutation(primes[i], primes[j]):
                continue

            third = primes[j] + primes[j] - primes[i]

            if third in primes and is_permutation(third, primes[i]):
                return int(str(primes[i]) + str(primes[j]) + str(third))

    raise 'Sequence not found.'


if __name__ == '__main__':
    print('#49 Prime Permutations')

    solution = solve()
    assert solution == 2969_6299_9629
    print(solution)
