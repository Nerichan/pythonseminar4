# Даны два файла, в каждом из которых находится запись многочлена. 
#Задача - сформировать файл, содержащий сумму многочленов.
file1 = open("polynomilal.txt", "r")
polyn1 = file1.read()
polyn1 = polyn1.replace(" ", "")
file2 = open("polyn2.txt", "r")
polyn2 = file2.read()
polyn2 = polyn2.replace(" ", "")
polyn_sum = polyn1 + polyn2
print(polyn_sum)
file3 = open("polyn_sum.txt", "w")
file3.write(polyn_sum)
file3.close()