#input an integer value
#output a list of prime factors
#the list of prime factors multiplied need to be equal to the input

num = int(input('What number would you like to find the prime factors of?:'))

prime_factors = []

def get_prime_factors(num):
    if num % num == 1 and num % 1 == num:
        prime_factors.append(num)
        print(prime_factors)
    else:
        return ('Not a prime number')

get_prime_factors(num)