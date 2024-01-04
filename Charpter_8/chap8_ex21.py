def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0: #If num is  divisible by any other number in the sequence
            #print(f'{num}%{i}={num%i}')
            return False #Isn't prime
    return True #Else is prime

def sum_primes(number):
    sum = 0
    for i in range(1, number+1):
        if is_prime(i):
            print(f'number {i} is prime')
            sum += 1
    return sum

while True:
    val = int(input('Enter a value: '))
    print(sum_primes(int(val)))

'''while True:
    print(is_prime(int(input('Enter a value: '))))'''