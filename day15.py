# Password Check and Reset with Retry

##saved_password = "Python123"
##password = input("Enter your password: ")
##if password == saved_password:
##    print(" Password is correct. Access Granted!")
##else:
##    print("Incorrect Password.")
##    choice = input("Do you want to reset password? (yes/no): ")
##    if choice.lower() == "yes":
##        while True:
##            new_password = input("Enter new password: ")
##            if len(new_password) >= 6:
##                saved_password = new_password
##                print(" Password reset successful!")
##                # Login again
##                password = input("Enter your new password again: ")
##                if password == saved_password:
##                    print(" Login Successful!")
##                else:
##                    print(" Password does not match.")
##                break  # exit loop
##            else:
##                print("️ Password too short! Use at least 6 characters.")
##    else:
##        print("Access Denied.")

'''
for j in range(1,10):
    print(j)
    if j==5:
        break

list_=[1,2,3,4]
for i in list_:
    print(i)
    if i==4:
        break
list_=[12,3,4,5,6,7]
for i in list_:
    print(i)
    if i == 4:
        break

for i in range(1,21):
    print(i)
    if i==5:
        continue'''
    
##for j in range(1,100):
##    print(j)
##    print("shyam")

user=int(input("enter limit:"))
num1=0
num2=1
print(num1,num2,end=" ")
for i in range(user+1):
    num3=num1+num2
    num1=num2
    num2=num3
    print(num3,end=" ")

   





























    
