import random
user_input= None
rand_num = random.randint(1,5)
while rand_num!=user_input: 
  user_input = int(input("enter a number: "))
  if rand_num==user_input:
     print("you won the lottery")
  
  else :
     print("try again")
