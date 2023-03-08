# Задана натуральная степень k. 
#Сформировать случайным образом список коэффициентов 
#(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#*Пример:* 
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
k = input("enter K: ")
import random
random_numbers = random.sample(range(0, 101), 3)
print(random_numbers)
#print((random_numbers[0]), "x^", int(k), "+", str(random_numbers[1]), "y^", int(k), "+", random_numbers[2], sep='')
print("{}*x^{} + {}*y^{} + {}".format(random_numbers[0], k, random_numbers[1], k, random_numbers[2]))
f = open('polynomilal.txt', 'w')
f.write("{}*x^{} + {}*y^{} + {}".format(random_numbers[0], k, random_numbers[1], k, random_numbers[2]))
f.close()