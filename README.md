# bond-calculator
Given the conventional formula for pricing bonds, it is impossible to directly calculate the yield to maturity of a bond algebraically because the variable is hidden away in a higher order polynomial. 
Hence, the implementation needs to instead approximate the solution with high precision. 
The algorithm used here is binary search, which can approximate any function in logarithmic time. 
