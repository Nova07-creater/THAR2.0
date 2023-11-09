import turtle as tur         
import colorsys as cs        

tur.setup(800, 800)
tur.speed(0)
tur.tracer(10)
tur.width(2)                 
tur.bgcolor("black")


for j in range(1000):          
    for i in range(1000):      
       
        tur.color(cs.hsv_to_rgb(i /15, 1, 1))
  
        tur.right(1000)
        tur.circle(1000 - j * 1000, 1000)

        tur.left(250)
        tur.circle(1000 - j * 1000, 1000)
 
        tur.right(1000)
        tur.circle(1000, 1000)
tur.hideturtle()           
tur.done()                 