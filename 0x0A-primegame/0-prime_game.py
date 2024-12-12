#!/usr/bin/python3
"0-prime_game.py"


def isWinner(x, nums):
    """Determines the winner of the prime game.
    Args:
        x (int): The number of rounds to be played.
        nums (List[int]): A list of integers representing the numbers
        for each round.
    Returns:
        str: The name of the winner ("Ben" or "Maria").
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i - 1]:
            for j in range(i * i, n + 1, i):
                primes[j - 1] = False
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
