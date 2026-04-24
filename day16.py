### Day 16 Simple Program
### Count Even and Odd Numbers
##
##even_count = 0
##odd_count = 0
##
##numbers = []
##
##count = 1
##max_numbers = 5
##
##while count <= max_numbers:
##    num = int(input("Enter a number: "))
##    # skip negative numbers
##    if num < 0:
##        print("Negative skipped")
##        continue
##    # stop if 0 entered
##    if num == 0:
##        print("Zero entered. Stopping.")
##        break
##    # placeholder
##    if num == 1:
##        pass
##    # check even or odd
##    if num % 2 == 0:
##        even_count += 1
##    else:
##        odd_count += 1
##    numbers.append(num)
##    count += 1
##else:
##    print("You entered all numbers")
# Program to print increasing star pattern
##
##rows = 5   # number of lines
##
##for i in range(1, rows + 1):
##    for j in range(i):
##        print("*", end=" ")
##    print()
##print("\nNumbers you entered:")
##
##for i in range(len(numbers)):
##    print("Number", i+1, ":", numbers[i])
##
##print("\nTotal Even numbers:", even_count)
##print("Total Odd numbers:", odd_count)





rows=5

for i in range(1,rows+1):
    for j in range(i):
        print("*",end=" ")
    print()
print("\nNumbers you entered")        
    






















