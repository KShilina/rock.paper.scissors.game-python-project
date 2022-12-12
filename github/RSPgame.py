# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 21:54:52 2022

@author: maild
"""
# Import Required Library
import tkinter as tk
import random

# Initialising score to 0
user=''
computer='' 
user_count= 0
computer_count= 0

#defining the function if player selected rock
def result_rock():
   global user_count
   global computer_count

   user="rock"
   computer = ["rock", "paper", "scissors"]
   computer_choice=random.choice(computer)
   print("Computer choice:",computer_choice)
 
   if user==computer_choice:
     print("It's a tie")
   elif  user == 'rock' and computer_choice=='paper':
     print('✋ beat the 🤛',"computer win this round")
     computer_count = computer_count+1
   elif  user == 'rock' and  computer_choice=='scissors':
     print('🤛 beat the ✌️,user win this round')
     user_count=user_count+1
   elif  computer_choice == 'rock' and user=='paper':
     print('✋ beat the 🤛',"user win this round")
     user_count = user_count+1
   elif  computer_choice == 'rock' and  user =='scissors':
     print('🤛 beat the ✌️',"computer win this round")
     computer_count = computer_count+1
     
    #implementing console output to the user's interface screen  
   text_area=tk.Text(master=window,height=12,width=60,bg='#FFFFE1')
   text_area.grid(column=1,row=4)
   answer="Your Choice:{uc}\nComputer's Choice :{cc}\n Your Score:{u}\n Computer Score: {c}".format(uc=user,cc=computer_choice,u=user_count,c=computer_count)
   text_area.insert(tk.END,answer)
   total_score_user= user_count 
   total_score_computer = computer_count
   
   #Set a condition when user or computer hits score=3, annoucment set to Game is over.
   if total_score_user==3 or total_score_computer==3:
       text_area.insert(tk.END,"\nGame is Over!")
       print("Game is over!")
   

#defining the function if player selected paper
def result_paper():
    global user_count
    global computer_count
    user = "paper"
    computer = ["rock", "paper", "scissors"]
    computer_choice=random.choice(computer)
    print("Computer choice:",computer_choice)
    if user == 'paper' and  computer_choice=='rock':
      print("✋ beat the 🤛,user win this round")
      user_count = user_count+1
    elif user == 'paper' and  computer_choice=='scissors':
      print("✌️ beat the ✋,computer win this round")
      computer_count = computer_count+1
    elif computer_choice == 'paper' and  user=='rock':
      print("✋ beat the 🤛,computer win this round")
      computer_count = computer_count+1
    elif computer_choice == 'paper' and  user=='scissors':
      print("✌️ beat the ✋,user win this round")
      user_count = user_count+1
    
      
    #implementing console output to the user's interface screen  
    text_area=tk.Text(master=window,height=12,width=60,bg='#FFFFE1')
    text_area.grid(column=1,row=4)
    answer="Your Choice:{uc}\nComputer's Choice :{cc}\n Your Score:{u}\n Computer Score: {c}".format(uc=user,cc=computer_choice,u=user_count,c=computer_count)
    text_area.insert(tk.END,answer)
    total_score_user= user_count 
    total_score_computer = computer_count
    
    #Set a condition when user or computer hits score=3, announcement set to"Game is over".
    if total_score_user==3 or total_score_computer==3:
        text_area.insert(tk.END,"\nGame is Over!")
        print("Game is over!")
        
#defining the function if player selected scissors      
def result_scissors():
    global user_count
    global computer_count
    user = "scissors"
    computer = ["rock", "paper", "scissors"]
    computer_choice=random.choice(computer)
    print("Computer choice:",computer_choice)
      
    if user=='scissors' and computer_choice=='rock':
       print('🤛 beat the ✌️, computer win this round')
       computer_count = computer_count+1
    elif user=='scissors' and computer_choice== 'paper':
      print('✌️ beat the ✋, user win this round')
      user_count = user_count+1
      
      
     #implementing console output to the user's interface screen  
    text_area=tk.Text(master=window,height=12,width=60,bg='#FFFFE1')
    text_area.grid(column=1,row=4)
    answer="Your Choice:{uc}\nComputer's Choice :{cc}\n Your Score:{u}\n Computer Score: {c}".format(uc=user,cc=computer_choice,u=user_count,c=computer_count)
    text_area.insert(tk.END,answer)
   
    total_score_user= user_count 
    total_score_computer = computer_count
    
    #Set a condition when user or computer hits score=3, annoucment set to Game is over.
    if total_score_user==3 or total_score_computer==3:
        text_area.insert(tk.END,"\nGame is Over!")
        print("Game is over!")
    
    
# defining the function for Reset The Game    
def reset_game():
    global user_count
    global computer_count
    user_count=0
    computer_count=0
    
    #create a pop-up window with announcement: "Welcome to new round"
    text_area=tk.Text(master=window,height=5,width=26,fg="black", bg="#ffa500",font=('Arial Bold',10))
    text_area.grid(column=1,row=4)
    answer="***Welcome to new round***"
    text_area.insert(tk.END,answer)
    
    
# Create Object
window = tk.Tk()
# Set title
window.title("Rock Paper Scissors Game") 


#creating the window
window.columnconfigure([0,1,2], minsize=250,)
window.rowconfigure(0, minsize=100)


# Add Labels
label1 = tk.Label(text="Player",bg="#FF8C00", fg="black",font =(
  'Verdana', 15))
label1.grid(row=0, column=0, sticky="nsew")

label4 = tk.Label(text="",bg="#333333", fg="white", font =(
  'Verdana', 15))
label4.grid(row=1, column=0,sticky="nsew")

label5 = tk.Label(text="VS",bg="#333333", fg="white",font =(
  'Verdana', 15))
label5.grid(row=0, column=1, sticky="nsew")
label6 = tk.Label(text="",bg="#333333", fg="white",font =(
  'Verdana', 15))
label6.grid(row=1, column=1,sticky="nsew")

label2 = tk.Label(text="Computer",bg="#FF8C00", fg="black",font =(
  'Verdana', 15))
label2.grid(row=0, column=2, sticky="nsew")
label4 = tk.Label(text="",bg="#333333", fg="white", font =(
  'Verdana', 15))
label4.grid(row=1, column=2,sticky="nsew")



#butoons to choose (rock,paper,scissors)
btn_rock = tk.Button(master=window, text="Rock",font =(
  'Verdana', 15),command=result_rock)
btn_rock.grid(row=3, column=0, sticky="nsew",padx=10, pady=10)


btn_paper = tk.Button(master=window, text="Paper",font =(
  'Verdana', 15),command=result_paper)
btn_paper.grid(row=3, column=1, sticky="nsew",padx=10, pady=10)


btn_scissors = tk.Button(master=window, text="Scissors",font =(
  'Verdana', 15),command=result_scissors)
btn_scissors.grid(row=3, column=2, sticky="nsew",padx=10, pady=10)

#reset game button
btn_reset=tk.Button(master=window, text="Reset Game",fg='#CC5800',font =(
  'Verdana', 15),command=reset_game)
btn_reset.grid(row=5, column=1, sticky="nsew",padx=10, pady=10)

# Execute Tkinter
window.mainloop()
