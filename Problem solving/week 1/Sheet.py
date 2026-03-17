#problem:(A) Military Enrollment Check
h,w=map(int,input().split())
if h>=160 and w<=120:
    print("Accepted")
else:
    print("Rejected")

print("End of problem A")
#------------------------------------------------------------------------#
#problem: (B) Bank Account Eligibility Counter
n = int(input())
ages = list(map(int, input().split()))

count = 0
for age in ages:
    if age >= 21:
        count += 1

print(count)
print("End of problem B")
#------------------------------------------------------------------------#
#problem: (C) Factorial
t = int(input())
for _ in range(t):
    n = int(input())
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)
print("End of problem C")
#------------------------------------------------------------------------#    
#problem: (D) Login Attempts
p = input().strip()      
k = int(input())         

success = False

for _ in range(k):
    attempt = input().strip()
    if attempt == p:
        print("Success")
        success = True
        break

if not success:
    print("Locked")
print("End of problem D")
#------------------------------------------------------------------------#    
#problem: (E) Shop Checkout
n = int(input())
prices = list(map(float, input().split()))
S = sum(prices)
T, d = map(float, input().split())

if S >= T:
    S = S * (1 - d / 100)

print(S)
print("End of problem E")
#------------------------------------------------------------------------#
#problem: (F) Array Shift Check
n, k = map(int, input().split())
arr = list(map(int, input().split()))
k = k % n

for _ in range(k):
    last = arr[n - 1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last

for x in arr:
    print(x, end=" ")
print("\nEnd of problem F")
#------------------------------------------------------------------------#    
# problem: (G) Function-Based Calculator
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def divi(a, b):
    return int(a / b)   

a, b, op = input().split()
a = int(a)
b = int(b)

operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': divi
}

if op == '/' and b == 0:
    print("Error")
else:
    print(operations[op](a, b))

print("End of problem G")
#------------------------------------------------------------------------#
# problem: (_Bounce_1) Recover Three Numbers
A, B, C = map(int, input().split())

x = (A + C - B) // 2
y = (A + B - C) // 2
z = (B + C - A) // 2

print(x, y, z)
print("End of problem Bounce 1")
#------------------------------------------------------------------------#
#problem: (_Bounce_2) Clean Title Case Line
s = input()
words = s.split()  
result = ""

for w in words:
    word = w[0].upper() + w[1:].lower()
    result += word

print(result)
print("End of problem Bounce 2")
#------------------------------------------------------------------------#





