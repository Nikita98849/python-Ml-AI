from tkinter import *   
  
top = Tk()  
  
top.geometry("200x200")  
  
#creating a simple canvas  
c = Canvas(top,bg = "yellow",height = "300",width = "300")  
  
arc = c.create_arc((7,15,100,150),start = 0,extent = 150, fill= "blue")  
  
c.pack()  
  
top.mainloop()  
