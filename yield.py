# l and r define the lower and upper bound for rate
def findyield(price, par, coupon, maturity, l, r): 
    rate = (l + r)/2
    estimate = coupon * ((1 - (1/((1 + rate)**maturity)))/rate) + par/((1 + rate)**maturity) 

    if(estimate - precision < price < estimate + precision): 
        return rate
    if(estimate < price): 
        return findyield(price, par, coupon, maturity, l, rate)
    else: 
        return findyield(price, par, coupon, maturity, rate, r)

#PROMPT USER FOR INPUT
print("This calculator finds the yield to maturity of a bond accurate to within one basis point (0.0001)")
print("Please enter the bond details as follows: price, face par value, coupon, maturity")
print("This calculator assumes annual payment in accordance with most UNSW Finance courses")

precision = .0001
price = float(input("price (dollars): "))
par = float(input("par (dollars): "))
coupon = float(input("coupon (dollars): "))
maturity = int(input("time to maturity (years): "))

#FUNCTION CALL and OUTPUT
rate = findyield(price, par, coupon, maturity, 0, 1) 
print("the YTM is: %.4f" % rate)
    
