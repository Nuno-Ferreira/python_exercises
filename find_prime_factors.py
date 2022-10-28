#input an integer value
#output a list of prime factors
#the list of prime factors multiplied need to be equal to the input

num = int(input('What number would you like to find the prime factors of?:'))

def get_prime_factors(a):
    prime_factors = []
    divisor = 2
    while(divisor <= a):
        if (a % divisor) == 0:
            prime_factors.append(divisor)
            a = a//divisor
        else:
            divisor += 1
    return prime_factors

b = get_prime_factors(num)
print(b)