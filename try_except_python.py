try:
    number = int(input("enter a number: "))
    print(number)
    value = 10/0
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
    
    
