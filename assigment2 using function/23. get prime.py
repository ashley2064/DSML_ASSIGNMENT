def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def primes_below_n(N):
    return [i for i in range(2, N) if is_prime(i)]

result = primes_below_n(10)
print(result)