https: // www.geeksforgeeks.org/program-to-find-lcm-of-two-numbers/


function primeFactors(n){
    var factors = [],
    divisor = 2

    while(n > 2){
        if(n % divisor == 0){
            factors.push(divisor)
            n = n / divisor
        }
        else{
            divisor++
        }
    }
    return factors
}

> primeFactors(69)
= [3, 23]


# https: // www.geeksforgeeks.org/program-to-find-lcm-of-two-numbers/
# Python program to find LCM of two numbers

# Recursive function to return gcd of a and b


def gcd(a, b):
	if(a == 0):
      return b
    return gcd(b%a,a)

# Function to return LCM of two numbers
def lcm(a,b):
	return (a / gcd(a,b))* b

# Driver program to test above function
a = 15
b = 20
print('LCM of', a, 'and', b, 'is', lcm(a, b))

# This code is contributed by Danish Raza
