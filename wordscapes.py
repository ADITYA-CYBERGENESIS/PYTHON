import time
letters = [['h', 'o', 'l', 'i', 'd', 'a', 'y'],

           ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g'],

           ['b', 'o', 'o', 't', 'c', 'a', 'm', 'p'],

           ['f', 'l', 'o', 'w', 'c', 'h', 'a', 'r', 't'],

           ['w', 'o', 'r', 'd', 's', 'c', 'a', 'p', 'e', 's']]

words = [["hi", "hay", "day", "had", "lay", "dal", "lad", "lid", "hold", "lady", "hail"],

         ["go", "an", "in", "no", "on", "map", "mom", "gap", "gag", "pig", "man", "ping",

          "pong", "pram", "prom", "ramp"],

         ["am", "at", "to", "cab", "cap", "cob", "cop", "map", "mop", "act", "bat", "camp",

          "comb", "boom", "pact", "atom"],

         ["of", "at", "or", "to", "caw", "cow", "how", "who", "calf", "claw", "flaw", "flow",

          "fowl", "wolf", "crow", "half"],

         ["we", "do", "as", "cap", "caw", "cop", "cow", "paw", "cod", "dew", "pad", "cape",

          "cope", "crap", "crew", "crop", "pace"]]
lives = 5
guess_correct = 0
level = 1

print("Welcome to the game of wordscapes")
print("In this game you have to gues correct word from characters provided to you \nAfter 3 correct guess you will win a level\nAfter 5 wrong guess you will lose the game\ngame consist of 5 levels ")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
i = 0
score=0
while level<6:
 print(f"Starting level {level}")
 print(letters[i])
 guess_to_go = 3
 double_checker=""
 while guess_to_go>0:
     user_guess=input("Enter the word you guessed : ")
     if user_guess == double_checker:
         print("you guess same word twice")
         lives =lives-1
         print(f"you have lives {lives} remaining.")
         score=score+1
     elif user_guess in words[i]:
         guess_to_go=guess_to_go-1
         print(f"You guessed correct word {user_guess}")
         if guess_to_go<1:
            continue
         else:
           print(f"{guess_to_go} remaining to win the level")
     else:
         print(f"Your guess {user_guess} is wrong ")
         lives =lives-1
         print(f"you have lives {lives} remaining.")
         score = score + 1
     if lives == 0:
      print("Oops!All lives lost")
      print(f"Your score is {score}")
      print("Better luck next time")
      exit()
 while level<5:
      user_choice=(input("Do you want to play next level (Y/N)")).lower()
      if user_choice == "y":
          level = level + 1
          break
      elif user_choice == "n":
          print(f"Thanks for playing game.Your score is {score}")
          exit()
      else:
          print("Tryagain wrong choice")

 i = i+1
