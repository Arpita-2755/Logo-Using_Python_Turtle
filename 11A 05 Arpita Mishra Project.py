import turtle

t = turtle.Turtle()

t.speed(10)

t.width(8)

t.getscreen().bgcolor("black")

t.color("red")
t.begin_fill
t.forward(150)
t.right(90)

t.circle(-150,240)
t.end_fill

t.penup()

t.home()

t.forward(135)
t.right(90)
t.forward(10)

t.pendown()
t.color("cyan")
t.begin_fill

t.circle(-120,70)

t.penup()
t.circle(-150,40)
t.pendown()

t.circle(-130,240)
t.end_fill

t.penup()

t.home()

t.forward(118)
t.right(90)
t.forward(10)
t.circle(-110,30)
t.pendown()

t.color("red")
t.begin_fill
t.circle(-115,300)

t.end_fill

t.penup()
t.home()
t.forward(100)
t.right(90)
t.forward(10)

t.pendown()

t.color("green")
t.begin_fill
t.circle(-95,160)

t.penup()
t.circle(-95,20)
t.pendown()

t.circle(-95,160)

t.end_fill

t.penup()
t.home()
t.left(90)
t.forward(150)
t.left(90)
t.forward(250)
t.backward(10)
t.pendown()
t.color("red")

t.write("Gopinath Classes",move=False,align="left",font=("Arial Black",40))

t.width(2)
t.color("cyan")
t.backward(500)

t.penup()
t.home()
t.right(90)
t.forward(200)
t.right(90)
t.forward(180)
t.backward(10)
t.pendown()
t.width(8)
t.color("red")

t.write("Realize Your Potential",move=False,align="left",font=("Berlin Sans FB",30))

turtle.done()

