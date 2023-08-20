#Leap Year Checker

# Problem
''' Check whether Year is leap or not  '''

# Soltion

print("*** Welcome to the Leap Year checker ***\n")
#Asking user to enter the year to be checked
year = int(input("Which year do you want to check?\n Year: "))

print()
# result
if(year%4 == 0):
   
    if(year%100 != 0):
        print(f"{year} is a Leap year.")
        
    else:
        if(year%400 == 0):
         print(f"{year} is a Leap year.")
        else:
         print(f"{year}Not leap year.")    
        
else:
    print(f"{year}Not leap year.")   

print()
print("*** Thank you ***")