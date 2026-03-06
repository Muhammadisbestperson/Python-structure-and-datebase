def sieve_two_digit_primes():
    limit = int(input("Enter a Number:"))
    
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False 
    
    
    for p in range(2, int(limit**0.5) + 1):
        if primes[p]:
            
            for i in range(p * p, limit + 1, p):
                primes[i] = False
                
  
    two_digit_primes = [p for p in range(10, limit + 1) if primes[p]]
    return two_digit_primes

print(sieve_two_digit_primes())


