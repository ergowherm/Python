
#http://anh.cs.luc.edu/handsonPythonTutorial/graphics.html
""" Graphics program """""

"""from graphics import *


def main():
    win = GraphWin('Face', 200, 150) # give title and dimensions
    win.yUp() # make right side up coordinates!

    head = Circle(Point(40,100), 25) # set center and radius
    head.setFill("yellow")
    head.draw(win)

    eye1 = Circle(Point(30, 105), 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2 = Line(Point(45, 105), Point(55, 105)) # set endpoints
    eye2.setWidth(3)
    eye2.draw(win)

    mouth = Oval(Point(30, 90), Point(50, 85)) # set corners of bounding box
    mouth.setFill("red")
    mouth.draw(win)

    label = Text(Point(100, 120), 'A face')
    label.draw(win)

    message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()

main()"""

"""from graphics import *


def main():
    win = GraphWin('Face', 200, 150) # give title and dimensions
    win.setCoords(0, 0, 199, 149)

    head = Circle(Point(40,100), 25) # set center and radius
    head.setFill("yellow")
    head.draw(win)

    eye1 = Circle(Point(30, 105), 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2 = Line(Point(45, 105), Point(55, 105)) # set endpoints
    eye2.setWidth(3)
    eye2.draw(win)

    mouth = Oval(Point(30, 90), Point(50, 85)) # set corners of bounding box
    mouth.setFill("red")
    mouth.draw(win)

    label = Text(Point(100, 120), 'A face')
    label.draw(win)

    message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()

main()"""

#example:

'''Program: triangle.py or triangle.pyw (best name for Windows)
Interactive graphics program to draw a triangle,
with prompts in a Text object and feedback via mouse clicks.
'''

"""from graphics import *

def main():
    win = GraphWin('Draw a Triangle', 350, 350)
    win.setCoords(0, 0, 349, 349)
    win.setBackground('yellow')
    message = Text(Point(win.getWidth()/2, 30), 'Click on three points')
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(20)
    message.draw(win)

    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    vertices = [p1, p2, p3]

    # Use Polygon object to draw the triangle
    triangle = Polygon(vertices)
    triangle.setFill('gray')
    triangle.setOutline('cyan')
    triangle.setWidth(4)  # width of boundary line
    triangle.draw(win)

    message.setText('Click anywhere to quit') # change text message
    win.getMouse()
    win.close() 

main()"""

#Animation
'''Test animation and depth.
'''

"""from graphics import *
import time

def main():
    win = GraphWin('Back and Forth', 300, 300)
    win.setCoords(0, 0, 299, 299)

    rect = Rectangle(Point(200, 90), Point(220, 100))
    rect.setFill("blue")
    rect.draw(win)

    cir1 = Circle(Point(40,100), 25)
    cir1.setFill("yellow")
    cir1.draw(win)
    
    cir2 = Circle(Point(150,125), 25)
    cir2.setFill("red")
    cir2.draw(win)

    for i in range(46):
        cir1.move(5, 0)
        time.sleep(.05)

    for i in range(46):
        cir1.move(-5, 0)
        time.sleep(.05)

    win.getMouse()
    win.close()

main()"""

#Example

'''Test animation of a group of objects making a face.
'''

"""from graphics import *
import time

def moveAll(shapeList, dx, dy):
    ''' Move all shapes in shapeList by (dx, dy).'''   
    for shape in shapeList: 
        shape.move(dx, dy)
            

def moveAllOnLine(shapeList, dx, dy, repetitions, delay):
    '''Animate the shapes in shapeList along a line.
    Move by (dx, dy) each time.
    Repeat the specified number of repetitions.
    Have the specified delay (in seconds) after each repeat.
    '''
    for i in range(repetitions):
        moveAll(shapeList, dx, dy)
        time.sleep(delay)
        

def main():
    win = GraphWin('Back and Forth', 300, 300)
    win.setCoords(0, 0, 299, 299)

    rect = Rectangle(Point(200, 90), Point(220, 100))
    rect.setFill("blue")
    rect.draw(win)

    head = Circle(Point(40,100), 25)
    head.setFill("yellow")
    head.draw(win)

    eye1 = Circle(Point(30, 105), 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2 = Line(Point(45, 105), Point(55, 105))
    eye2.setWidth(3)
    eye2.draw(win)

    mouth = Oval(Point(30, 90), Point(50, 85))
    mouth.setFill("red")
    mouth.draw(win)

    faceList = [head, eye1, eye2, mouth]
    
    cir2 = Circle(Point(150,125), 25)
    cir2.setFill("red")
    cir2.draw(win)

    moveAllOnLine(faceList, 5, 0, 46, .05)
    moveAllOnLine(faceList, -5, 0, 46, .05)

    win.getMouse()
    win.close()

main() """

#example



