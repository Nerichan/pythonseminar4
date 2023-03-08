#Задайте последовательность чисел. 
#Напишите программу, которая выведет 
#список неповторяющихся элементов исходной последовательности.
initial_sequence = [1,1,2,2,3,4,4,5]
not_repeats = []
for index in range (0, len(initial_sequence)):
    repeats = initial_sequence.count(initial_sequence[index])
    if repeats == 1:
        not_repeats.append(initial_sequence[index])
print(not_repeats)