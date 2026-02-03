# use re module to validate email addresses and handle exceptions using try-except block
import re   

def email_validation(email):
    try:
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(regex, email) is not None
    except Exception:
        return False


emails = [
    "alaa@gmail.com",
    "wrongemail.com",
    "test@outlook.com",
    "user@domain",
    "name@yahoo.co.uk"
]

results = map(email_validation, emails) 
print(list(results)) #[True, False, True, False, True]
