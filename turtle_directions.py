'''Homeowork 09: Modules & Files
Lorrayya Williams (llw5)
CS 108
April 6, 2018'''


#import modules
import turtle, sys

file = input("Enter a File Name:")
bob = turtle.Turtle()
window = turtle.Screen()


with open(file) as directionsforturtle:
    for line in directionsforturtle:
        directions_split = line.strip().split()
        if directions_split == []:
            continue
        else:
            #checks for penup command and executes if there
            if directions_split[0] == 'penup':
                bob.penup()
                
            #checks for pendown command and executes if there
            elif directions_split[0] == 'pendown':
                bob.pendown()
                
            #Checks for color command and executes
            elif directions_split[0] == 'color':
                if directions_split[1] in ['green', 'red', 'pink', 'purple', 'black', 'blue']:
                    bob.color(directions_split[1])
                    
            #Checks for goto command and executes if there
            elif directions_split[0] == 'goto':
                if (directions_split[1].isdigit() or directions_split[1][1:].isdigit()) and (directions_split[2].isdigit() or (directions_split[2][1:].isdigit())):
                    if len(directions_split[1]) > 2:
                           if (directions_split[1][1:] == '-') and (directions_split[2][1:] == '-'):
                                bob.goto(directions_split[1],directions_split[2])
                    else:
                        bob.goto(int(directions_split[1]),int(directions_split[2]))
            
            #checks for point command and draws dot
            elif directions_split[0] == 'point':
                if (5 < int(directions_split[1]) < 20) and (directions_split[2].isdigit() or directions_split[2][1:].isdigit()) and (directions_split[3].isdigit() or (directions_split[3][1:].isdigit())):
                    if len(directions_split[1]) > 2:
                           if (directions_split[2][1:] == '-') and (directions_split[3][1:] == '-'):
                                bob.dot(directions_split[1],directions_split[2], directions_split[3])
                    else:
                        bob.goto(int(directions_split[2]),int(directions_split[3]))
                        bob.dot(int(directions_split[1]))
                
            #checks for comment         
            elif directions_split[0][0]!= '#':
                continue
window.exitonclick()