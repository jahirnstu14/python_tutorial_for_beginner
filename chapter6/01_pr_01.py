text = input("enter the textv :")
spam=False
if("make a lof of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
else:
    spam=False
if(spam):
    print("this is text spam")
else:
    print("this text is not spam")