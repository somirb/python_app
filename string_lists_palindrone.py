#using string reversal
lst1 = input(str("Enter a string: "))
lst2 = lst1[::-1]
if lst1 == lst2:
    print("This is a palindrone.")
else:
    print("This is not a palindrone.")


#refactored
lst = input("Enter a string: ")
if lst == lst[::-1]:
    print("This is a palindrone.")
else:
    print("This is not a palindrone.")