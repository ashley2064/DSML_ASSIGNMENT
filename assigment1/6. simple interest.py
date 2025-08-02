# question no.6:If balance is greater than 99999, interest is 7 %
balance=float(input("enter the balance: "))
time=int(input("enter the time:"))
if balance>99999:
    interest=(7/100)  #interest=7%
    SI=(balance*time*interest)/100
    print("the interest is 7%  and the SI is", SI)
else:
    print("no interest")
#============================================================================================================
# question no.6 (B):If balance is greater than or equal to 50000 and less than 100000 interest is 5 %
if balance>=50000 or balance<100000:
    interest=(5/100)  #interest=5%
    SI=(balance*time*interest)/100
    print("the interest is 5%  and the SI is", SI)
else:
    print("no interest")
#============================================================================================================
#question no.6(C):If balance is less than 50000, interest is 3%
if balance<50000:
    interest=(3/100)  #interest=3%
    SI=(balance*time*interest)/100
    print("the interest is 3%  and the SI is", SI)
else:
    print("no interest")

#============================================================================================================
#============================================================================================================
