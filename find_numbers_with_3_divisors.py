def solution(n, m):
    import math
    
    # Sieve of Eratosthenes to generate all primes up to sqrt(m)
    def sieve(limit):
        is_prime = [True] * (limit + 1)
        p = 2
        while (p * p <= limit):
            if is_prime[p]:
                for i in range(p * p, limit + 1, p):
                    is_prime[i] = False
            p += 1
        primes = [p for p in range(2, limit + 1) if is_prime[p]]
        return primes
    
    # Compute the upper limit for prime checking
    upper_limit = int(m**0.25) + 1
    
    # Generate all primes up to upper_limit
    primes = sieve(upper_limit)
    
    # Compute p^4 for each prime and filter those within the range [n, m]
    result = []
    for prime in primes:
        p4 = prime**4
        if n <= p4 <= m:
            result.append(p4)
    
    # Sort the result array (although it should already be sorted)
    result.sort()
    
    return result

# Example usage:
print(solution(2, 100))  # Output should be [16]
