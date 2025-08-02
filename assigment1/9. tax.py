#The rates of tax on gross salary are as shown below:
#Income                  Tax
#Less than 10,000         Nill
#Rs. 10,000 to 19,999       10%
#Rs. 20,000 to 39,999        15%
#Rs. 40,000 to above          20%
#Write a program to compute the net salary after deducting the tax for the given information

income=int(input("enter the income"))
if income<10000:
    print("nill")
elif income in range (10000, 19999):
    newincome=income-(10/100)*income
    print("the tax is10% and new income becomes:", newincome)
elif income in range(20000,39999):
    newincome=income-(15/100)* income
    print("the tax is 15% and new income becomes:",newincome)
else:
    newincome=income-(20/100)*income
    print("the tax is 20% and new income becomes:",newincome)