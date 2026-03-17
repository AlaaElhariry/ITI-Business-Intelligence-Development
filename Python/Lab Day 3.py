#lab day 3
# use for loop to print a right angle triangle pattern of asterisks with a height of 5 
height =[" ", " ", " ", " ", " "]
for i in range (1,len(height)+1):
          height[len(height)- (len(height)+i)] = "*"
          print (height)
print('\n')
print (height)                    #[' ', ' ', ' ', ' ', '*']
                                  #[' ', ' ', ' ', '*', '*']
                                  #[' ', ' ', '*', '*', '*']
                                  #[' ', '*', '*', '*', '*']
                                  #['*', '*', '*', '*', '*']


                                  #['*', '*', '*', '*', '*']

print('---------------------------------------------------------------')
##You are given a list of email addresses in the format username@domain.Your task is to use the map() function along with a lambda domain part from each email address.
#expression to extract only the 
#2 – You are given a list of email addresses, some of which are invalid and use the filter() function to return only the valid email addresses

# -------- is_valid_email defined globally --------
def is_valid_email(email):
    return "@" in email and "." in email

# -------- get user data function --------
def get_user_data():
    name = input("Enter your name: ")
    while not name.isalpha():
        name = input("Invalid name, enter again: ")

    email = input("Enter your email: ")
    while not is_valid_email(email):
        email = input("Invalid email, enter again: ")

    return name, email

# -------- email list --------
emails = [
    "alaa@gmail.com",
    "wrongemail.com",
    "test@outlook.com",
    "user@domain",
    "name@yahoo.co.uk"
]

# -------- filter + map --------
valid_emails = list(filter(is_valid_email, emails))
domains = list(map(lambda e: e.split("@")[1], valid_emails))

# -------- get user data --------
user_name, user_email = get_user_data()

# -------- print all --------
print("\nName:", user_name)             #Name: alaa
print("Email:", user_email)             #Email: alaa@gmail.com
print("Valid Emails:", valid_emails)    #Valid Emails: ['alaa@gmail.com', 'test@outlook.com', 'name@yahoo.co.uk']
print("Domains:", domains)              #Domains: ['gmail.com', 'outlook.com', 'yahoo.co.uk']


