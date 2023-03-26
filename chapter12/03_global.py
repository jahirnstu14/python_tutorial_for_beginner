a = 54 
def fun1():
    global a
    print(f"the global valu is 1:{a} ")
    a = 8
    print(f"the global varible will b e change2: {a}")
fun1()
print(f"the global valuable will be {a}")
