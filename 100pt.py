#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in collision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")
direction = 4


class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.up = Button(self.myContainer1)
		self.up.configure(text="Up", background= "orange")
		self.up.grid(row=0,column=1)
					
		# "Bind" an action to the first button												
		self.up.bind("<Button-1>", self.moveUp)
		    #button 2
	        self.button2 = Button(self.myContainer1)
	        self.button2.configure(text="Right", background= "yellow")
	        self.button2.grid(row=1,column=3)
	        self.button2.bind("<Button-1>", self.button2Click)
		
		#button 3
   	        self.button3 = Button(self.myContainer1)
	        self.button3.configure(text="Left", background= "yellow")
	        self.button3.grid(row=1,column=0)
	        self.button3.bind("<Button-1>", self.button3Click)	
		
		#button 4
	        self.button4 = Button(self.myContainer1)
	        self.button4.configure(text="Down", background= "orange")
	        self.button4.grid(row=3,column=1)
	        self.button4.bind("<Button-1>", self.button4Click)	
                
		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		self.animate()

		
	def moveUp(self, event):   
	   global player
	   global drawpad
           x1,y1,x2,y2 = drawpad.coords(player)
	   if y1 > 0:
              drawpad.move(player,0,-10)
         
        #button 2	
	def button2Click(self, event):
	    global oval
	    global drawpad
	    x1,y1,x2,y2 = drawpad.coords(player)
	    if x2 <drawpad.winfo_width():
	        drawpad.move(player,10,0)
	#button 3
	def button3Click(self, event):
	    global oval
	    global drawpad
	    x1,y1,x2,y2 = drawpad.coords(player)
	    if x1 >0:
	        drawpad.move(player,-10,0)
	#button 4
	def button4Click(self, event):
	    global oval
	    global drawpad
	    x1,y1,x2,y2 = drawpad.coords(player)
	    if y2 < drawpad.winfo_height():
               drawpad.move(player,0,10)
         
	    
	  
	
    
         
        # Animate function that will bounce target left and right, and trigger the collision detection  
	def animate(self):
	    global target
	    global direction
	    tx1,ty1,tx2,ty2=drawpad.coords(target)
	    
	    if tx1 < 0:
	       direction = 10
	    if tx2 > 480:
	       direction = -10
	    drawpad.move(target,direction,0)
	    
	    
	    didWeHit = self.collisionDetect()
            if didWeHit:
                drawpad.after(10, self.animate)
           
            # Use the value of didWeHit to create an if statement
            # that determines whether to run drawpad.after(1,self.animate) or not
            
	# Use a function to do our collision detection
	def collisionDetect(self):
                global target
		global drawpad
                global player
                x1,y1,x2,y2=drawpad.coords(player)
                tx1,ty1,tx2,ty2=drawpad.coords(target)
                if (x1 > tx1 and x2 < tx2) and (y1 > ty1 and y2 < ty2):
                    return False
                else:
                    return True
                             
		
myapp = MyApp(root)

root.mainloop()