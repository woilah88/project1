import turtle


screen = turtle.Screen()
screen.bgcolor("white")


pen = turtle.Turtle()
pen.pensize(5)
pen.color("green")


pen.penup()
pen.goto(-50, -100)  
pen.pendown()

pen.left(90)         
pen.forward(200)     

pen.right(135)       
pen.forward(100)     

pen.left(90)         
pen.forward(100)     

pen.right(135)       
pen.forward(200)     


pen.hideturtle()
screen.mainloop()
