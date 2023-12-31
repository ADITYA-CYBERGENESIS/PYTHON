def multiply(number_list):
    res = 1
    for num in number_list:
        res *= num
    print("Multiplication of all numbers in the list: ",res)

number_list = [1,8,6,2,11,2, 3,5, 4, 5]
multiply(number_list)
