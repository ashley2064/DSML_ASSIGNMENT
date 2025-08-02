n = int(input("enter a mumber"))
reversed=0
while (n != 0):
    remainder = n % 10
    reversed = reversed * 10 + remainder
    n /= 10

if n == reversed:
    print("it  is a palindrome.")
else:
    print("it is not a palindrome.")
