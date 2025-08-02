num=int(input("enter a year"))
if (num%4==0 and num%100 !=0 )or (num%400==0):
    print("it is a leap year")
else:
    print("it is not a leap year")