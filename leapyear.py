n=int(input("Enter a year"))
if((n%100!=0 and n%4==0) or (year%400==0)):
    print("leap year")
else:
    print("not a leap year")
