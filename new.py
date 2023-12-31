import time
friends_dict = {
  "sahil":"9514646459",
  "amod":"9564659456",
  "pranay":"9584652156",
  "ritik":"9588909436",
}
sorted_friends_dicts = sorted(friends_dict.items())
yes=["yes","y","Y","YES"]
no=["no","n","N","NO"]
a=["a","A"]
b=["b","B"]
c=["c","C"]

e=["e","E"]
def name_check(name):
    if name in friends_dict:
        print("Your friend "+name+" is present with phone number "+friends_dict[name])
    else:
        print(name+" is not present.Do you want to add him in list(y/n)")
        user_input=input("Enter here: ")
        if user_input in yes:
          friend_adder()
        elif user_input in no:
          exiter()
        else :
          print("Invalid input")
          exiter()  
    
        
def friend_adder():
    while True:
     name = input("Enter name of friend : ")
     name = name.lower()
     phone = input("Enter phone number : ")
     friends_dict[name]=phone
     print("Your friend "+name+" is added with phone number "+phone)
     user_input = input("Do you want to add more friends(y/n) : ")
     if user_input in no:
       break
     elif user_input in yes:
       continue
     else:
       print("Invalid input")
       break
    print("here is the updated list")
    time.sleep(1)
    sorted_list()
    exiter()
    
def exiter():
    print(".. .  .   .")
    time.sleep(1)
    print("Exiting the program")
    time.sleep(1)
    print("Thanks for using this program")
def sorted_list():      
  sorted_friends_dicts = sorted(friends_dict.items())
  for key,value in sorted_friends_dicts:
    print(key,value)
while True:
 user_input = input("print list of friends : enter(A) \ncheck if friend is present : enter(B) \nadd friend : enter(c) \nexit : enter(e) \nEnter here : ")
 if user_input in a:
   sorted_list()
   break
 elif user_input in b:
    name = input("Enter name to check : ")
    name = name.lower()
    name_check(name)
    break   
 elif user_input in c:
     friend_adder()
     break
 elif user_input in e:
      exiter()
      break
 else:
     print("Invalid input")
     print("Try again")
     