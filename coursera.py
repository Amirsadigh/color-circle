import turtle as t 
colors = [ "orange" , "red" , "pink" , "yellow" , "blue" , "green" ,"purple" , "brown"]
for x in range (360):
    t.pencolor(colors[x %  8])
    t.width(x / 5 + 1 )
    t.forward(x)
    t.left(20)

