import turtle
from random import randint
import time

print('Welcome to the WHEEL OF FORTUNE!!!! START THE GAME.....THE WHEEL WILL SPIN AUTOMATICALLY!!!!ALL THE BEST')

tw=turtle.Screen()
tw.setup(1050,700)
turtle.title('Welcome to the WHEEL OF FORTUNE ')
turtle.speed(0)

colors = ['red','blue','yellow','green','purple','grey','orange','violet',
          'pink','black','red','blue','yellow','white','green','purple','grey',
          'orange','violet','pink','crimson','dark green','light blue','orange']

consonants=['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
vowels=['A','E','I','O','U']
print("If you want to buy vowel it costs 250 dollars")

# Creating the framework of the wheel
def wheel(colors, radius=250, center=(25, 50)):
    slice_angle = 360 / len(colors)
    heading, position = 90, (center[0] + radius, center[1])
    for color in colors:
        turtle.color('black', color)
        turtle.penup()
        turtle.goto(position)
        turtle.setheading(heading)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(radius, extent=slice_angle)
        heading, position = turtle.heading(), turtle.position()
        turtle.penup()
        turtle.goto(center)
        turtle.end_fill()
    turtle.penup()
    turtle.goto(190,-100)
    turtle.write('800$',True,"center",("Arial",12,"bold"))
    turtle.penup()
    turtle.goto(230,-60)
    turtle.write('470$',True,"center",("Arial",12,"bold"))
    turtle.penup()
    turtle.goto(250,5)
    turtle.write('free-play',True,"right",("Arial",12,"bold"))
    turtle.penup()
    turtle.goto(240,60)
    turtle.write('150$',True,"center",("Arial",12,"bold"))
    turtle.penup()
    turtle.goto(230,120)
    turtle.write('350$',True,"center",("Arial",12,"bold"))
    turtle.penup()
    turtle.goto(210,180)
    turtle.write('1000$',True,"center",("Arial",12,"bold"))        
    turtle.penup()
    turtle.goto(160,220)
    turtle.write('500$',True,"center",("Arial",12,"bold"))        
    turtle.penup()
    turtle.goto(100,250)
    turtle.write('740$',True,"center",("Arial",12,"bold"))    
    turtle.penup()
    turtle.goto(50,260)
    turtle.write('990$',True,"center",("Arial",12,"bold"))
    turtle.penup()
    turtle.goto(0,260)
    turtle.write('1125$',True,"center",("Arial",12,"bold"))
    turtle.penup()
    turtle.goto(-60,255)
    turtle.write('420$',True,"center",("Arial",12,"bold"))
    turtle.penup()
    turtle.goto(-110,220)
    turtle.write('100$',True,"center",("Arial",12,"bold"))
    turtle.penup()
    turtle.goto(-150,180)
    turtle.pencolor('white')
    turtle.write('bankrupt',True,"center",("Arial",12,"bold"))
    turtle.pencolor('black')
    turtle.penup()
    turtle.goto(-190,120)
    turtle.write('5000$',True,"center",("Arial",12,"bold"))
    turtle.penup()
    turtle.goto(-190,60)
    turtle.write('630$',True,"center",("Arial",12,"bold"))
    turtle.penup()
    turtle.goto(-190,20)
    turtle.write('300$',True,"center",("Arial",12,"bold"))
    turtle.penup()
    turtle.goto(-190,-40)
    turtle.write('lose-turn',True,"left",("Arial",12,"bold"))
    turtle.penup()
    turtle.goto(-170,-95)
    turtle.write('880$',True,"center",("Arial",12,"bold"))
    turtle.penup()
    turtle.goto(-115,-130)
    turtle.write('770$',True,"center",("Arial",12,"bold"))
    turtle.penup()
    turtle.goto(-70,-160)
    turtle.write('575$',True,"center",("Arial",12,"bold"))
    turtle.penup()
    turtle.goto(-10,-175)
    turtle.write('690$',True,"center",("Arial",12,"bold"))
    turtle.penup()
    turtle.goto(50,-175)
    turtle.write('50$',True,"center",("Arial",12,"bold"))
    turtle.penup()
    turtle.goto(100,-170)
    turtle.write('1111$',True,"center",("Arial",12,"bold"))
    turtle.penup()
    turtle.goto(150,-140)
    turtle.write('195$',True,"center",("Arial",12,"bold"))
    turtle.hideturtle()
# Taking a random phrase from file, creating players and making letters in phrases as '_' 
w1=[]
line = open('AhladitaN.txt','r')
n=randint(1,75)
for i in range(0,n): 
    w2=line.readline()

for i in range(0,len(w2)-1):
    w1.append(w2[i])

st=False
players=[["P-1",0],["P-2",0],["P-3",0]]

guess=[]
for i in range(0,len(w1)):
    if w1[i]!=" ":
        guess.append("_")
    else:
        guess.append(" ")
# Creating blocks for puzzle in turtle window
def blocks():
    turtle.tracer(0, 0)
    block=turtle.Turtle()
    block.speed(0)
    block.hideturtle()
    block.penup()
    block.color("greenyellow")
    block.shape("square")
    block.setpos(305,305)
    line=turtle.Turtle()
    line.speed(0)
    line.hideturtle()
    line.penup()
    line.color("black")
    line.setpos(307,295)
    for i in range(0,len(w1)):
        if w1[i]!=" ":
            block.stamp()
            line.write(guess[i], font=('Arial', 13, 'bold'), align='center')
            block.fd(30)
            line.fd(30)
        else:
            block.setx(305)
            block.right(90)
            block.fd(50)
            block.left(90)
            line.setx(307)
            line.right(90)
            line.fd(50)
            line.left(90)
    turtle.update()

#Making a marker to spin
def spin():
    
    pen=turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    turtle.tracer(0,0)
    def draw_clock(s,pen):
        pen.clear()
        blocks()
        pen.penup()
        pen.goto(25,50)
        pen.pensize(5)
        pen.color("brown")
        pen.setheading(0)
        angle=(s/60)*360
        pen.rt(angle)
        pen.pendown()
        pen.fd(200)
    global j    
    j=randint(1,60)
    for s in range(j):
        pen.clear()
        draw_clock(s,pen)
        turtle.update()
        if (j-1)==0:
            break

#Creating players name and money earned in turtle window
total=turtle.Turtle()
total.hideturtle()
total.speed(0)
total.color("black")
total.seth(90)
def totals():
    total.clear()
    total.penup()
    total.setpos(-350,100)
    for i in range (0,3):
        total.write(players[i][0], font=('Arial',22, 'bold'), align='center')
        total.right(180)
        total.fd(20)
        total.write(players[i][1], font=('Courier',22, 'bold'), align='center')
        total.fd(70)
        total.right(180)
#This is where overall game process starts
def main(t):
        global st
        st=False
        if t==3:
            t=0
        blocks()
        totals()
        print(guess)
        print(players[t][0],"its your turn!")
        print("You have",players[t][1],"$")
        time.sleep(0.5)
        print("spinning....")
        spin()
        
         

        # Here each sector in the wheel displays an amount

        if j-1 > 2.5 and j-1 <= 5:
            amount=470
            print(amount,"$ you will get multipied by repetition IF CORRECT")
            
            
        elif j-1 > 5 and j-1 <= 7.5:
            amount=800
            print(amount,"$ you will get multipied by repetition IF CORRECT")
            
        elif j-1 > 7.5 and j-1 <= 10:
            amount=195
            print(amount,"$ you will get multipied by repetition IF CORRECT")
            
        elif j-1 > 10 and j-1 <= 12.5:
            amount=1111
            print(amount,"$ you will get multipied by repetition IF CORRECT")
            
        elif j-1 > 12.5 and j-1 <= 15:
            amount=50
            print(amount,"$ you will get multipied by repetition IF CORRECT")
           
        elif j-1 > 15 and j-1 <= 17.5:
            amount=690
            print(amount,"$ you will get multipied by repetition IF CORRECT")
           
        elif j-1 > 17.5 and j-1 <= 20:
            amount=575
            print(amount,"$ you will get multipied by repetition IF CORRECT")
            
        elif j-1 > 20 and j-1 <= 22.5:
            amount=770
            print(amount,"$ you will get multipied by repetition IF CORRECT")
            
        elif j-1 > 22.5 and j-1 <= 25:
            amount=880
            print(amount,"$ you will get multipied by repetition IF CORRECT")
            
        elif j-1 > 27.5 and j-1 <= 30:
            amount=300
            print(amount,"$ you will get multipied by repetition IF CORRECT")
            
        elif j-1 > 30 and j-1 <= 32.5:
            amount=630
            print(amount,"$ you will get multipied by repetition IF CORRECT")
            
        elif j-1 > 32.5 and j-1 <= 35:
            amount=5000
            print(amount,"$ you will get multipied by repetition IF CORRECT")
                    
        elif j-1 > 37.5 and j-1 <= 40:
            amount=100
            print(amount,"$ you will get multipied by repetition IF CORRECT")

        elif j-1 > 40 and j-1 <= 42.5:
            amount=420
            print(amount,"$ you will get multipied by repetition IF CORRECT")
            
        elif j-1 > 42.5 and j-1 <= 45:
            amount=1125
            print(amount,"$ you will get multipied by repetition IF CORRECT")
            
        elif j-1 > 45 and j-1 <= 47.5:
            amount=990
            print(amount,"$ you will get multipied by repetition IF CORRECT")
            
        elif j-1 > 47.5 and j-1 <= 50:
            amount=740
            print(amount,"$ you will get multipied by repetition IF CORRECT")
            
        elif j-1 > 50 and j-1 <= 52.5:
            amount=500
            print(amount,"$ you will get multipied by repetition IF CORRECT")
            
        elif j-1 > 52.5 and j-1 <= 55:
            amount=1000
            print(amount,"$ you will get multipied by repetition IF CORRECT")
            
        elif j-1 > 55 and j-1 <= 57.5:
            amount=350
            print(amount,"$ you will get multipied by repetition IF CORRECT")
            
        elif j-1 > 57.5 and j-1 <= 60:
            amount=150
            print(amount,"$ you will get multipied by repetition IF CORRECT")

        # Allocation of general amount cases, bankrupt, lose a turn and free play    
          
        if (j-1 > 2.5 and j-1 <= 25) or (j-1 > 27.5 and j-1 <= 35) or j-1 > 37.5:
    
            print("Enter 'c' consonant or 'v' for buying vowel: ")
            answer = input()
            if answer=="c":
                consonant=input("Enter Consonant: ").upper()
                for i in range (0,len(w1)-1):
                    if w1[i]==consonant:
                        guess[i]=consonant
                        players[t][1]+= amount
                        
                if consonant in w1:
                    if guess==w1:
                        print("***",players[t][0],"has won***")
                        st=True
                        
                    else:
                        main(t)
                if consonant not in w1:
                    print("Wrong consonant!")
                    
                else:
                    print("What is the guess of phrase??")
                    guessing=input().upper()
                    guessing=[b for b in guessing]
                    print(guessing)
                    if guessing==w1:
                        print("Correct,",players[t][0],"wins!")
                        st=True
                    else:
                        print("Incorrect!")
            elif answer=="v" and players[t][1] >= 250:
                vowel = input("What is the vowel you are buying?: ").upper()
                players[t][1] -= 250
                for i in range (0,len(w1)):
                    if w1[i]==vowel:
                        guess[i]=vowel
                        
                if vowel not in w1:
                    print("Wrong vowel!")
                    
                else:
                    main(t)
            else:
                print(players[t][1],"dollars are not sufficient!")

        elif (j-1 > 35 and j-1 <= 37.5):
            print("Bankrupt!!!!!")
            players[t][1]=0
            

        elif (j-1 > 25 and j-1 <= 27.5) :
            print("Lost a turn!!!!!")
            

        elif(j-1 > 0 and j-1 <= 2.5):
            print("Free play!!!!")
            alphabet=input("enter directly a consonant or a vowel: ").upper()
            for i in range (0,len(w1)):
                if w1[i]==alphabet:
                    guess[i]=alphabet
                    
            if alphabet not in w1:
                print("Incorrect!")
                    
            else:
                print(guess)
                main(t)


     




global next
next=0
wheel(colors, 250, center=(25,50))
blocks()
totals()
while st != True:
    main(next)
    next+=1
blocks()
