
###Question 1: Multiply Items Together
part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
final_value_1 = 1

for number1 in part1:
    final_value_1 = (final_value_1*number1)

print("Question 1: The value calculated by multiplying the numbers in the list is", final_value_1)

###Question 2: Adding Items Together
part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
final_value_2 = 0

for number2 in part2:
    final_value_2 = (final_value_2+number2)

print("Question 2: The value calculated by adding all the numbers in the list is", final_value_2)

###Question 3: 
part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 
final_value_3 = 0
part3_even = []    #creating empty list for the even values

#making list of even numbers
for number3 in part3: 
    if number3 % 2 == 0:   #using the modulus operator gives us the remainder, if the remainder dividng by 2 is 0, then the number is even
        part3_even.append(number3)    #appending the to the part3_even list if it fulfills the booleon condition 

#adding up values in even list
for number_even in part3_even:
    final_value_3 = final_value_3 + number_even    #for loop to add each number from the evens only list

print("Question 3: The value calculated by adding all the even numbers in the list is", final_value_3)