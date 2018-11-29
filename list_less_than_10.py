lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
"""lst_2 = []
for num in lst:
    if num < 5:
        lst_2.append(num)
print(lst_2)"""

num = input("Pick a number.")

lst_2 = []

for x in lst:
    if x < int(num):
        lst_2.append(x)

print(lst_2)