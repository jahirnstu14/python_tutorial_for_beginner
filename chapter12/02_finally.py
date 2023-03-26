try:
    a = input("Enter a number: ")
   
    a = int(a)
    if a>6:
        print("enter a greater number than 6")
except Exception as e:
        print(f"your inputed result is error {e}") 
        exit() 
finally:
    print("thanks for playing this game ")  
