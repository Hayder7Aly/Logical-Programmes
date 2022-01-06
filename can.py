from tkinter import *
root=Tk()
can=Canvas(root,bg='cyan',width=320,height=320)
can.pack()

can.create_oval((10,10,300,300),fill='yellow')

can.create_arc((50,100,100,150),extent=180,fill='black')
can.create_arc((200,100,250,150),extent=180,fill='black')


can.create_line((50,200,110,240),fill='red',width=5)
can.create_line((110,240,190,240),fill='red',width=5)
can.create_line((190,240,250,200),fill='red',width=5)



root.mainloop()