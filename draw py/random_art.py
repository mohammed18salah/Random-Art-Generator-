import turtle
import random
import math

def draw_heart():
    t = turtle.Turtle()
    t.speed(3)  # Slower speed
    t.pensize(2)
    t.color('hot pink')
    t.begin_fill()
    
    t.left(140)
    t.forward(180)
    for _ in range(200):
        t.right(1)
        t.forward(2)
    t.left(120)
    for _ in range(200):
        t.right(1)
        t.forward(2)
    t.forward(180)
    
    t.end_fill()
    t.hideturtle()

def draw_rose():
    t = turtle.Turtle()
    t.speed(3)  # Slower speed
    t.pensize(2)
    t.color('deep pink')
    
    # Draw the flower
    t.begin_fill()
    for i in range(360):
        radius = 150 * math.sin(math.radians(i * 4))
        t.forward(radius / 50)
        t.left(5)
    t.end_fill()
    
    # Draw stem
    t.penup()
    t.goto(0, -200)
    t.setheading(90)
    t.color('lime green')
    t.pendown()
    t.forward(200)
    
    t.hideturtle()

def draw_snake():
    t = turtle.Turtle()
    t.speed(3)  # Slower speed
    t.pensize(3)
    
    # Draw snake body
    t.color('lime green', 'green yellow')
    t.begin_fill()
    
    # Starting position
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    
    # Draw snake's wavy body
    for i in range(4):
        t.circle(50, 90)
        t.circle(-50, 90)
    
    t.end_fill()
    
    # Draw snake's head
    t.penup()
    t.goto(50, 0)
    t.color('yellow green', 'forest green')
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    
    # Draw eyes
    t.penup()
    t.goto(60, 25)
    t.color('red')
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    
    t.penup()
    t.goto(60, 15)
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    
    # Draw tongue
    t.penup()
    t.goto(70, 20)
    t.color('red')
    t.pendown()
    t.forward(20)
    t.right(45)
    t.forward(10)
    t.backward(10)
    t.left(90)
    t.forward(10)
    
    t.hideturtle()

def main():
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Random Art - Rose, Heart, or Snake")
    screen.bgcolor('black')
    screen.tracer(1)  # Normal speed
    
    # Randomly choose between heart, rose, or snake
    choice = random.choice(['heart', 'rose', 'snake'])
    if choice == 'heart':
        draw_heart()
    elif choice == 'rose':
        draw_rose()
    else:
        draw_snake()
    
    screen.exitonclick()

if __name__ == "__main__":
    main() 