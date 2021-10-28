from tkinter import *
import random
from tkinter import messagebox
import time

# GAME DESCRIPTION: This program codes for a color hunt card game. The player gets to flip two cards during each turn in the game, and then if they colors on the cards match, the player scores a point. If the colors do not match, the cards turn over, and they get to turn over another card. The game consists of sixteen cards with eights pairs of colors. The game ends after the player has matched all eight colors. 

#WINDOW SET UP

window = Tk()
window.title("Color Hunt")
#titles webpage


#DEFINE VARIABLES


clickcount = 0 
# how many clicks the user has made
flipped = 0  
# how many card flips the user has made per round, limited to 1 to 2
check1 = ""
#first card checked per round
check2 =""
#second card checked per round
colors = ["white", "blue", "green", "red", "purple", "yellow", "black", "orange"]
#list of the types of cards that can be paired
carddeck = {}
#dictionary of cards and their values in the given game
score = 0
#all games begin with a starting score of zero 
buttons = []

#DEFINE FUNCTIONS

#set up function, where the game board is set up for each game such that every card on a board contains a random color that pairs with exactly one other card with the same color
def setup ():
  unplaced = {"white":2, "blue":2, "green":2, "red":2, "purple":2, "yellow":2, "black":2, "orange":2}
  #dictionary for all the values that have not been assigned to a card, otherwise known as unplaced colors  
  for input in carddeck:
    #for every "card" in the grid,
    random.shuffle(colors)
    #shuffle the list of color values
    if len(colors)>0:
      #if the colors list is not empty,
      carddeck[input]=colors[0]
      #set the current card to the first color value in the list of colors
      unplaced[colors[0]]-= 1
      #remove one count of the color from the unplaced dictionary, because the color has been placed, so there is one less unplaced card

      if unplaced[colors[0]]==0:
      #when both unplaced cards of a color are placed, the color can be deleted from the color dictionary and no longer shuffled for placement
        colors.remove(colors[0])


#flipover function, whenever the user flips over a card, and after two cards are flipped, it checks whether the two cards are the same
def flipover(input):
  global clickcount, flipped, check1, check2
  
  clickcount += 1 
  # add 1 to number of clicks
  flipped += 1
  # add 1 to number of flips per round
  if flipped == 1:
    check1 = input
    input.configure(text = carddeck[input], padx=40, pady=20, state = DISABLED)
    #displays card text
  if flipped ==2:
    check2 = input
    input.configure(text = carddeck[input], padx=41, pady=20, state = DISABLED)
    #displays card text
    window.after(600, checksame)
    #pause 600ms and then run checksame function to check whether they are the same or not
    #restricts to two flips per round
    flipped = 0
    #set flipped back to 0 for next round


#checkssame function checks whether the cards are the same or not by what color text it is
def checksame():
  global  clickcount, score
  if check1['text'] != check2['text']:
    #if they are not the same
    check1.configure(text = "", padx=55, pady=20, state = NORMAL)
    check2.configure(text = "", padx=55, pady=20, state = NORMAL)
    #changes it back to no text
    score += 0
    #score does not change
    message2()
    #run message2
  else:
    #if they are the same
    score += 1
    #score increases by 1
      

    message()
    #run message
    if score == 8:
      #after all cards have been paired
      message3()
      x = clickcount
      """for x in range(40, 80):
        wut do i want from it tho hhh"""
      #run message 3


#message after scoring
def message():
  MsgBox = messagebox.showinfo ('Great Job','You have scored ' + str(score) + ' points.')
  #displays score

#message after missing  
def message2():
  Message = messagebox.askquestion ('Sorry','You missed. So far you have scored ' + str(score) + ' points.' + 'If you want to quit click no and if you want to keep going click yes' )
  #displays score and allows user to choose if they want to continue playing
  if Message == 'no':
    window.destroy()
    #if they do not want to play anymore, closes game

#message after winning
def message3():
  Message = messagebox.showinfo ('Congratulations!','You have won in ' + str(clickcount) + ' clicks. Goodbye!' )
  window.destroy()
  #ends game

#message for instructions on how to play the game
def instructions():
  Message = messagebox.askquestion ('Welcome', 'Welcome to Color Hunt. Click on the cards to see the color behind it and match it with the card with the same color. There are only two colors of each card, and you will only be able to select two cards each time. Good luck! Click yes to get started or no if not interested')
  #provides instructions and asks whether they want to play
  if Message == 'no':
    messagebox.showinfo ('Bye','See you next time!:)')
    window.destroy()
    #if they do not want to, ends game


#DEFINE BUTTONS

card1 = Button(window, padx=55, pady=20, command=lambda: flipover(card1))
carddeck[card1]=""
card2 = Button(window, padx=55, pady=20, command=lambda: flipover(card2))
carddeck[card2]=""
card3 = Button(window, padx=55, pady=20, command=lambda: flipover(card3))
carddeck[card3]=""
card4 = Button(window, padx=55, pady=20, command=lambda: flipover(card4))
carddeck[card4]=""
card5 = Button(window, padx=55, pady=20, command=lambda: flipover(card5))
carddeck[card5]=""
card6 = Button(window, padx=55, pady=20, command=lambda: flipover(card6))
carddeck[card6]=""
card7 = Button(window, padx=55, pady=20, command=lambda: flipover(card7))
carddeck[card7]=""
card8 = Button(window, padx=55, pady=20, command=lambda: flipover(card8))
carddeck[card8]=""
card9 = Button(window, padx=55, pady=20, command=lambda: flipover(card9))
carddeck[card9]=""
card10 = Button(window,padx=55, pady=20, command=lambda: flipover(card10))
carddeck[card10]=""
card11 = Button(window, padx=55, pady=20, command=lambda: flipover(card11))
carddeck[card11]=""
card12 = Button(window, padx=55, pady=20, command=lambda: flipover(card12))
carddeck[card12]=""
card13 = Button(window, padx=55, pady=20, command=lambda: flipover(card13))
carddeck[card13]=""
card14 = Button(window, padx=55, pady=20, command=lambda: flipover(card14))
carddeck[card14]=""
card15 = Button(window, padx=55, pady=20, command=lambda: flipover(card15))
carddeck[card15]=""
card16 = Button(window, padx=55, pady=20, command=lambda: flipover(card16))
carddeck[card16]=""

#setup the grid into a four by four grid
def grid_setup():
  card1.grid(row=4, column=0)
  card2.grid(row=4, column=1)
  card3.grid(row=4, column=2)
  card4.grid(row=4, column=3)
  card5.grid(row=3, column=0)
  card6.grid(row=3, column=1)
  card7.grid(row=3, column=2)
  card8.grid(row=3, column=3)
  card9.grid(row=2, column=0)
  card10.grid(row=2, column=1)
  card11.grid(row=2, column=2)
  card12.grid(row=2, column=3)
  card13.grid(row=1, column=0)
  card14.grid(row=1, column=1)
  card15.grid(row=1, column=2)
  card16.grid(row=1, column=3)

#set up grid
grid_setup() 
#run instructions
instructions()
#run setup 
setup() 

window.mainloop()