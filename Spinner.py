"""press 'a' to spin left and 'd' ro spin right"""
import turtle 

state = {'turn':0}

def spinner():
    turtle.clear()
    angle = state['turn'] / 20
    turtle.right(angle)
    
    turtle.forward(100)
    turtle.dot(120,'red')
    turtle.back(100)
    turtle.left(120)

    turtle.forward(100)
    turtle.dot(120,'yellow')
    turtle.back(100)
    turtle.left(120)

    turtle.forward(100)
    turtle.dot(120,'blue')
    turtle.back(100)
    turtle.left(120)

    turtle.update()
def animate():
    if state['turn']>0:
        state['turn'] -=1   
    elif state['turn']<0:
        state['turn'] +=1     
    spinner()                   
    turtle.update()
    turtle.ontimer(animate,20)  

def flick_right():
    state['turn'] += 50

def flick_left():
    state['turn'] -= 50

turtle.tracer(False)
turtle.width(40)
turtle.color("#000000")

turtle.onkey(flick_right,'d')
turtle.onkey(flick_left,'a')

turtle.listen()
animate()
turtle.done()
