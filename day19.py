##def validate_pin():
##    remaining_attempts=3
##    while remaining_attempts>0:
##        user_pin=input("enter 4 digit pin:")
##        if len(user_pin)==4 and user_pin==user_info['ATM PIN']:
##           print(" Welcome to the ATM")
##           return True
##        else:
##            remaining_attempts -=1
##            if remaining_attempts>0:
##                print(f"Invalid PIN. Attempts left : {remaining_attempts}")
##            else:
##                print("card blocked. Please contact customer care")
##                return False
##
##user_info={
##    "name":"Mohan Shyam",
##    "ATM PIN":"7700",
##    "state":"Andhra Pradesh"
##    }
####validate_pin()
##
##any="python is a language"
##vowel_list=[]
##cons_list=[]
##def vowel_con(any,vowel_list,cons_list):
##    for j in any:
##        if j in "aeiouAEIOU":
##            vowel_list.append(j)
##        else:
##            cons_list.append(j)
##    print(f"{vowel_list} these are all vowel in the string")
##    print(f"{cons_list} these are all cons in the string")
##vowel_con(any,vowel_list,cons_list)

##any=lambda so:so+10
##print(any(8))

##
##add=lambda x:x+10
##print(add(5))
##
##mul=lambda y:y*2
##print(mul(5))
##
##sq_no=lambda z:z**3
##print(sq_no(5))
##
##
##add_2=lambda a,b:a+b
##print(add_2(3,5))
##
##div=lambda c:c/2
##print(div(10))
##
##sub=lambda d:d-5
##print(sub(10))
##
##even_odd= lambda x: "even"  if x%2==0  else "odd"
##print(even_odd(5))
##
##old_list=[1,2,3,4,5]
##new_list=[j for j in old_list if j%2==0]
##print(new_list)





# Create List
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)


# 1. append() — Add item at end
numbers.append(60)
print("\nAfter append(60):", numbers)


# 2. insert() — Add item at specific position
numbers.insert(1, 15)
print("After insert(1, 15):", numbers)


# 3. extend() — Add multiple items
numbers.extend([70, 80])
print("After extend([70, 80]):", numbers)


# 4. remove() — Remove specific item
numbers.remove(30)
print("After remove(30):", numbers)


# 5. pop() — Remove last item
numbers.pop()
print("After pop():", numbers)


# pop(index)
numbers.pop(2)
print("After pop(2):", numbers)


# 6. index() — Find position
pos = numbers.index(40)
print("Index of 40:", pos)


# 7. count() — Count occurrences
numbers.append(20)
count_20 = numbers.count(20)
print("Count of 20:", count_20)


# 8. sort() — Sort list
numbers.sort()
print("After sort():", numbers)


# sort descending
numbers.sort(reverse=True)
print("After sort(reverse=True):", numbers)


# 9. reverse() — Reverse list
numbers.reverse()
print("After reverse():", numbers)


# 10. copy() — Copy list
copy_list = numbers.copy()
print("Copied List:", copy_list)


# 11. clear() — Clear list copy
copy_list.clear()
print("After clear() copied list:", copy_list)


# ---------- Additional Useful Programs ----------

# Find Largest Number
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("\nLargest Number:", largest)


# Find Smallest Number
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest Number:", smallest)


# Sum of List
total = 0

for num in numbers:
    total += num

print("Sum of List:", total)


# Average of List
average = total / len(numbers)
print("Average of List:", average)


# Count Even and Odd Numbers
even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even Count:", even)
print("Odd Count:", odd)


# Remove Duplicates
duplicates = [1, 2, 2, 3, 4, 4, 5]

unique = []

for num in duplicates:
    if num not in unique:
        unique.append(num)

print("\nOriginal with duplicates:", duplicates)
print("After removing duplicates:", unique)


# Reverse List Without reverse()
rev = []

for num in numbers:
    rev.insert(0, num)

print("Reverse without reverse():", rev) 

















































































































































