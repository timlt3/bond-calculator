# prompts user and takes input for the bonds price, face value (par), coupon payment, time to maturity
class Bond:
    price = str()
    par = str()
    coupon = str()
    maturity = str()
    rate = "" 
    def init(): 
        mybond = Bond() 
        mybond.price = input("price: " )
        mybond.price = float(mybond.price) 

        mybond.par = input("par value: ")
        mybond.par = float(mybond.par) 

        mybond.coupon =  input("coupon payment: ")
        mybond.coupon = float(mybond.coupon)

        mybond.maturity = input("Time to maturity: ")
        mybond.maturity = float(mybond.maturity)
        return mybond

    def print(bond): 
        print("price: ", bond.price, "par value: ", bond.par, "coupon: ", bond.coupon, "maturity: ", bond.maturity, "rate: ", bond.rate) 

    def findrate(b, l, r, t): 
        b.rate = (l + r)/2
        print(b.rate)
        estimate = b.coupon * ((1 - (1/((1 + b.rate)**b.maturity)))/b.rate) + b.par/((1 + b.rate)**b.maturity) 
        print("estimate is", estimate)
        print("estimate - t", estimate -t) 
        print("bprice", b.price)
        print("estimate + t", estimate + t)
        if abs(estimate - t) < abs(b.price) and abs(b.price) < abs(estimate + t):  
            print("HELLOOOOOOOOOOOOOOOOOOOOOOOO THE BLACKS") 
            return(b.rate) 
        elif estimate < b.price:  #yield and price are inversely related
            Bond.findrate(b, l, (l + r)/2, t) 
        Bond.findrate(b, (l + r)/2, r, t) 



#        Bond.estimate(mybond.price, mybond.par, mybond.coupon, mybond.maturity)
#
#
#    def estimate(price, par, coupon, maturity): 
#        rate = 0.1
#
#        estimate = coupon * ((1 - (1/((1 + rate)**maturity)))/rate) + par/((1 + rate)**maturity) 
#        print("estimate: ", estimate)


# "Main function" 
# Find out price, coupon, time to maturity and face value for bond
# binary search to estimate yield
b = Bond.init()
b.rate = Bond.findrate(0, 100, 50)
Bond.print(b)






#SPOTRATE STUFF ##EXTRA CODE ## 
# will need for spotrate calculation later: 
#numRates = maturity - 1 
#    rateList = []
#    for i in range(numRates): 
#        print("rate", i + 1 , "=") 
#        rates = input() 
#        rateList.append(rates)


