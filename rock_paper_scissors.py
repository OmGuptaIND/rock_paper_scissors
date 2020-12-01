import random
from os import system as sys
from time import sleep
print("Lets Play Rock , Paper , Scissors....")
options = ["r","p","s"]
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
class game():
    def __init__(self,name,user_score=0,comp_score=0):
        self.name = name
        self.user_score = user_score
        self.comp_score = comp_score
    def score(self):
        print(f"{self.name} : {self.user_score}\nComputer:{self.comp_score}")
    def play_ch(self,ch,player="Computer"):
        if ch =="r":
            return (f"{player} played\n{rock}")
        elif ch == "p":
            return (f"{player} played\n{paper}")
        else:
            return (f"{player} played\n{scissors}")        
    def comp_ch(self):
        random.shuffle(options)
        ch = random.choice(options)
        print(self.play_ch(ch))
        return ch
    def user_ch(self):
        while(True):
            ch = input("Select from Rock(r) , Paper(p) or Scissior(s) ...").lower()[0]
            if ch not in options:
                print("Wrong choice Select Only from Rock(r) Paper(p) Scissors(s)")
                continue
            else:
                print(self.play_ch(ch,self.name))
                return ch
                break
    def check_win(self , user_ch , comp_ch):
        if user_ch=="r" and comp_ch=="s":
            print(f"Rock Destroy Scissors ... {self.name} Wins") 
            self.user_score+=1 
        elif user_ch=="s" and comp_ch=="r":
            print(f"Rock Destroy Scissors ... Computer Wins") 
            self.comp_score+=1

        elif user_ch=="p" and comp_ch=="s":
            print(f"Scissors Destroy Paper ... Computer Wins") 
            self.comp_score+=1 
        elif user_ch=="s" and comp_ch=="p":
            print(f"Scissors Destroy Paper ... {self.name}  Wins") 
            self.user_score+=1 

        elif user_ch=="p" and comp_ch=="r":
            print(f"Paper Stops Rock ... {self.name} Wins")  
            self.user_score+=1 
        elif user_ch=="r" and comp_ch=="p":
            print(f"Paper Stops Rock ...  Computer Wins")  
            self.comp_score+=1   
        else:
            print("its a Draw")    

user_name = input("Enter Your Name: ").capitalize()
rps = game(name=user_name)
chances = 0
while chances<3:
    choice_user = rps.user_ch()
    rps.play_ch(choice_user)
    
    choice_comp = rps.comp_ch()
    rps.play_ch(choice_comp)
    
    rps.check_win(choice_user,choice_comp)
    rps.score()

    sleep(5)
    sys("cls")
    chances+=1
if rps.user_score>rps.comp_score:
    print(f"Yippe You win {rps.name} by {rps.user_score} : {rps.comp_score} ")    
else:
    print(f"Ohh Computer Wins by {rps.user_score} : {rps.comp_score} ... We Created them never Forget it...")   