# for i in range(101):
#     if i==0:
#         print(i ,"is not even or odd")
#     elif i%2==0:
#         print(i,"is even")    
#     else:
#         print(i,"is odd")
# i=1
# while i<=5:
#     for j in range(3):
#         print("*",end=" ")
#     print()    
#     i+=1

# myself="i am best web developer"
# print(myself)
# print(myself[5])

# myself_multine="""i 
# am 
# best web developer"""
# print(myself_multine)
# print(myself_multine[-2])
# j=0
# f=0
# k=0
# strange="sdf52$"

# for i in range(len(strange)):
#     if strange[i].isalpha():
#         j=j+1
#     elif strange[i].isdigit():
#         f=f+1
#     else :
#         k=k+1
# print("alphabet =",j,"|", "digit = ",f,"|","special characters =",k)     

# a="HELLO WORLD"   
# print(a[-12])

# i=1
# while i!=11:
#     print("i")

# proname =["python","java","c++","php","javascript"]

# print(proname)
# print(proname[-1])
# print(proname[2:4])
# list=[1,2,3,4,5,6,7]
# list2=[]
# print(list2)
# list=list(range(7,100,3))
# print(list)
# first_floor=list(range(101,111))
# second_floor=[1,2,3,4,5,6,7,8,9,10]
# for i in range(len(first_floor)):
#     second_floor[i]=first_floor[i]+100
#     i=i+1    
# print(second_floor)

# name_list=["aditya","vijay","rajesh","suresh"]

# for i in range(len(name_list)):
#     name_list[i]=name_list[i].upper()
# print(name_list)    
# num_list=[5,10,15,20,25]
# j=1
# for i in range(len(num_list)):
#     j=j*num_list[i]
#     i+=1
# print(j)

# list_1 =list(range(1,12))
# print(list_1)
# list_1.append(12)
# print(list_1)
# list_1.insert(6,13)
# print(list_1)
# print(len(list_1))
# list_1.remove(13)
# print(list_1)
# list_1.pop(0)
# print(list_1)

# print(sum(list_1))
# print(max(list_1))
# print(min(list_1))

# list_1.append([1,2,3])
# print(list_1)

# print(list_1[11][2]) 
# tuple_range=tuple(range(1,11))
# tuple_list=(1,2,3,4,5)
# print(tuple_list)
# print(tuple_range)
# print(len(tuple_range))
# print(tuple_range.count(2))
# print(tuple_range.index(3))
#set
# set_list=set(range(1,11))
# print(set_list)
# set_list.remove(9)
# print(set_list)
# dictionary 
# emp_dict={
#     "a":100,
#     "b":200,
#     "c":300
    
# }
# print(emp_dict.clear())

# trial_txt="hello my name is {name}".format(name="oreo")

# print(len(trial_txt))

# dict_1={
#     0:10,
#     1:20,
#     2:30   
# }
# print(dict_1)

# hw_list=list(range(100,501,100))
# print(hw_list)
# hw_list_reverse=list(reversed(hw_list))
# print(hw_list_reverse)
# hw_list_reverse_m2=list(range(500,99,-100))
# print(hw_list_reverse_m2)

# sq_root_list=list(range(1,6))
# print(sq_root_list)
# sq_list=list(sq_root_list)
# print(sq_list)
# for i in range(len(sq_list)):
#     sq_list[i]=sq_list[i]*sq_list[i]
#     i+=1
# print(sq_list)

# summ=int(input("enter a number: ")) #4
# temp=0
# list_1=list(range(1,summ+1))  
# for i in range(len(list_1)): 
#     temp=temp+list_1[i]
#     i+=1
# # print(temp)    

# user_input=input("enter a number: ")
# print(len(user_input))
# user_input=int(user_input)
# print(type(user_input))
# count=0
# while user_input!=0:
#     user_input=user_input//10
#     count+=1
# print(count)

# dict_1={
#     0:10,
#     1:20,
#     2:30}
# dict_2={
#     5:50,
#     6:60
# }
# dict_3={**dict_1,**dict_2}
# print(dict_3)

