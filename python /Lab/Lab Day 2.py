# Lab Day 2
#Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display the output.
def main():
    arr = []
    for i in range(5):
        num = int(input(f"Enter element {i+1}: "))   #Enter element 1: 5
                                                     #Enter element 2: 4
                                                     #Enter element 3: 8
                                                     #Enter element 4: 7
                                                     #Enter element 5: 9

        arr.append(num)

    ascending = sorted(arr)
    descending = sorted(arr, reverse=True)
    print("Array in Ascending Order:", ascending)  #Array in Ascending Order: [4, 5, 7, 8, 9]
    print("Array in Descending Order:", descending) #Array in Descending Order: [9, 8, 7, 5, 4]


main()

print('------------------------------------------------------------------------------------------------  ')

##Write a program that generate a multiplication table from 1 to the number passed.
#EX: 
#The input is 3         
#The Output is:[[1],[2,4],[3,6,9]]     
n = int(input("Enter number: "))   #5

result = []

for i in range(1, n + 1):
    row = []
    for j in range(1, i + 1):
        row.append(i * j)
    result.append(row)

print(result)               #[[1], [2, 4], [3, 6, 9], [4, 8, 12, 16], [5, 10, 15, 20, 25]]
print('------------------------------------------------------------------------------------------------  ')
#Ask the user for his name then confirm that he has entered his name(not an empty 
#string/integers). then proceed to ask him for his email and print all this data(Bonus) check if it is 
#a valid email or not
name = input("Enter your name: ")                             #Enter your name: alaa

while name == "" or name.isdigit():
    print("Invalid name")
    name = input("Enter your name again: ")

email = input("Enter your email: ")                           #Enter your email:alaaelhariry@gmail.com

while email == "" or "@" not in email or "." not in email:
    print("Invalid email")
    email = input("Enter your email again: ")

print("Name:", name)  #Name: alaa
print("Email:", email)  #Email: alaaelhariry@gmail.com

print('------------------------------------------------------------------------------------------------  ')
 
#Check user login and password that saves in a list of dictionaries.
users = [
    {"name": "omar", "pass": "123"},
    {"name": "ahmed", "pass": "456"}
]

username = input("Enter username: ")  #omar
password = input("Enter password: ")  #123

if any(user["name"] == username and user["pass"] == password for user in users):
    print("Login successful")        #Login successful
else:
    print("Invalid username or password")

    
