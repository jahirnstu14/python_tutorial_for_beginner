a = int(input("Enter the first value of a :"))
b = int(input("Enter the first value of b :"))
try:
    t=a/b
    print(t)
except ZeroDivisionError as f:
    print(f"the zerodivisions error is occured {f}")