# function

# num1=int(input("enter a number: "))
# num2=int(input("enter a number: "))
# num3=int(input("enter a number: "))
# def add_subtract(num1,num2,num3):
#     num10=(num1-num2)+num3
#     print(num10)
#     return num10
    
    
# num10=add_subtract(num1,num2,num3)    
# print(num10)

    
# def info(name,age,marks,):
#     print("name:{},age:{},marks:{}".format(name,age,marks))
#     # postion based value allotment

# info("aditya",20,90)    

# def student_info(name="not given",age="not given",marks="not given",city="not given"):
#     print("name:{},age:{},marks:{},city:{}".format(name,age,marks,city))

# student_info("aditya",20,90,"pune")    
# student_info()
    
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)   

# print(factorial(999))     
# user_input=int(input("enter a number: "))

# def armscheck(user_input):
#     temp_num=user_input
#     sum=0
#     while(temp_num>0):
#      last_digit=temp_num%10
#      sum+=(last_digit**len(str(user_input)))
#      temp_num=temp_num//10
#     return sum

# sum=armscheck(user_input)

# print(sum)
# if sum==user_input:
#     print("armstrong number")
# else:
#     print("not armstrong number")   
    
# user_input=input("enter a word: ") 

# temp_word=user_input[::-1]#string reverse
# print(temp_word)

# if user_input==temp_word:
#     print("palindrome")
# else:
#     print("not palindrome")   
# 
# 
# 
# 
# 
# 
# 
# count=0
# for i in range(1,10):
#     count+=1
#     for j in range(1,count+1):
#         print(i,end="")
#     print()


# ########### class and objects
# class laptop:
#     def laptop_config(self):
#         print("16gb 512gb ssd")
# laptop=laptop()
# laptop.laptop_config()  
        
# ############INIT -SELF CALLING FUNCTION########## need to pass in obj to run init itself without calling init function

# class learning_init:
#     def __init__(self):
#      print("hello") 
# init_obj=learning_init()     

# class dog:
#     def __init__(self,name,age,color,breed):
#         self.name=name
#         self.age=age
#         self.color=color
#         self.breed=breed
#     def bark(self):
#         print("woof woof here are details of dog \nname: {} \nage: {} \ncolor: {} \nbreed: {}".format(self.name,self.age,self.color,self.breed))
        
 
# letcall=dog("rocky","2.6 years","golden","labrador retriever")
# letcall.bark()

########## oops ---inheritance
# class Animal:
#     name=""
#     def eat(self):
#         print("eating")

# class Dog(Animal):
#     def display(self):
#         print("{} is eating".format(self.name))

# dog=Dog()
# dog.name="rocky"
# dog.eat()
# dog.display()

# class grandfather:
#     def grandfather(self):
#         print("i have house")
# class father(grandfather):
#     def father(self):
#         print("i have car") 
# class son(father):
#     def son(self):
#         print("i have both")            
# son1=son()
# son1.father()
# son1.grandfather()
# # son1.son()        
# user_input1=int(input("enter a number1: "))
# user_input2=int(input("enter a number2: "))
# print(user_input1+user_input2)
# user_input3=input("enter a word: ")
# user_input4=input("enter a word: ")
# print(user_input3+user_input4)
# str="hello"
# print(len(str))
# list=list(range(1,11))
# print(len(list))
# dic={"a":100,"b":200,"c":300}
# print(len(dic))
# x=5
# def add(x):
#     if x == 1:
#         return x
#     else:
#         return x + add(x - 1)
# add1=add(x)
# print(add1)  

# user_input=int(input("enter a number: "))
# counter=user_input*2
# counter1=1
# for i in range(user_input+1):
#     print("*"*counter1,end="")
#     print(" "*counter,end="")
#     print("*"*counter1)
#     counter1+=1
#     counter-=2
####### try except finally
# a= 10
# b=2
# def divide():
#   print("file opened")
#   try:
#       print(a/b)
#   except Exception:
#       print("error zero")  
#   finally:
#       print("file closed")      

# divide()