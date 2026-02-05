# problem 1:A. Hello World
#The input: consists of a single line containing a string s and an integer — the name and age of the person (1≤|s|≤100, 1≤n≤100).
#Output a single line with the greeting message in the format "Hello s, you are n years old."
name,age=input().split()
print(f"Hello {name}, you are {age} years old.")


print ("-" * 40)

# problem 2:B. Calculate
# you are given four integers a ,b, c and d print the result of a+b∗c−d
#Input:one line containing four integers a, b, c and d (1≤a,b,c,d≤10^6).
#output: print the result of a+b∗c−d

a,b,c,d=map(int,input().split())
print(a+b*c-d)

print ("-" * 40)

#Problem 3 :Max value
#you are given three integers a, b and c print the maximum value among them. 
#Input: one line containing three integers a, b and c (1≤a,b,c≤10^6).
#Output: print the maximum value among a, b and c.
a,b=map(int,input().split())
c=int(input())
if a>=b and a>=c:
    print(a)        
elif b>=a and b>=c:
    print(b)
else:
    print(c)

print ("-" * 40)


# problem 4:Triangle 1
#You are given an integer n. Print a down right angled triangle that has n rows and n columns. The first row should contain one asterisk, the second row should contain two asterisks, and so on until the nth row which should contain n asterisks.
#Input: only one integer n (1≤n≤100).
#Output:Print the answer according to the required above.

n = int(input())
for i in range(1, n + 1):
    print("*" * i)    

print ("-" * 40)

# problem 5:Do a Replacement
#You are given an array of n numbers and two indexes a,b
#You have to replace the number of index a with the number of index b and replace the number of index b with the number of index a
#Input:First line contains three numbers n,a,b(1≤n≤10^4),(1≤a,b<n),the size of the array and the indexes you have to do a replacement to it.
#Second line contains n numbers the elements of the array (1≤array[i]≤10^6).
#Output:Print the array after doing the replacement.

n, a, b = map(int, input().split())
arr = list(map(int, input().split()))

a -= 1
b -= 1

arr[a], arr[b] = arr[b], arr[a]

print(*arr)
