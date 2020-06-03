n = 100

sieve = [i for i in range(n)]
sieve[1] = 0

for i in range(2, n):
    if sieve[i] != 0:
        j = i + i
        while j < n:
            sieve[j] = 0
            j += i

print(sieve)

sieve_1 = [i for i in sieve if i != 0]
print(sieve_1)