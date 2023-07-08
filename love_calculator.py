#LOVE-->CALCULATOR
import turtle

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

string_combined=name1 + name2
#convert combined string into lower case.
lower_case=string_combined.lower()
t=lower_case.count('t')
r=lower_case.count('r')
u=lower_case.count('u')
e=lower_case.count('e')
l=lower_case.count('l')
o=lower_case.count('o')
v=lower_case.count('v')
count_true=t+r+u+e
count_love=l+o+v+e
#combine both count_true and count_love to get love percentage.
love=str(count_true) + str(count_love)
true_love=int(love)
if true_love < 20:
    print(f"Your score is {true_love }.")
    turtle.bgcolor("black")
    turtle.pensize(10)
    def txt():
        turtle.up()
        turtle.setpos(-100,90)
        turtle.down()
        #set the text color
        turtle.color("red")
        #write specified text with specified font style and size.
        turtle.write("ENEMIES",font=("verdana",40,"bold"))

    txt()
    turtle.ht()
elif true_love >= 20 and true_love <50:
    print(f"Your score is {true_love }.")
    turtle.bgcolor("black")
    turtle.pensize(10)
    def txt():
        turtle.up()
        turtle.setpos(-100,90)
        turtle.down()
        #set the text color
        turtle.color("lightblue")
        #write specified text with specified font style and size.
        turtle.write("SIBLINGS",font=("verdana",50,"bold"))
        
    txt()
    turtle.ht()
    
elif true_love >= 50 and true_love <= 70:
    print(f"Your score is {true_love}.")
    turtle.bgcolor("black")
    turtle.pensize(2)
    def txt():
        turtle.up()
        turtle.setpos(-100,90)
        turtle.down()
        #set the text color
        turtle.color("white")
        #write specified text with specified font style and size.
        turtle.write("FRIENDS",font=("verdana",40,"bold"))
        
    txt()
    turtle.ht()
    
elif true_love > 70 and true_love < 90:
    print(f"Your score is {true_love}.")
    turtle.bgcolor("black")
    turtle.pensize(2)
    def txt():
        turtle.up()
        turtle.setpos(-100,90)
        turtle.down()
        #set the text color
        turtle.color("pink")
        #write specified text with specified font style and size.
        turtle.write("AFFECTION",font=("verdana",50,"bold"))
        
    txt()
    turtle.ht()
    
else:
    print(f"Your score is {true_love}.")
    turtle.bgcolor("black")
    turtle.pensize(2)
    def curve():
        for i in range(200):
            turtle.right(1)
            turtle.forward(1)
    def txt():
        turtle.up()
        turtle.setpos(-38,90)
        turtle.down()
        #set the text color
        turtle.color("red")
        #write specified text with specified font style and size.
        turtle.write("IT'S LOVE",font=("verdana",12,"bold"))
        
    turtle.speed(0)
    turtle.color("red","pink")
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(113)
    curve()
    turtle.left(120)
    curve()
    turtle.forward(112)
    turtle.end_fill()

    txt()

    turtle.ht()
