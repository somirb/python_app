def divisors():
    user_num = input("Pick a number: ")
    lst = range(1, int(user_num) + 1)
    #print(lst)
    for num in lst:
        if int(user_num) % num == 0:
            print(num)
divisors()