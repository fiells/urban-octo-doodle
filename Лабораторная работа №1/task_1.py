numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
count_numbers = len(numbers)
# TODO заменить значение пропущенного элемента средним арифметическим
numbers[4] = 0
sum_numbers = sum(numbers)
average_number = sum_numbers/count_numbers
numbers[4] = average_number

print("Измененный список:", numbers)
