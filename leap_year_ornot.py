num=int(input("enter year"))

if num%4==0:
    if num%100==0:
        if num%400==0:
            print("leap year")
        print("leap year")
    print("leap year")  
    
else:
    print("not leap year")

