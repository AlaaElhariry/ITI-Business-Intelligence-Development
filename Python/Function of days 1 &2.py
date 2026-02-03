##Function of days 1 &2

print('------------------------------------------------------------------------------------------------  ')

# Write a function that counts up the number of vowels [a, e, i, o, u]contained in the string.
def count_vowels(s):
    vowels = "aeiou"          
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count
string = input("Enter a string: ")  #Alaa Elhariry
result = count_vowels(string)
print("The number of vowels in the string is:", result)  #The number of vowels in the string is: 6

print('------------------------------------------------------------------------------------------------  ')

# Write a FUNCTION that prints the locations of "i" character in any string you added.

def location_of_I(s):
    for index, char in enumerate(s):
        if char.lower() == 'i':
            print("The character 'i' is found at index:", index)

string = input("Enter a string: ")         #ITI PORTsaid
location_of_I(string)                      #The character 'i' is found at index: 0
                                           #The character 'i' is found at index: 2
                                           #The character 'i' is found at index: 10

print('------------------------------------------------------------------------------------------------  ')

# Write a function that generate a multiplication table from 1 to the number passed.

def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

num = int(input("Enter a number : "))    #5
multiplication_table(num)                #5 x 1 = 5
                                         #5 x 2 = 10
                                         #5 x 3 = 15
                                         #5 x 4 = 20
                                         #5 x 5 = 25
                                         #5 x 6 = 30
                                         #5 x 7 = 35
                                         #5 x 8 = 40
                                         #5 x 9 = 45
                                         #5 x 10 = 50

print('------------------------------------------------------------------------------------------------  ')

#Write a function to Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display the output
def sort_array():
    arr = []

    for i in range(5):
        num = int(input(f"Enter element {i+1}: ")) #2,5,4,8,4
        arr.append(num)

    print("Array in Ascending Order:", sorted(arr))               #Array in Ascending Order: [2, 4, 4, 5, 8]
    print("Array in Descending Order:", sorted(arr, reverse=True)) #Array in Descending Order: [8, 5, 4, 4, 2]

    
sort_array()

print('------------------------------------------------------------------------------------------------  ')
###Write a function that generate a multiplication table from 1 to the number passed.

def multiplication_table(n):
    result = []

    for i in range(1, n + 1):
        row = []
        for j in range(1, i + 1):
            row.append(i * j)
        result.append(row)

    return result


n = int(input("Enter number: ")) #5
print(multiplication_table(n))   #[[1], [2, 4], [3, 6, 9], [4, 8, 12, 16], [5, 10, 15, 20, 25]]
