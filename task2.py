#2 Задайте натуральное число N. Напишите программу, 
#которая составит список простых множителей числа N.
n = int(input("введите число N: "))
#def multipliers(a):
numbers = []
counter = 2
while n>counter:
    if n%counter == 0:
        numbers.append(n/counter)
        counter=counter+1
    else: 
        counter=counter+1

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = []
for index in range (0, len(numbers)):
    if is_prime(numbers[index]) == True:
        prime_numbers.append(numbers[index])
if len(prime_numbers) == 0:
    print("число простое, его множители это 1 и", n)
else:
    print("простые множители: ", 1, list(map(round, prime_numbers)))