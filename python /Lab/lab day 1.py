## Day 1 Lab
# Write a program that counts up the number of vowels [a, e, i, o, u]contained in the string.
vowels = "aeiou"
string = input("Enter a string: ")  #Alaa Elhariry
count = 0
for char in string:
    if char.lower() in vowels:
        count += 1
print("The number of vowels in the string is:", count) #The number of vowels in the string is: 6

print('------------------------------------------------------------------------------------------------  ')


# Write a program that prints the locations of "i" character in any string you added.

string = input("Enter a string: ")    #ITI Traniee
for index, char in enumerate(string):
    if char.lower() == 'i':
        print("The character 'i' is found at index:", index)          #The character 'i' is found at index: 0
                                                                      #The character 'i' is found at index: 2
                                                                      #The character 'i' is found at index: 8
print('------------------------------------------------------------------------------------------------  ')


# Write a program that generate a multiplication table from 1 to the number passed.

num = int(input("Enter a number : "))    #5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")  #5 x 1 = 5
                                       # 5 x 2 = 10
                                       # 5 x 3 = 15
                                       #5 x 4 = 20
                                       #5 x 5 = 25
                                       #5 x 6 = 30
                                       #5 x 7 = 35
                                       #5 x 8 = 40
                                       #5 x 9 = 45
                                       #5 x 10 = 50

print('------------------------------------------------------------------------------------------------  ')

# Write a program that build a Mario pyramid
n = int(input("Enter height: ")) #5

for i in range(1, n + 1):
    print("*" * i)           #*
                             #**
                             #***
                             #****
                             #*****        