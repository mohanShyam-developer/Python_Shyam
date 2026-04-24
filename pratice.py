'''try:
    a=9
    b=10
    print(a+b)
except:
    print("error here")
else:
    print("no error in the code")
finally:
    print("the try except block is defined")            '''

'''
Except block
- - - - - - - - - - - -
-  - > This block will take care of any errors.
ex
- - - -
except :
        print("This block can handle error")

else block
finally block

try:
       a = 9
       b = 10
       print(a + c)
except:
       print("Error here")
else:
       print("No error in the code")
finally:
       print("The try-except block is finished")
'''

try:
       num = int(input("Enter a number: "))
       num = int(input("Enter a number: "))
       result = num / num_2
except ValueError:
       print("Pls enter a valid number")
except ZeroDivisionError:
       print("Cannot divide by zero")
else :
       print(f"Result = {result}")
finally:
       print("Program is completed")
       
    