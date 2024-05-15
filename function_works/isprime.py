def is_prime(n1):
    is_primes=True
    for i in range(2,n1):
        if n1%i==0:
            is_primes= False
            break
    return(is_primes)
print(is_prime(13))