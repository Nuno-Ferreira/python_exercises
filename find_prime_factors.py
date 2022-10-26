#input an integer value
#output a list of prime factors
#the list of prime factors multiplied need to be equal to the input

num = int(input('What number would you like to find the prime factors of?:'))

prime_factors = []

def get_prime_factors():
    if num % num == 0 and num % 1 == 0:
        prime_factors.append(num)
        print(prime_factors)
    else:
        return ('Not a prime number')
