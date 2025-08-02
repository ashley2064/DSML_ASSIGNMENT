#question no.3 and 4(A)If purchased amount is greater than or equal to 1000, discount is 5%
purchase=int(input("enter a purchase amount"))
if purchase==1000 or purchase > 1000:
    discount=int(5/100*purchase)
    print("the discount is 5%:", discount)
else:
    print("no discount can be offered")
#============================================================================================================

#question no.4 (B)If purchased amount is less than 1000, discount is 3%.
if purchase==1000 or purchase < 1000:
    discount = int(3 / 100 * purchase)
    print("the discount is 3%:", discount)
else:
    print("no discount can be offered")
#============================================================================================================

#question no.5(a) If purchased amount is greater than or equal to 5000, discount is 10%
if purchase==1000 or purchase > 5000:
    discount = int(10 / 100 * purchase)
    print("the discount is 10%:", discount)
else:
    print("no discount can be offered")
#============================================================================================================

#5(b):If purchased amount is greater than or equal to 4000 and less than 5000, discount is 7%
if purchase>=4000 or purchase < 5000:
    discount = int(7 / 100 * purchase)
    print("the discount is 7%:", discount)
else:
    print("no discount can be offered")
#============================================================================================================

# question no.5(c) If purchased amount is greater than or equal to 3000 and less than 4000, discount is 5%.
if purchase>=3000 or purchase < 4000:
    discount = int(5 / 100 * purchase)
    print("the discount is 5%:", discount)
else:
    print("no discount can be offered")
#============================================================================================================

#question no.5(d):If purchased amount is greater than or equal to 2000 and less than 3000, discount is 3%
if purchase>=2000 or purchase < 3000:
    discount = int(3 / 100 * purchase)
    print("the discount is 3%:", discount)
else:
    print("no discount can be offered")
#============================================================================================================

#question no.5(e):If purchased amount is less than 2000, discount is 2%
if  purchase < 2000:
    discount = int(2 / 100 * purchase)
    print("the discount is 2%:", discount)
else:
    print("no discount can be offered")
