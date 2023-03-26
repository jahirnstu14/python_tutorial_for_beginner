def factorial(n):
    product=1
    for i in range(n):
        product=product* (i+1)
    return product

def factorialrecursion(n):
    if n==0 or n==1:
        return 1
    return n * factorialrecursion(n-1)

#f=factorial(5)
f=factorialrecursion(5)
print(f)
