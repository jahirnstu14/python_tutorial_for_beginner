while(True):
    print("press q to quit")
    a = input("Enter a number: ")
    if a == 'q':
        break
    try:
        a = int(a)
        if a>6:
            print("enter a greater number than 6")
    except Exception as e:
        print(f"your inputed result is error {e}")  
print("thanks for playing this game ")
